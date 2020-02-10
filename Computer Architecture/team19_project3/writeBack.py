
class WriteBack:

    def __init__(self, sim):
        self.sim = sim

    def run(self):
        if self.sim.postMEMbuff[1] != -1:
            self.sim.R[self.sim.destReg[self.sim.postMEMbuff[1]]] = self.sim.postMEMbuff[0]
            self.sim.postMEMbuff[0] = -1
            self.sim.postMEMbuff[1] = -1

        if self.sim.postALUbuff[1] != -1:
            self.sim.R[self.sim.destReg[self.sim.postALUbuff[1]]] = self.sim.postALUbuff[0]
            self.sim.postALUbuff[0] = -1
            self.sim.postALUbuff[1] = -1
