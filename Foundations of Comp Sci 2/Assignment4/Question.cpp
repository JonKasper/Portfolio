// File name: Question.cpp
//
// Author: Jon-Paul Kasper
// Date: March 30, 2018
// Assignment Number: 4
// CS 2308.262
// Instructor: Yijuan Lu
//
// List of function definitions and descriptions from Question.h.

#include "Question.h"
#include <iostream>

using namespace std;

//*****************************************************************************
// void setStem: assigns a question string to the stem member variable
//
// string q: a string that contains the question to be assigned
//*****************************************************************************
void Question::setStem(string q){
   stem = q;
}

//*****************************************************************************
// void setAnswers: assigns an answer string to element i of the member array
//                  answers
//
// string a: a string that contains the answer to be assigned
// int i: an integer to select the correct element of the array
//*****************************************************************************
void Question::setAnswers(string a, int i){
   answers[i] = a;
}

//*****************************************************************************
// void setKey: assings a character to the key member variable
//
// char c: a character that contains the letter to be assigned
//*****************************************************************************
void Question::setKey(char c){
   key = c;
}

//*****************************************************************************
// string getStem: returns a string that is stored in the member variable stem
//
// returns: the string that is stored in stem
//*****************************************************************************
string Question::getStem() const{
   return stem;
}

//*****************************************************************************
// string getAnswer: returns a string that is stored in the element i of the 
//                   member array answers
//
// int j: the element of the array to be accessed
// returns: the string that is held in element i of the array answers
//*****************************************************************************
string Question::getAnswer(int j) const{
   return answers[j];
}

//*****************************************************************************
// char getKey: returns a character that is stored in the member variable key
//
// returns: the letter that is stored in key
//*****************************************************************************
char Question::getKey() const{
   return key;
}

//*****************************************************************************
// void display: calls getStem to output the question to the console as well as
//               printing the answers for that question with labels in front
//
// int max: integer that holds the number of answers to print for the question
//*****************************************************************************
void Question::display(){
   cout << getStem() << endl;
   
   for(int i = 0; i < 4; i++)
      cout << char('A' + i) << ". " << getAnswer(i) << endl;
}

//*****************************************************************************
// Question: constructor for the class if nothing is passed to the object;
//           assigns default values to the member variables stem, key, and
//           every element in answers[]
//*****************************************************************************
Question::Question(){
   stem = " ";
   key = 'X';

   for(int i = 0; i < 4; i++)
      answers[i] = " ";
}

//*****************************************************************************
// Question: constructor for the class if there is data to be assigned to the
//           object
//
// string q: contains the string to be assigned to the member variable stem
// string a[]: array containing the answers for the question stored in stem
// char c: contains the character that is the correct answer for the question
//         stored in stem
//*****************************************************************************
Question::Question(string q, string a[], char c){
   stem = q;
   key = c;

   for(int i = 0; i < 4; i++)
      answers[i] = a[i];
}
