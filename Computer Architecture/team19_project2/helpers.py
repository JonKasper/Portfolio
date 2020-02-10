# helpers file. contains the functions that help break down the masks and machine code

import sys
import masking_constants as Masks


class SetUp:
    """Contains supporting functions that are mostly class based"""

    def __init__(self):
        pass

    @classmethod
    def get_input_filename(cls):
        """gets input file name from the command line and returns the name"""
        for i in range(len(sys.argv)):
            if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
                    inputFileName = sys.argv[i + 1]

        return inputFileName

    @classmethod
    def get_output_filename(cls):
        """gets output file name from the command line and returns the name"""
        for i in range(len(sys.argv)):
            if (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)):
                outputFileName = sys.argv[i + 1]

        return outputFileName

    @classmethod
    def import_data_file(cls):
        """gets filename from the command line and then downloads the input file and returns the list"""
        for i in range(len(sys.argv)):
            if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)):
                inputFileName = sys.argv[i + 1]

        try:
            instructions = [line.rstrip() for line in open(inputFileName, 'r')]
        except IOError:
            print("Could not open input file, is path correct?")

        return instructions

    @classmethod
    def imm_bit_to_32_bit_converter(cls, num, bitsize):
        """Converts binaries of various lengths to a standard 32 bit length and returns the converted number"""
        if bitsize == 19:
            extendMask = 0xFFF80000
            negBitMask = 1 << (bitsize - 1)

            if (negBitMask & num) > 0:  # is it?
                num = num | extendMask  # if so extend with 1's
                num = num ^ 0xFFFFFFFF  # 2s comp
                num = num + 1
                num = num * -1  # add neg sign
            else:
                extendMask = 0x00000000
                num = num | extendMask
            return num
        elif bitsize == 26:
            extendMask = 0x2000000
            negBitMask = 1 << (bitsize - 1)

            if (negBitMask & num) > 0:  # is it?
                num = num | extendMask  # if so extend with 1's
                num = num ^ 0xFFFFFFFF  # 2s comp
                num = num + 1
                num = num * -1  # add neg sign
            else:
                extendMask = 0x00000000
                num = num | extendMask
            return num

    @classmethod
    def immSignedToTwosConverter(cls, num):
        """Converts num to a 2s complement version"""
        numLength = (len(bin(num)))
        bitsize = numLength - 2
        negBitMask = 1 << (bitsize - 1)

        if (negBitMask & num) > 0:
            num = num ^ 0x7FFFF
            num = num + 1
            num = num * -1
            return num
        else:
            return num

    @classmethod
    def bin2StringSpaced(cls, s):
        spacedStr = s[0:8] + " " + s[8:11] + " " + s[11:16] + " " + s[16:21] + " " + s[21:26] + " " + s[26:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedD(cls, s):
        spacedStr = s[0:11] + " " + s[11:20] + " " + s[20:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedIM(cls, s):
        spacedStr = s[0:9] + " " + s[9:11] + " " + s[11:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedCB(cls, s):
        spacedStr = s[0:8] + " " + s[8:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedI(cls, s):
        spacedStr = s[0:10] + " " + s[10:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedR(cls, s):
        spacedStr = s[0:11] + " " + s[11:16] + " " + s[16:22] + " " + s[22:27] + " " + s[27:32]
        return spacedStr

    @classmethod
    def bin2StringSpacedB(cls, s):
        spacedStr = s[0:6] + " " + s[6:32]
        return spacedStr

    @classmethod
    def imm_32_bit_unsigned_to_32_bit_signed_converter(cls, num):
        """converts 32 bit signed, handles negative number, returns number"""
        num = num[0:32] & Masks.specialMask
        return num  # eventually convert this to decimal for display

    @classmethod
    def decimalToBinary(cls, num):
        """This function converts decimal number to binary and prints it"""
        if num > 1:
            cls.decimalToBinary(num // 2)
        print(num % 2, end='')

    @classmethod
    def binaryToDecimal(cls, binary):
        print("\n")
        print(int(binary, 2))
