// File name: QuizDriver.cpp
//
// Author: Jon-Paul Kasper
// Date: March 30, 2018
// Assignment Number: 4
// CS 2308.262 Spring 2018
// Instructor: Yijuan Lu
//
// Driver for the class in Question.h and Question.cpp. Creates an array of 
// objects called question[] and assigns values to the variables stored within
// the class. 
// Outputs the question and answers for each element in the array. Outputs
// the key for each question at the end.

#include "Question.h"
#include <iostream>

using namespace std;

int main(){
   const int QUESTIONMAX = 5;
   const int ANSWERMAX = 5;

   string q1Stem = "What name is given to half of a Byte (4 bits)?";
   string q1Answers[ANSWERMAX] = {"Nibble", "Ort", "Scrap", "Snippet"};
   char q1Key = 'A';

   string q2Stem = "Which country is home to the Kangaroo?";
   string q2Answers[ANSWERMAX] = {"China", "India", "Mexico", "Australia"};
   char q2Key = 'D';

   string q3Stem = "What do you use to measure an angle?";
   string q3Answers[ANSWERMAX] = {"Compass", "Protractor", "Rule", "T-Square"};
   char q3Key = 'B';

   string q4Stem = 
      "The Great Sphinx has the head of a human and the body of a what?";
   string q4Answers[ANSWERMAX] = {"Camel", "Eagle", "Lion", "Alligator"};
   char q4Key = 'C';

   string q5Stem =
      "What is the flat rubber disc used in a game of ice hockey?";
   string q5Answers[ANSWERMAX] = {"Birdie", "Puck", "Dart", "Tile"};
   char q5Key = 'B';

   Question question[QUESTIONMAX] = {Question(q1Stem, q1Answers, q1Key),
                                     Question(q2Stem, q2Answers, q2Key),
                                     Question(q3Stem, q3Answers, q3Key),
                                     Question(q4Stem, q4Answers, q4Key),
                                     Question(q5Stem, q5Answers, q5Key)};

   for(int i = 0; i < QUESTIONMAX; i++)
   {
      cout << (i + 1) << ". ";
      question[i].display();
      cout << endl;
   }

   cout << "Answers: \n";
   for(int i = 0; i < QUESTIONMAX; i++)
      cout << question[i].getKey() << " ";

   cout << "\n\n";

   return 0;
}
