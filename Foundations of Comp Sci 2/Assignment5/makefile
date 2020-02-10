#makefile

a.out: ListDriver.o StringList.o
	g++ ListDriver.o StringList.o

ListDriver.o: ListDriver.cpp StringList.h
	g++ -c ListDriver.cpp

StringList.o: StringList.cpp StringList.h
	g++ -c StringList.cpp
