from cache import Cache


class IF:

    def __init__(self, sim):
        self.sim = sim

        self.instrCheck = [-1, -1]
        self.stall = False
        self.fetch = True

    @classmethod
    def RAWcheck(cls, src1Reg, src2Reg, destReg, preALUbuff, preMEMbuff, postALUbuff, postMEMbuff,
                 preIssueBuff):
        issueMe = True
        curr = 0  # integer holding the next instruction to be looked at
        numIssued = 0

        try:
            numInPreIssueBuff = preIssueBuff.index(-1)
        except ValueError:
            numInPreIssueBuff = 4

        numInIssueAtClockCycleBegin = numInPreIssueBuff

        # check preISSbuff for each instruction and check for RAW hazards

        # RAW check - later instruction tries to read an operand before earlier instruction writes it - extremely
        # common hazard We will check each preIssueBuff entry against other preIssueBuff entries that are "leftover"
        # during processing and against preMEM and preALU. If either source of the current instruction is equal to
        # the destination of the previous instructions this is a hazard. This is like a LW issue with a stall and
        # forward so we check post buffer too

        while numIssued < 2 and numInPreIssueBuff > 0 and curr > 4:
            issueMe = True
            index = preIssueBuff[curr]

            if index == -1:
                break

            if curr > 0:
                for i in range(0, curr):
                    if src1Reg[index] == destReg[preIssueBuff[i]] or src2Reg[index] == destReg[preIssueBuff[i]]:
                        # found RAW in pre issue buff
                        issueMe = False
                        break
                # see if there is a RAW in the preMEMbuff
                for i in range(0, len(preMEMbuff)):
                    if preMEMbuff[i] != -1:
                        if src1Reg[index] == destReg[preMEMbuff[i]] or src2Reg[index] == destReg[preMEMbuff[i]]:
                            # found RAW in pre issue buff
                            issueMe = False
                            break
                # see if there is a RAW in the preALUbuff
                for i in range(0, len(preALUbuff)):
                    if preALUbuff[i] != -1:
                        if src1Reg[index] == destReg[preALUbuff[i]] or src2Reg[index] == destReg[preALUbuff[i]]:
                            # found RAW in pre issue buff
                            issueMe = False
                            break

                # see if there is a RAW in the post buffs too
                if postALUbuff[1] != -1:
                    if src1Reg[index] == destReg[postALUbuff[1]] or src2Reg[index] == destReg[postALUbuff[1]]:
                        # found RAW in post ALU buff
                        issueMe = False
                if postMEMbuff[1] != -1:
                    if src1Reg[index] == destReg[postMEMbuff[1]] or src2Reg[index] == destReg[postALUbuff[1]]:
                        # found RAW in post MEM buff
                        issueMe = False

        return issueMe

    def run(self):
            found = False
            available = 0
            fill = 0
            base = 0
            isNotRAWhaz = self.RAWcheck(self.sim.src1Reg, self.sim.src2Reg, self.sim.destReg, self.sim.preALUbuff,
                                        self.sim.preMEMbuff, self.sim.postALUbuff, self.sim.postMEMbuff,
                                        self.sim.preIssueBuff)
            # c = Cache(self.sim.numInstructs, self.sim.instructions, self.sim.dataval, self.sim.address)

            # check to see if there is room in the buffer for instructions
            for i in self.sim.preIssueBuff:
                if i == -1:
                    available += 1

            # set whether IF can fetch instructions and how many
            if self.stall and found:
                return True
            elif available == 0:
                self.fetch = False
            elif available == 1:
                self.fetch = True
                fill = 1
            elif available > 1:
                self.fetch = True
                fill = 2

            # checkCache(self, dataIndex, instructionIndex, isWriteToMem, dataToWrite)
            while self.sim.PC in self.sim.address and base < fill:
                index = (self.sim.PC - 96) / 4
                # check the cache and see if the instruction is in there
                instrCheck = self.sim.cache.checkCache(-1, int(index), False, 0)
                if instrCheck[0] != 0:
                    # handle the branch instructions that might be passed to the IF
                    # if B - don't validate and jump the PC
                    # if CBZ - validate, check if jump is within the PC range, jump the PC
                    # if CBNZ - validate, check if jump is within the PC range, jump the PC

                    # check if the instruction is a unconditional branch
                    # if unconditional update the PC by changing the value of curr to the new address value
                    if self.sim.opcodeStr[int(index)] == "B":
                        fill -= 1
                        self.sim.PC = self.sim.PC + ((self.sim.arg1[int(index)] * 4) - 4)
                        base += 1

                    # check if the instruction is branch if zero
                    # if CBZ validate the correct values and check if the branch is located in the PC
                    elif self.sim.opcodeStr[int(index)] == "CBZ":
                        fill -= 1

                        if isNotRAWhaz:
                            if self.sim.R[self.sim.arg2[int(index)]] == 0:
                                self.sim.PC = self.sim.PC + ((self.sim.arg1[int(index)] * 4) - 4)

                                if self.sim.PC not in self.sim.address:
                                    self.stall = True
                                    break

                            else:
                                self.sim.PC += 4

                            base += 1

                    # check if the instruction is branch if not zero
                    # if CBNZ validate the correct values and check if the branch is located in the PC
                    elif self.sim.opcodeStr[int(index)] == "CBNZ":
                        fill -= 1

                        if isNotRAWhaz:
                            if self.sim.R[self.sim.arg2[int(index)]] != 0:
                                self.sim.PC = self.sim.PC + ((self.sim.arg1[int(index)] * 4) - 4)

                                if self.sim.PC not in self.sim.address:
                                    self.stall = True
                                    break

                            else:
                                self.sim.PC += 4

                            base += 1

                    # check for NOP and BREAK
                    # if NOP - increment PC and continue
                    # if BREAK - increment PC and end

                    # check if the instruction is NOP
                    # if NOP increment PC and continue
                    elif self.sim.opcodeStr[int(index)] == "NOP":
                        self.sim.PC = self.sim.PC + 4
                        base += 1

                    # check if the instruction is BREAK
                    # if BREAK increment PC and end
                    elif self.sim.opcodeStr[int(index)] == "BREAK":
                        self.sim.PC = self.sim.PC + 4
                        base += 1
                        self.stall = True
                        found = True
                        return False

                    # check for all other instructions and add them to the pre issue buffer
                    else:
                        placed = False
                        i = 0
                        while i in range(0, len(self.sim.preIssueBuff)) and not found:
                            if self.sim.preIssueBuff[i] == -1:
                                self.sim.preIssueBuff[i] = int(index)
                                placed = True
                            i += 1
                        self.sim.PC += 4
                        base += 1
                else:
                    return True
