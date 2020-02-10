# MEM
# performs the following instructions: LDUR, STUR
# pre - instructions are stored in preMEMbuff
# in - calculate the memory addresses for LDUR and STUR; check for hits and misses; check for RAW hazard during STUR
# post - write to preMEMbuff; write to postMEMbuff during LDUR only

from cache import Cache


class MEM:
    checkRes = [-1, -1]  # holds the values returned from checkCache

    def __init__(self, sim):
        self.sim = sim
        self.checkRes = [-1, -1]
        self.isRAW = False

    def run(self):
        i = self.sim.preMEMbuff[0]
        # c = Cache(self.sim.numInstructs, self.sim.instructions, self.sim.dataval, self.sim.address)

        if i != -1:
            if self.sim.opcodeStr[i] == "LDUR":  # LDUR

                dataIndex = int(((self.sim.R[self.sim.arg2[i]] + (self.sim.arg1[i] * 4)) - self.sim.address[self.sim.numInstructs - 1]) / 4)-1
                dataToWrite = -1
                # self.checkRes = Cache.checkCache(dataIndex, self.address[i], False, dataToWrite)

                self.checkRes = self.sim.cache.checkCache(dataIndex, self.sim.address[i], False, dataToWrite)

                if self.checkRes[0] != 0:
                    self.sim.postMEMbuff[0] = self.checkRes[1]
                    self.sim.postMEMbuff[1] = self.sim.address[i]
                    self.sim.preMEMbuff[0] = self.sim.preMEMbuff[1]
                    self.sim.preMEMbuff[1] = -1

            elif self.sim.opcodeStr[i] == "STUR":  # STUR

                dataIndex = int(((self.sim.R[self.sim.arg2[i]] + (self.sim.arg1[i] * 4)) - self.sim.address[self.sim.numInstructs - 1]) / 4 ) - 1
                dataToWrite = self.sim.R[self.sim.arg3[i]]
                self.checkRes = self.sim.cache.checkCache(dataIndex, self.sim.address[i], True, dataToWrite)

                if self.checkRes[0]:
                    # perform a RAW hazard check if preMEMbuff contains the same value as self.R[self.arg2[i]] (the
                    # register we are using for calculations) there is a RAW hazard same goes for preALUbuff and element
                    # 0 of postMEMbuff / postALUbuff see if there is a RAW in the preMEMbuff
                    for check in range(0, len(self.sim.preMEMbuff)):
                        if self.sim.preMEMbuff[check] != -1:
                            if self.sim.preMEMbuff[check] == self.sim.R[self.sim.arg2[i]]:
                                # found RAW in pre mem buff
                                self.isRAW = True
                                break
                    # see if there is a RAW in the preALUbuff
                    for check in range(0, len(self.sim.preALUbuff)):
                        if self.sim.preALUbuff[check] != -1:
                            if self.sim.preALUbuff[check] == self.sim.R[self.sim.arg2[i]]:
                                # found RAW in pre alu buff
                                self.isRAW = True
                                break

                    # see if there is a RAW in the post buffs too
                    if self.sim.postALUbuff[1] != -1:
                        if self.sim.postALUbuff[1] == self.sim.R[self.sim.arg2[i]]:
                            # found RAW in post ALU buff
                            self.isRAW = True
                    if self.sim.postMEMbuff[1] != -1:
                        if self.sim.postMEMbuff[1] == self.sim.R[self.sim.arg2[i]]:
                            # found RAW in post MEM buff
                            self.isRAW = True

                    # if there is no hazard
                    if self.isRAW == 0:
                        length = int(((self.sim.R[self.sim.arg2[i]] + (self.sim.arg1[i] * 4)) -
                                      self.sim.address[self.sim.numInstructs - 1]) / 4)
                        if length > (len(self.sim.dataval) - 1):
                            # append 0s to the end of dataval until the new length
                            for z in range((len(self.sim.dataval) - 1), length):
                                if z == (length - 1):
                                    # store the value in the new location
                                    self.sim.dataval[int(((self.sim.R[self.sim.arg2[i]] + (self.sim.arg1[i] * 4)) - self.sim.address[
                                                 self.sim.numInstructs - 1]) / 4) - 1] = self.sim.R[self.sim.arg3[i]]
                                else:
                                    self.sim.dataval.append(0)
                        else:
                            self.sim.dataval[int(((self.sim.R[self.sim.arg2[i]] + (self.sim.arg1[i] * 4)) - self.sim.address[
                                         self.sim.numInstructs - 1]) / 4) - 1] = self.sim.R[self.sim.arg3[i]]
                        self.sim.preMEMbuff[0] = self.sim.preMEMbuff[1]
                        self.sim.preMEMbuff[1] = -1
