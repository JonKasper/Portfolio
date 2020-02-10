import dissasembler
import simulator

mydis = dissasembler.Disassembler()

output = {}
output = mydis.run()
mydis.print()

mysim = simulator.Simulator(**output)
mysim.run()
