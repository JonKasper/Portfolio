import alu


class ALUtest:

    R = [0, 1, 2, 3, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    opcodeStr = ["ADD", "ADD"]
    src2Reg = [1, 2]
    src1Reg = [3, 4]
    preALUbuff = [0, 1]
    postALUbuff = [-1, -1]
    destReg = [3, 5, 6, 12, 14, 6]

    test = alu.ALU(R, opcodeStr, destReg, src2Reg, src1Reg, preALUbuff, postALUbuff)
    print("ALUTEST INSTRUCTION INDEX 0: ", str(preALUbuff[0]))
    print("ALUTEST INSTRUCTION INDEX 1: ", str(preALUbuff[1]))
    postALUbuff = test.run()
    print("ALUTEST RESULT:              ", str(postALUbuff[0]))
    print("ALUTEST INSTRUCTION INDEX 0: ", str(preALUbuff[0]))
    print("ALUTEST INSTRUCTION INDEX 1: ", str(preALUbuff[1]))
    postALUbuff = test.run()
    print("ALUTEST RESULT:              ", str(postALUbuff[0]))



