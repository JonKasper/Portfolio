//*****************************************************************************
// File Name: IntStack.cpp
//
// Author: Jon-Paul Kasper
// Date: April 28, 2018
// Assignment Number: 6
// CS 2308.262 Spring 2018
// Instructor: Yijuan Lu
//
// Contains the function definitions for the IntStack.h header file. 
//*****************************************************************************

#include "IntStack.h"
#include <iostream>

//*****************************************************************************
// IntStack: constructor for the IntStack class. Finishes creating an empty 
//           linked list.
//*****************************************************************************
IntStack::IntStack(){
   head = NULL;
}

//*****************************************************************************
// ~IntStack: destructor for the IntStack class. Calls the pop function until 
//            the entire list is destroyed.
//*****************************************************************************
IntStack::~IntStack(){
   while(!isEmpty())
      pop();
}

//*****************************************************************************
// void push: creates a new node with the data passed to the function. Put the
//            new node at the head of the stack.
//
// int value: holds the integer value of the character that was added to the 
//            stack.
//*****************************************************************************
void IntStack::push(int value){
   if(!isFull()){
      Node * newNode = new Node;
      newNode->data = value;
      newNode->next = head;
      head = newNode;
   }
}

//*****************************************************************************
// int pop: removes the value at the top of the stack and returns its value
//
// return: returns either the value that was found in the stack or a default
//          character
//*****************************************************************************
int IntStack::pop(){
   if(!isEmpty()){
      int value = head->data;
      Node * p = head;
      head = head->next;
      delete p;

      return value;
   }
   else
      return 'X';
}

//*****************************************************************************
// bool isFull: checks to see if the stack is full
//
// return: returns a false boolean flag because the class uses a linked list
//*****************************************************************************
bool IntStack::isFull(){
   return false;
}

//*****************************************************************************
// bool isEmpty: checks to see if the stack is empty
//
// return: returns a boolean flag that signifies if the list and stack are
//         empty
//*****************************************************************************
bool IntStack::isEmpty(){
   return (head == NULL);
}
