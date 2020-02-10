#makefile

a.out: QuizDriver.o Question.o
	g++ QuizDriver.o Question.o

QuizDriver.o: QuizDriver.cpp Question.h
	g++ -c QuizDriver.cpp

Question.o: Question.cpp Question.h
	g++ -c Question.cpp
