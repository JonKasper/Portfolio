import issue


class ISSUE:
    preIssueBuff = [1, 2, -1, -1]
    preMEMbuff = [-1, -1]
    postMEMbuff = [-1, -1]
    preALUbuff = [-1, -1]
    postALUbuff = [-1, -1]
    src1Reg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    src2Reg = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    destReg = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
    opcodeStr = [10010001000000000001000000100001, 10010001000000000001010001000010, 10001011000001000000000010100011,
                 11001011000001110000000110000100, 10001010000000100000000000100101, 10101010000000100000000001000110,
                 11101010000000100000000000100111, 11111110110111101111111111100111]

    test = issue.ISSUE(preIssueBuff, preMEMbuff, postMEMbuff, preALUbuff, postALUbuff, src1Reg, src2Reg, destReg, opcodeStr)

    print("ISSUETEST pre MEM INSTRUCTION INDEX 0: ", str(preMEMbuff[0]))
    print("ISSUETEST pre MEM INSTRUCTION INDEX 1: ", str(preMEMbuff[1]))
    print("preALUbuff[0]: ", str(preALUbuff[0]))
    print("preALUbuff[1]: ", str(preALUbuff[1]))
    test.run()
    print("ISSUETEST pre MEM INSTRUCTION INDEX 0: ", str(preMEMbuff[0]))
    print("ISSUETEST pre MEM INSTRUCTION INDEX 1: ", str(preMEMbuff[1]))
    print("preALUbuff[0]: ", str(preALUbuff[0]))
    print("preALUbuff[1]: ", str(preALUbuff[1]))
    test.run()
    print("ISSUETEST pre MEM INSTRUCTION INDEX 0: ", str(preMEMbuff[0]))
    print("ISSUETEST pre MEM INSTRUCTION INDEX 1: ", str(preMEMbuff[1]))
    print("preALUbuff[0]: ", str(preALUbuff[0]))
    print("preALUbuff[1]: ", str(preALUbuff[1]))
    test.run()
