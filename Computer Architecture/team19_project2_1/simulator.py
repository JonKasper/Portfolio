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
            outFile.write("cycle: " + str(self.cycle) + "\t" + str(self.PC) + "\t" + str(self.opcodeStr[i]) +
                          self.arg1Str[i] + self.arg2Str[i] + self.arg3Str[i] + "\n")
            outFile.write("\n" + "registers:")

            regNumber = 0

            while regNumber < len(self.R):
                if (regNumber % 8) == 0:
                    outFile.write("\n" + "r" + str(int(regNumber)).zfill(2) + ":\t" + str(self.R[regNumber]) + "\t")
                else:
                    outFile.write(str(self.R[regNumber]) + "\t")
                regNumber += 1

            outFile.write("\n\ndata: \n")
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

        while foundBreak == False:
            jumpAddr = armState.PC
            # get the next instruction
            i = armState.getIndexOfMemAddress(armState.PC)

            if self.opcode[i] == 0:  # NOP
                armState.printState()
                armState.incrementPC()
                armState.cycle += 1
                continue
            elif 160 <= self.opcode[i] <= 191:  # B
                jumpAddr = jumpAddr + ((self.arg1[i] * 4) - 4)
            elif self.opcode[i] == 1104:  # AND
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] & armState.R[self.arg1[i]]
            elif self.opcode[i] == 1112:  # ADD
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] + armState.R[self.arg1[i]]
            elif 1160 <= self.opcode[i] <= 1161:  # ADDI
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] + self.arg1[i]
            elif self.opcode[i] == 1360:  # ORR
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] | armState.R[self.arg1[i]]
            elif 1440 <= self.opcode[i] <= 1447:  # CBZ
                if armState.R[self.arg2[i]] == 0:
                    jumpAddr = jumpAddr + ((self.arg1[i] * 4) - 4)
            elif 1448 <= self.opcode[i] <= 1455:  # CBNZ
                if armState.R[self.arg2[i]] != 0:
                    jumpAddr = jumpAddr + ((self.arg1[i] * 4) - 4)
            elif self.opcode[i] == 1872:  # EOR
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] ^ armState.R[self.arg1[i]]
            elif self.opcode[i] == 1692:  # ASR
                armState.R[self.arg3[i]] = armState.R[self.arg1[i]] >> armState.R[self.arg2[i]]
            elif self.opcode[i] == 1691:  # LSL
                armState.R[self.arg3[i]] = (armState.R[self.arg1[i]] * pow(2, self.arg2[i]))
            elif self.opcode[i] == 1690:  # LSR
                armState.R[self.arg3[i]] = int(armState.R[self.arg1[i]] / pow(2, self.arg2[i]))
            elif self.opcode[i] == 1624:  # SUB
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] - armState.R[self.arg1[i]]
            elif 1672 <= self.opcode[i] <= 1673:  # SUBI
                armState.R[self.arg3[i]] = armState.R[self.arg2[i]] - self.arg1[i]
            elif 1684 <= self.opcode[i] <= 1687:  # MOVZ
                armState.R[self.arg3[i]] = self.arg2[i] << self.arg1[i]
            elif 1940 <= self.opcode[i] <= 1943:  # MOVK
                armState.R[self.arg3[i]] = armState.R[self.arg3[i]] | (self.arg2[i] << self.arg1[i])
            elif self.opcode[i] == 1984:  # STUR
                # check if the store location is outside the range of the data values
                length = int(
                    ((armState.R[self.arg2[i]] + (self.arg1[i] * 4)) - self.address[self.numInstructs - 1]) / 4)
                if length > (len(armState.dataval) - 1):
                    # append 0s to the end of dataval until the new length
                    for z in range((len(armState.dataval) - 1), length):
                        if z == (length - 1):
                            # store the value in the new location
                            armState.dataval[int(((armState.R[self.arg2[i]] + (self.arg1[i] * 4)) - self.address[
                                self.numInstructs - 1]) / 4) - 1] = armState.R[self.arg3[i]]
                        else:
                            armState.dataval.append(0)
                else:
                    armState.dataval[int(((armState.R[self.arg2[i]] + (self.arg1[i] * 4)) - self.address[
                        self.numInstructs - 1]) / 4) - 1] = armState.R[self.arg3[i]]
            elif self.opcode[i] == 1986:  # LDUR
                armState.R[self.arg3[i]] = armState.dataval[int(
                    ((armState.R[self.arg2[i]] + (self.arg1[i] * 4)) - self.address[self.numInstructs - 1]) / 4) - 1]
            elif self.opcode[i] == 2038:  # BREAK
                foundBreak = True
            else:
                print("IN SIM -- UNKNOWN INSTRUCTION --------------------- !!!!")

            armState.printState()
            armState.PC = jumpAddr
            armState.incrementPC()
            armState.cycle += 1
