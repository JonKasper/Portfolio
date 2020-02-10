// File name: Question.h
//
// Author: Jon-Paul Kasper
// Date: March 30, 2018
// Assignment Number: 4
// CS 2308.262
// Instructor: Yijuan Lu
//
// Header file containting the class Question. Used in QuizDriver.cpp to 
// create a quiz. Class contains private data and public member functions.

#include <string>

using namespace std;

class Question{
   private:
      string stem;
      string answers[4];
      char key;
   public:
      void setStem(string);
      void setAnswers(string, int);
      void setKey(char);
      void display();
      string getStem() const; // ensure no data is altered
      string getAnswer(int) const; // ensure no data is altered
      char getKey() const; // ensure no data is altered
      Question();
      Question(string, string [], char);
};
