import sys
from helpers import SetUp
import masking_constants as Masks


class State:
    dataval = []
    PC = 96
    cycle = 1
    R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __init__(self, opcodes, dataval, addrs, arg1, arg2, arg3, numInstructs, opcodeStr, arg1Str, arg2Str, arg3Str):
        self.opcode = opcodes
        self.dataval = dataval
        self.address = addrs
        self.numInstructs = numInstructs
        self.arg1 = arg1
        self.arg2 = arg2
        self.arg3 = arg3
        self.opcodeStr = opcodeStr
        self.arg1Str = arg1Str
        self.arg2Str = arg2Str
        self.arg3Str = arg3Str

    def getIndexOfMemAddress(self, currAddr):
        return int((currAddr - 96) / 4)

    def incrementPC(self):
        self.PC = self.PC + 4

    def printState(self):
        outputFileName = SetUp.get_output_filename()

        with open(outputFileName + "_sim.txt", 'a') as outFile:

            i = self.getIndexOfMemAddress(self.PC)
            outFile.write("====================\n")
            """   """
            outFile.write("cycle:" + str(self.cycle) + "\t" + str(self.PC) + "\t" + str(self.opcodeStr[i]) +
                          self.arg1Str[i] + self.arg2Str[i] + self.arg3Str[i] + "\n")
            outFile.write("\n" + "registers:" + "\t" + str(self.PC) + "\t")

            regNumber = 0

            while regNumber < len(self.R):
                if (regNumber % 8) == 0:
                    outFile.write("\n" + "r0" + str(int(regNumber)) + ":\t" + str(self.R[regNumber]) + "\t")
                else:
                    outFile.write(str(self.R[regNumber]) + "\t")
                regNumber += 1

            outStr = ""

            for i in range(len(self.dataval)):
                if (i % 8) == 0 and i != 0 or i == len(self.dataval):
                    outFile.write(outStr + "\n")
                if (i % 8) == 0:
                    outStr = str(self.address[i + self.numInstructs]) + ":" + str(self.dataval[i])
                if (i % 8) != 0:
                    outStr = outStr + "\t" + str(self.dataval[i])

            outFile.write(outStr + "\n")
            outFile.close()


class Simulator:

    def __init__(self, instructions, opcode, opcodeStr, arg1, arg1Str, arg2, arg2Str, arg3, arg3Str, dataval, address,
                 numInstructs):
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
        self.specialMask = Masks.specialMask

    def run(self):
        foundBreak = False
        armState = State(self.opcode, self.dataval, self.address, self.arg1, self.arg2, self.arg3, self.numInstructs,
                         self.opcodeStr, self.arg1Str, self.arg2Str, self.arg3Str)
        print(len(self.dataval))
        armState.printState()
