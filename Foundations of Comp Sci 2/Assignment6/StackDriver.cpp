//*****************************************************************************
// File Name: StackDriver.cpp
//
// Author: Jon-Paul Kasper
// Date: April 28, 2018
// Assignment Number: 6
// CS 2308.262 Spring 2018
// Instructor: Yijuan Lu
//
// A driver file that uses a stack to check if there are matching brackets,
// braces, or parentheses and returns error messages if there are any that are
// not matched.
// The program's error checking does not cover an open bracket, brace, or
// parenthesis if they are alone. 
//*****************************************************************************

#include "IntStack.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(){
  
   string fname = " ";
   char symbol = 'X';
   char checkSym = 'X';
   bool error = false;

   cout << "Enter the file name to be read from. Include extension > ";
   getline(cin, fname);   // get the file name from the user

   ifstream infile;
   infile.open(fname.c_str());

   // check if the file exists
   if(!infile){
      cout << "ERROR: Unable to open input file. " << endl;
      return -1;
   }

   IntStack stack;

   // loop through the entire file reading every character
   while(infile >> symbol){
      // Check if the character read is a bracket, braces, or parenthesis.
      // If an opening character is found then add its partner for comparison.
      // If a closing character is found then perform error checking to see if
      // the character belongs.
      switch(symbol){
         case '{':
            stack.push(symbol);
            stack.push('}');
            break;
         case '[':
            stack.push(symbol);
            stack.push(']');
            break;
         case '(':
            stack.push(symbol);
            stack.push(')');
            break;
         case '}':
            checkSym = stack.pop();
            switch(checkSym){
               case 'X':
                  cout << "ERROR: Unmatched '}' " << endl;
                  stack.push(checkSym);
                  error = true;
                  break;
               case '}':
                  stack.pop();
                  break;
               case ']':
                  cout << "ERROR: Expected ']' but found '}' " << endl;
                  stack.push(checkSym);
                  error = true;
                  break;
               case ')':
                  cout << "ERROR: Expected ')' but found '}' " << endl;
                  stack.push(checkSym);
                  error = true;
                  break;
            }
            break;
         case ']':
            checkSym = stack.pop();
            switch(checkSym){
               case 'X':
                  cout << "ERROR: Unmatched ']' " << endl;
                  stack.push(checkSym);
                  error = true;
                  break;
               case ']':
                  stack.pop();
                  break;
               case '}':
                  cout << "ERROR: Expected '}' but found ']' " << endl;
                  error = true;
                  break;
               case ')':
                  cout << "ERROR: Expected ')' but found ']' " << endl;
                  error = true;
                  break;
            }
            break;
         case ')':
            checkSym = stack.pop();
            switch(checkSym){
               case 'X':
                  cout << "ERROR: Unmatched ')' " << endl;
                  stack.push(checkSym);
                  error = true;
                  break;
               case ')':
                  stack.pop();
                  break;
               case '}':
                  cout << "ERROR: Expected '}' but found ')' " << endl;
                  stack.push(checkSym);
                  error = true;
                  break;
               case ']':
                  cout << "ERROR: Expected ']' but found ')' " << endl;
                  stack.push(checkSym);
                  error = true;
                  break;
            }
            break;
         default:
            break;
      }
   }

   // check to see if there are any missing closing characters.
   while(!stack.isEmpty()){
      checkSym = stack.pop();
      switch(checkSym){
         case '}':
            cout << "ERROR: Missing '}' " << endl;
            error = true;
            break;
         case ']':
            cout << "ERROR: Missing ']' " << endl;
            error = true;
            break;
         case ')':
            cout << "ERROR: Missing ')' " << endl;
            error = true;
            break;
      }
   }

   if(!error)
      cout << "No errors were found. " << endl;

   infile.close();
   return 0;
}
