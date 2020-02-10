# ALU
# performs the following instructions : ADD, AND, ORR, SUB, LSR, LSL, ASR, EOR, MOVZ, MOVK, ADDI, SUBI
# pre - instructions are stored in the Pre-ALU Buffer
# in - perform instructions and send out
# post - output the instruction results and update the post ALU buffer


class ALU:

    def __init__(self, sim):
        self.sim = sim

    def run(self):
        i = self.sim.preALUbuff[0]

        if i != -1:
            if self.sim.opcodeStr[i] == "ADD":  # ADD
                self.sim.postALUbuff = [self.sim.R[self.sim.arg2[i]] + self.sim.R[self.sim.arg1[i]], i]
            elif self.sim.opcodeStr[i] == "AND":  # AND
                self.sim.postALUbuff = [self.sim.R[self.sim.arg2[i]] & self.sim.R[self.sim.arg1[i]], i]
            elif self.sim.opcodeStr[i] == "ORR":  # ORR
                self.sim.postALUbuff = [self.sim.R[self.sim.arg2[i]] | self.sim.R[self.sim.arg1[i]], i]
            elif self.sim.opcodeStr[i] == "SUB":  # SUB
                self.sim.postALUbuff = [self.sim.R[self.sim.arg2[i]] - self.sim.R[self.sim.arg1[i]], i]
            elif self.sim.opcodeStr[i] == "LSR":  # LSR
                self.sim.postALUbuff = [(self.sim.R[self.sim.arg2[i]] % (1 << 32) >> self.sim.arg1[i]), i]
            elif self.sim.opcodeStr[i] == "LSL":  # LSL
                self.sim.postALUbuff = [(self.sim.R[self.sim.arg1[i]] * pow(2, self.sim.arg2[i])), i]
            elif self.sim.opcodeStr[i] == "ASR":  # ASR
                self.sim.postALUbuff = [self.sim.R[self.sim.arg1[i]] >> self.sim.R[self.sim.arg2[i]], i]
            elif self.sim.opcodeStr[i] == "EOR":  # EOR
                self.sim.postALUbuff = [self.sim.R[self.sim.arg2[i]] ^ self.sim.R[self.sim.arg1[i]], i]
            elif self.sim.opcodeStr[i] == "MOVZ":  # MOVZ
                self.sim.postALUbuff = [(self.sim.arg2[i] << self.sim.arg1[i]), i]
            elif self.sim.opcodeStr[i] == "MOVK":  # MOVK
                self.sim.postALUbuff = [(self.sim.R[self.sim.arg3[i]] | (self.sim.arg2[i] << self.sim.arg1[i])), i]
            elif self.sim.opcodeStr[i] == "ADDI":  # ADDI
                self.sim.postALUbuff = [(self.sim.R[self.sim.arg2[i]] + self.sim.arg1[i]), i]
            elif self.sim.opcodeStr[i] == "SUBI":  # SUBI
                self.sim.postALUbuff = [(self.sim.R[self.sim.arg2[i]] - self.sim.arg1[i]), i]

            self.sim.preALUbuff[0] = self.sim.preALUbuff[1]
            self.sim.preALUbuff[1] = -1
