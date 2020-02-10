# ISSUE
# Gets instructions from the pre issue buffer in order of oldest to newest and checks for hazards
# pre - instruction list stored in preIssueBuff
# in - compare the entries in preIssueBuff and check for hazards
# post - update the preMEMbuff and preALUbuff dependent on the instructions

from helpers import SetUp


class ISSUE:

    def __init__(self, sim):
        self.sim = sim

    def run(self):
        curr = 0  # integer holding the next instruction to be looked at
        numIssued = 0

        try:
            numInPreIssueBuff = self.sim.preIssueBuff.index(-1)
        except ValueError:
            numInPreIssueBuff = 4

        numInIssueAtClockCycleBegin = numInPreIssueBuff

        # check preISSbuff for each instruction and check for RAW hazards

        # RAW check - later instruction tries to read an operand before earlier instruction writes it - extremely
        # common hazard We will check each preIssueBuff entry against other preIssueBuff entries that are "leftover"
        # during processing and against preMEM and preALU. If either source of the current instruction is equal to
        # the destination of the previous instructions this is a hazard. This is like a LW issue with a stall and
        # forward so we check post buffer too

        while numIssued < 2 and numInPreIssueBuff > 0 and curr < 4:
            issueMe = True
            index = self.sim.preIssueBuff[curr]

            if index == -1:
                break

            if curr > 0:
                for i in range(0, curr):
                    if self.sim.src1Reg[index] == self.sim.destReg[self.sim.preIssueBuff[i]] or self.sim.src2Reg[
                        index] == self.sim.destReg[self.sim.preIssueBuff[i]]:
                        # found RAW in pre issue buff
                        issueMe = False
                        break
                # see if there is a RAW in the preMEMbuff
                for i in range(0, len(self.sim.preMEMbuff)):
                    if self.sim.preMEMbuff[i] != -1:
                        if self.sim.src1Reg[index] == self.sim.destReg[self.sim.preMEMbuff[i]] or self.sim.src2Reg[
                            index] == \
                                self.sim.destReg[self.sim.preMEMbuff[i]]:
                            # found RAW in pre issue buff
                            issueMe = False
                            break
                # see if there is a RAW in the preALUbuff
                for i in range(0, len(self.sim.preALUbuff)):
                    if self.sim.preALUbuff[i] != -1:
                        if self.sim.src1Reg[index] == self.sim.destReg[self.sim.preALUbuff[i]] or self.sim.src2Reg[
                            index] == \
                                self.sim.destReg[self.sim.preALUbuff[i]]:
                            # found RAW in pre issue buff
                            issueMe = False
                            break

                # see if there is a RAW in the post buffs too
                if self.sim.postALUbuff[1] != -1:
                    if self.sim.src1Reg[index] == self.sim.destReg[self.sim.postALUbuff[1]] or self.sim.src2Reg[
                        index] == self.sim.destReg[self.sim.postALUbuff[1]]:
                        # found RAW in post ALU buff
                        issueMe = False
                if self.sim.postMEMbuff[1] != -1:
                    if self.sim.src1Reg[index] == self.sim.destReg[self.sim.postMEMbuff[1]] or self.sim.src2Reg[
                        index] == self.sim.destReg[self.sim.postALUbuff[1]]:
                        # found RAW in post MEM buff
                        issueMe = False

            if issueMe:
                numIssued += 1
                # copy the instruction to the appropriate buffer
                # the assumption here is that we will have a -1 in the right spot! Think we will.
                if SetUp.isMemOp(index, self.sim.opcodeStr):
                    self.sim.preMEMbuff[self.sim.preMEMbuff.index(-1)] = index
                else:
                    self.sim.preALUbuff[self.sim.preALUbuff.index(-1)] = index

                # move the instr in the pre issue buff down one level
                self.sim.preIssueBuff[0:curr] = self.sim.preIssueBuff[0:curr]
                # print"pre" + str(self.preIssueBuff[curr+1])
                self.sim.preIssueBuff[curr:3] = self.sim.preIssueBuff[
                                                curr + 1:]  # dropped 4, think will go to end always
                self.sim.preIssueBuff[3] = -1
                numInPreIssueBuff -= 1

            curr += 1
