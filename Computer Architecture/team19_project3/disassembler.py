# test comment
# TO DO:    create algorithm for hashing
#           create algorithm for checking the breakdown against the instruction code

# algorithm for hashing

from helpers import SetUp
import os
import masking_constants as Masks
import sys


class Disassembler:

    def __init__(self):

        self.bMask = Masks.bMask
        self.jAddrMask = Masks.jAddrMask
        self.specialMask = Masks.specialMask
        self.rnMask = Masks.rnMask
        self.rmMask = Masks.rmMask
        self.rdMask = Masks.rdMask
        self.imMask = Masks.imMask
        self.shmtMask = Masks.shmtMask
        self.addrMask = Masks.addrMask
        self.addr2Mask = Masks.addr2Mask
        self.imsftMask = Masks.imsftMask
        self.imdataMask = Masks.imdataMask

    opcodeStr = []
    instrSpaced = []
    arg1 = []
    arg2 = []
    arg3 = []
    arg1Str = []
    arg2Str = []
    arg3Str = []
    destReg = []
    src1Reg = []
    src2Reg = []
    dataval = []
    rawdata = []
    address = []
    numInstructs = 0

    def run(self):

        instructions = []
        inputfile = SetUp.get_input_filename()
        instructions = SetUp.import_data_file()

        outputFilename = SetUp.get_output_filename()

        print("raw output filename is ", outputFilename)

        # create an address list with appropriate length
        for i in range(len(instructions)):
            self.address.append(96 + (i * 4))

        opcode = []

        # create an opcode list by selecting the left 11 bits
        for z in instructions:
            opcode.append(int(z, base=2) >> 21)

        # decode and dissect :) no bugs in this class

        for i in range(len(opcode)):
            self.numInstructs = self.numInstructs + 1
            if opcode[i] == 1112:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ADD")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1104:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("AND")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1360:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ORR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1624:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("SUB")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1690:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(-1)
            elif opcode[i] == 1691:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("LSL")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.shmtMask) >> 10)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", #" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(-2)
            elif opcode[i] == 1692:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("ASR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1872:
                self.instrSpaced.append(SetUp.bin2StringSpacedR(instructions[i]))
                self.opcodeStr.append("EOR")
                self.arg1.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg2.append((int(instructions[i], base=2) & self.rmMask) >> 16)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg1[i]))
                self.arg3Str.append(", R" + str(self.arg2[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(self.arg1[i])
                self.src2Reg.append(self.arg2[i])
            elif 1684 <= opcode[i] <= 1687:
                self.instrSpaced.append(SetUp.bin2StringSpacedIM(instructions[i]))
                self.opcodeStr.append("MOVZ")
                self.arg1.append(((int(instructions[i], base=2) & self.imsftMask) >> 21) * 16)
                self.arg2.append((int(instructions[i], base=2) & self.imdataMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", " + str(self.arg2[i]))
                self.arg3Str.append(", LSL " + str(self.arg1[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(-3)
                self.src2Reg.append(-4)
            elif 1940 <= opcode[i] <= 1943:
                self.instrSpaced.append(SetUp.bin2StringSpacedIM(instructions[i]))
                self.opcodeStr.append("MOVK")
                self.arg1.append(((int(instructions[i], base=2) & self.imsftMask) >> 21) * 16)
                self.arg2.append((int(instructions[i], base=2) & self.imdataMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", " + str(self.arg2[i]))
                self.arg3Str.append(", LSL " + str(self.arg1[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(-5)
                self.src2Reg.append(-6)
            elif 1440 <= opcode[i] <= 1447:
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBZ")
                self.arg1.append(
                    SetUp.imm_bit_to_32_bit_converter((int(instructions[i], base=2) & self.addr2Mask) >> 5, 19))
                self.arg2.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg3.append(0)
                self.arg1Str.append("\tR" + str(self.arg2[i]))
                self.arg2Str.append(", #" + str(self.arg1[i]))
                self.arg3Str.append("")
                self.destReg.append(-7)
                self.src1Reg.append(-8)
                self.src2Reg.append(-9)
            elif 1448 <= opcode[i] <= 1455:
                self.instrSpaced.append(SetUp.bin2StringSpacedCB(instructions[i]))
                self.opcodeStr.append("CBNZ")
                self.arg1.append(
                    SetUp.imm_bit_to_32_bit_converter((int(instructions[i], base=2) & self.addr2Mask) >> 5, 19))
                self.arg2.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg3.append(0)
                self.arg1Str.append("\tR" + str(self.arg2[i]))
                self.arg2Str.append(", #" + str(self.arg1[i]))
                self.arg3Str.append("")
                self.destReg.append(-10)
                self.src1Reg.append(-11)
                self.src2Reg.append(-12)
            elif 1160 <= opcode[i] <= 1161:
                self.instrSpaced.append(SetUp.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("ADDI")
                self.arg1.append((int(instructions[i], base=2) & self.imMask) >> 10)
                self.arg2.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(-13)
                self.src2Reg.append(self.arg2[i])
            elif 1672 <= opcode[i] <= 1673:
                self.instrSpaced.append(SetUp.bin2StringSpacedI(instructions[i]))
                self.opcodeStr.append("SUBI")
                self.arg1.append((int(instructions[i], base=2) & self.imMask) >> 10)
                self.arg2.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]))
                self.destReg.append(self.arg3[i])
                self.src1Reg.append(-14)
                self.src2Reg.append(self.arg2[i])
            elif opcode[i] == 1984:
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("STUR")
                self.arg1.append((int(instructions[i], base=2) & self.addrMask) >> 12)
                self.arg2.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", [R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]) + "]")
                self.destReg.append(-15)
                self.src1Reg.append(-16)
                self.src2Reg.append(-17)
            elif opcode[i] == 1986:
                self.instrSpaced.append(SetUp.bin2StringSpacedD(instructions[i]))
                self.opcodeStr.append("LDUR")
                self.arg1.append((int(instructions[i], base=2) & self.addrMask) >> 12)
                self.arg2.append((int(instructions[i], base=2) & self.rnMask) >> 5)
                self.arg3.append((int(instructions[i], base=2) & self.rdMask) >> 0)
                self.arg1Str.append("\tR" + str(self.arg3[i]))
                self.arg2Str.append(", [R" + str(self.arg2[i]))
                self.arg3Str.append(", #" + str(self.arg1[i]) + "]")
                self.destReg.append(-18)
                self.src1Reg.append(-18)
                self.src2Reg.append(-19)
            elif 160 <= opcode[i] <= 191:
                self.instrSpaced.append(SetUp.bin2StringSpacedB(instructions[i]))
                self.opcodeStr.append("B")
                self.arg1.append(SetUp.imm_bit_to_32_bit_converter(int(instructions[i], base=2) & self.bMask, 26))
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("\t#" + str(self.arg1[i]))
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.destReg.append(-20)
                self.src1Reg.append(-21)
                self.src2Reg.append(-22)
            elif opcode[i] == 0:
                if int(instructions[i], base=2) == 0:
                    self.instrSpaced.append(SetUp.bin2StringSpaced(instructions[i]))
                    self.opcodeStr.append("NOP")
                    self.arg1.append(0)
                    self.arg2.append(0)
                    self.arg3.append(0)
                    self.arg1Str.append("")
                    self.arg2Str.append("")
                    self.arg3Str.append("")
                    self.destReg.append(-23)
                    self.src1Reg.append(-24)
                    self.src2Reg.append(-25)
                else:
                    self.instrSpaced.append(instructions[i])
                    self.opcodeStr.append(SetUp.immSignedToTwosConverter(int(instructions[i], base=2)))
                    self.arg1.append(0)
                    self.arg2.append(0)
                    self.arg3.append(0)
                    self.arg1Str.append("")
                    self.arg2Str.append("")
                    self.arg3Str.append("")
                    self.dataval.append(int(instructions[i], base=2))
                    self.numInstructs -= 1
            elif opcode[i] == 2038:
                self.instrSpaced.append(SetUp.bin2StringSpaced(instructions[i]))
                self.opcodeStr.append("BREAK")
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.destReg.append(-26)
                self.src1Reg.append(-27)
                self.src2Reg.append(-28)
            else:
                self.instrSpaced.append(instructions[i])
                self.opcodeStr.append(SetUp.immSignedToTwosConverter(int(instructions[i], base=2)))
                self.arg1.append(0)
                self.arg2.append(0)
                self.arg3.append(0)
                self.arg1Str.append("")
                self.arg2Str.append("")
                self.arg3Str.append("")
                self.dataval.append(int(instructions[i], base=2))
                self.numInstructs -= 1
        return {
            "instructions": instructions,
            "opcode": opcode,
            "opcodeStr": self.opcodeStr,
            "arg1": self.arg1,
            "arg1Str": self.arg1Str,
            "arg2": self.arg2,
            "arg2Str": self.arg2Str,
            "arg3": self.arg3,
            "arg3Str": self.arg3Str,
            "destReg": self.destReg,
            "src1Reg": self.src1Reg,
            "src2Reg": self.src2Reg,
            "dataval": self.dataval,
            "address": self.address,
            "numInstructs": self.numInstructs}

    def print(self):

        # the following lines write the disassembly out to a file
        outFile = open(SetUp.get_output_filename() + "_dis.txt", 'w')

        for i in range(self.numInstructs + len(self.dataval)):
            outFile.write(str(self.instrSpaced[i]) +
                          '\t' +
                          str(self.address[i]) +
                          '\t' +
                          str(self.opcodeStr[i]) +
                          str(self.arg1Str[i]) +
                          str(self.arg2Str[i]) +
                          str(self.arg3Str[i]) +
                          '\n')

        outFile.close()
