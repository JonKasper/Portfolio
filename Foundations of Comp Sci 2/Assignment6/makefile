#makefile

a.out: StackDriver.o IntStack.o
	g++ StackDriver.o IntStack.o

StackDriver.o: StackDriver.cpp IntStack.h
	g++ -c StackDriver.cpp

IntStack.o: IntStack.cpp IntStack.h
	g++ -c IntStack.cpp
