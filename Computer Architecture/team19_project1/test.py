from helpers import SetUp


instructions = [10110100111111111111111110110011]
instrSpaced = []
opcode = []
opcodeStr = []
arg1 = []
arg2 = []
arg3 = []
arg1Str = []
arg2Str = []
arg3Str = []
bMask = 0x3FFFFFF
jAddrMask = 0xFC000000
specialMask = 0x1FFFFF
rnMask = 0x3E0  # 1st argument  ARM Rn
rmMask = 0x1F0000  # second argument  ARM Rm
rdMask = 0x1f  # destination  ARM rd
imMask = 0x3FFC00  # ARM I Immediate
shmtMask = 0xFC00  # ARM ShAMT
addrMask = 0x1FF000  # ARM address for ld and st
addr2Mask = 0xFFFFE0  # addr for CB format
imsftMask = 0x600000  # shift for IM format
imdataMask = 0x1FFFE0  # data for IM type
'''
instrSpaced.append(SetUp.bin2StringSpacedCB(str(instructions[0])))
opcodeStr.append("CBZ")
arg1.append((int(str(instructions[0]), base=2) & rdMask) >> 0)
arg2.append((int(str(instructions[0]), base=2) & addr2Mask) >> 5)
arg3.append(0)
arg1Str.append("\tR" + str(arg1[0]))
arg2Str.append(", #" + str(arg2[0]))

print(instrSpaced)
print("testing opcodeStr: " + opcodeStr[0])
print("testing 1: " + str(arg1[0]))
print("testing 2: " + str(arg2[0]))
print("testing 3: " + str(arg3[0]))
print("testing string 1: " + arg1Str[0])
print("testing string 2: " + arg2Str[0])

print("Alternate tests")
print((arg2[0] ^ 0x7FFFF) + 1)
print(bin((arg2[0] ^ 0x7FFFF) + 1))

num = int(arg2[0])
print("testing binary num: ")
print(bin(num))
print("testing non binary num: ")
print(num)
bitsize = len(bin(num)) - 2
num = SetUp.imm_bit_to_32_bit_converter(num, bitsize)
print("num after 32 bit converter: " + str(bin(num)))
num = num ^ 0xFFFFFFFF
print("num after XOR: " + str(bin(num)))
num = num + 1
print("num after 2s: " + str(bin(num)))
print(num)


num = 524285
numAsBin = bin(num)
print("testing numAsBin value: " + str(numAsBin))
numLength = len(numAsBin)
print("testing numLength: " + str(numLength))
print(str(numAsBin[0]))
numAsBin = numAsBin[2:numLength]
print("testing new numAsBin value: " + str(numAsBin))
num = int(numAsBin, base=2)
print("testing num value after conversion: " + str(num))
print(str(numAsBin[0]))

num = 524285
bitsize = 19
if bitsize == 19:
    extendMask = 0xFFF80000
    negBitMask = 1 << (bitsize - 1)
    print("negBitMask if: " + str(negBitMask))
    if (negBitMask & num) > 0:  # is it?
        num = num | extendMask  # if so extend with 1's
        print("num1: " + str(num))
        num = num ^ 0xFFFFFFFF  # 2s comp
        print("num2: " + str(num))
        num = num + 1
        print("num3: " + str(num))
        num = num * -1  # add neg sign
        print("num4: " + str(num))
    else:
        extendMask = 0x00000000
        num = num | extendMask
        print("num4: " + str(num))
    print(num)
elif bitsize == 26:
    extendMask = 0x2000000
    negBitMask = 1 << (bitsize - 1)
    print("negBitMask else: " + str(negBitMask))
    if (negBitMask & num) > 0:  # is it?
        num = num | extendMask  # if so extend with 1's
        print("num1: " + str(num))
        num = num ^ 0xFFFFFFFF  # 2s comp
        print("num2: " + str(num))
        num = num + 1
        print("num3: " + str(num))
        num = num * -1  # add neg sign
        print("num4: " + str(num))
    else:
        extendMask = 0x00000000
        num = num | extendMask
        print("num4: " + str(num))
    print(num)


num = -32
numLength = len(bin(num)) - 2
print("numLength: " + str(numLength))
negBitMask = 1 << (numLength - 1)
print("negBitMask: " + str(negBitMask))
print("negBitMask & num: " + str(negBitMask & num))
if (negBitMask & num) > 0:
    mask = 1
    for i in range(numLength - 1):
        mask = (mask << 1) + 1
    num = num ^ mask
    num = num + 1
print("testing num value: ")
print(str(num))'''

num = -51
if num < 0:
    numLength = len(bin(num))
    print("numLength: " + str(numLength))
    numAsBinary = bin(num)
    print("numAsBinary1: " + numAsBinary)
    numAsBinary = numAsBinary[3:numLength]
    print("numAsBinary2: " + str(numAsBinary))
    signBit = 1 << (numLength - 3)
    print("signBit: " + str(signBit) + " " + bin(signBit))
    numAsBinary = int(numAsBinary, base=2) | signBit
    print("numAsBinary after signBit: " + str(numAsBinary) + " " + bin(numAsBinary))
    extendMask = 1
    for i in range(numLength - 3):
        extendMask = (extendMask << 1) + 1
    print("extend mask: " + str(extendMask) + " " + bin(extendMask))
    numAsBinary = numAsBinary ^ extendMask
    print("numAsBinary3: " + str(numAsBinary) + " " + bin(numAsBinary))
    numAsBinary += 1
    print("numAsBinary4: " + str(numAsBinary) + " " + bin(numAsBinary))
    print("in if num: " + str(numAsBinary) + " " + bin(numAsBinary))
else:
    print(num)
