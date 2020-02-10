import writeBack


class WBtest:

    R = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    postALUBuff = [5, 4]
    postMemBuff = [6, 5]
    destReg = [3, 5, 6, 12, 14, 6]

    test = writeBack.WriteBack(R, postMemBuff, postALUBuff, destReg)
    test.run()

    print(R[6])
