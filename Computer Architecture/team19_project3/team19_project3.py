import disassembler
import simulator

mydis = disassembler.Disassembler()

output = mydis.run()
mydis.print()

mysim = simulator.Simulator(**output)
mysim.run()
