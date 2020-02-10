# File used to test mem.py

import mem

from cache import Cache


class MEMtest:
    R = [0, 1, 2, 104, 4, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    opcodeStr = ["STUR", "LDUR"]
    destReg = [4, -5]
    dataval = [0, 1, 2, 3, 4, 5, 6, 7]
    Src1Reg = [3, 3]
    Src2Reg = [0, 0]
    address = [96, 100, 104, 108, 112]
    numInstructs = 2
    preALUbuff = [-1, -1]
    postALUbuff = [-1, -1]
    preMEMbuff = [0, 1]
    postMEMbuff = [-1, -1]
    instructions = [11111000010000000001000010000001, 11111000000000000001000010000010]
    c = Cache(numInstructs, instructions, dataval, address)

    test = mem.MEM(c, R, opcodeStr, destReg, dataval, Src1Reg, Src2Reg, address, numInstructs, preALUbuff, postALUbuff, preMEMbuff,
                   postMEMbuff, instructions)
    print("MEMTEST INSTRUCTION INDEX 0: ", str(preMEMbuff[0]))
    print("MEMTEST INSTRUCTION INDEX 1: ", str(preMEMbuff[1]))
    test.run()
    print("MEMTEST RESULT:              ", str(postMEMbuff[1]))
    print("MEMTEST INSTRUCTION INDEX 0: ", str(preMEMbuff[0]))
    print("MEMTEST INSTRUCTION INDEX 1: ", str(preMEMbuff[1]))
    test.run()
    print("MEMTEST RESULT:              ", str(postMEMbuff[1]))
    print("MEMTEST INSTRUCTION INDEX 0: ", str(preMEMbuff[0]))
    print("MEMTEST INSTRUCTION INDEX 1: ", str(preMEMbuff[1]))
    test.run()
    print("MEMTEST RESULT:              ", str(postMEMbuff[1]))
