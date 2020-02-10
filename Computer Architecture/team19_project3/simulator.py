import sys
from helpers import SetUp
import masking_constants as Masks
from writeBack import WriteBack
from mem import MEM
from alu import ALU
from cache import Cache
from issue import ISSUE
from instruction_fetch import IF


class Simulator:

    def __init__(self, instructions, opcode, opcodeStr, arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, dataval, address,
                 numInstructs, destReg, src1Reg, src2Reg):
        self.instructions = instructions
        self.opcode = opcode
        self.dataval = dataval
        self.address = address
        self.numInstructs = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str
        self.destReg = destReg
        self.src1Reg = src1Reg
        self.src2Reg = src2Reg
        self.specialMask = Masks.specialMask
        self.PC = 96
        self.cycle = 1
        self.R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.postMEMbuff = [-1, -1]
        self.postALUbuff = [-1, -1]
        self.preMEMbuff = [-1, -1]
        self.preALUbuff = [-1, -1]
        self.preIssueBuff = [-1, -1, -1, -1]

        self.WB = WriteBack(self)
        self.mem = MEM(self)
        self.alu = ALU(self)
        self.cache = Cache(self.numInstructs, self.instructions, self.dataval, self.address)
        self.issue = ISSUE(self)
        self.fetch = IF(self)

    def printState(self):
        outputFileName = SetUp.get_output_filename()

        with open(outputFileName + "_pipeline.txt", 'a') as outFile:
            outFile.write("--------------------\n")
            outFile.write("Cycle: " + str(self.cycle) + "\n\n")

            # print the pre issue buffer
            outFile.write("Pre-Issue Buffer:\n")
            for i in range(0, len(self.preIssueBuff)):
                outFile.write("\tEntry " + str(i) + ":\t")

                if self.preIssueBuff[i] != -1:
                    outFile.write("[" + str(self.opcodeStr[self.preIssueBuff[i]]) + self.arg1Str[self.preIssueBuff[i]] +
                                  self.arg2Str[self.preIssueBuff[i]] + self.arg3Str[self.preIssueBuff[i]] + "]\n")
                else:
                    outFile.write("\n")

            # print the pre alu buffer
            outFile.write("Pre-ALU Queue:\n")
            for i in range(0, len(self.preALUbuff)):
                outFile.write("\tEntry " + str(i) + ":\t")

                if self.preALUbuff[i] != -1:
                    outFile.write("[" + self.opcodeStr[self.preALUbuff[i]] + self.arg1Str[self.preALUbuff[i]] +
                                  self.arg2Str[self.preALUbuff[i]] + self.arg3Str[self.preALUbuff[i]] + "]\n")
                else:
                    outFile.write("\n")

            # print the post alu buffer
            outFile.write("Post-ALU Queue:\n")
            outFile.write("\tEntry 0:\t")
            if self.postALUbuff[0] != -1:
                outFile.write("[" + self.opcodeStr[self.postALUbuff[1]] + self.arg1Str[self.postALUbuff[1]] +
                              self.arg2Str[self.postALUbuff[1]] + self.arg3Str[self.postALUbuff[1]] + "]\n")
            else:
                outFile.write("\n")

            # print the pre mem buff
            outFile.write("Pre-MEM Queue:\n")
            for i in range(0, len(self.preMEMbuff)):
                outFile.write("\tEntry " + str(i) + ":\t")

                if self.preMEMbuff[i] != -1:
                    outFile.write("[" + self.opcodeStr[self.preMEMbuff[i]] + self.arg1Str[self.preMEMbuff[i]] +
                                  self.arg2Str[self.preMEMbuff[i]] + self.arg3Str[self.preMEMbuff[i]] + "]\n")
                else:
                    outFile.write("\n")

            # print the post mem buff
            outFile.write("Post-MEM Queue:\n")
            outFile.write("\tEntry 0:\t")
            if self.postMEMbuff[0] != -1:
                outFile.write("[" + self.opcodeStr[self.postMEMbuff[0]] + self.arg1Str[self.postMEMbuff[0]] +
                              self.arg2Str[self.postMEMbuff[0]] + self.arg3Str[self.postMEMbuff[0]] + "]\n\n")
            else:
                outFile.write("\n\n")

            # print the Register list
            outFile.write("Registers:\n")
            regNumber = 0

            while regNumber < len(self.R):
                if (regNumber % 8) == 0:
                    outFile.write("\n" + "r" + str(int(regNumber)).zfill(2) + ":\t" + str(self.R[regNumber]) + "\t")
                else:
                    outFile.write(str(self.R[regNumber]) + "\t")
                regNumber += 1

            # print the cache list
            outFile.write("\n\nCache:\n")
            for i in range(0, len(self.cache.cacheSets)):
                outFile.write("Set " + str(i) + ":\tLRU=" + str(self.cache.lruBit[i]) + "\n")
                for j in range(0, len(self.cache.cacheSets[i])):
                    outFile.write("\tEntry " + str(j) + ":[(")
                    for k in range(3):
                        if k != 2:
                            outFile.write(str(self.cache.cacheSets[i][j][k]) + ",")
                        else:
                            outFile.write(str(self.cache.cacheSets[i][j][k]) + ")<")
                    outFile.write(str(self.cache.cacheSets[i][j][3]) + "," + str(self.cache.cacheSets[i][j][4]) +">]")
                    outFile.write("\n")

            # print the data list
            outFile.write("\nData\n")
            if len(self.dataval) != 0:
                outStr = ""

                a = self.address[self.numInstructs - 1] + 4
                for i in range(len(self.dataval)):
                    if (i % 8) == 0 and i != 0 or i == len(self.dataval):
                        outFile.write(outStr + "\n")
                    if (i % 8) == 0:
                        outStr = str(a) + ":\t" + str(self.dataval[i])
                        a += (8 * 4)
                    if (i % 8) != 0:
                        outStr = outStr + "\t" + str(self.dataval[i])

                outFile.write(outStr + "\n")
            outFile.write("\n\n\n")

        outFile.close()

    def run(self):

        go = True

        while go:
            self.WB.run()
            self.alu.run()
            self.mem.run()
            self.issue.run()
            go = self.fetch.run()
            self.printState()
            self.cycle += 1

            if not go:
                if self.preIssueBuff.count(-1) != 4:
                    go = True
                if self.preMEMbuff.count(-1) != 2:
                    go = True
                if self.preALUbuff.count(-1) != 2:
                    go = True
                if self.postMEMbuff.count(-1) != 2:
                    go = True
                if self.postALUbuff.count(-1) != 2:
                    go = True

            self.cache.flush()
