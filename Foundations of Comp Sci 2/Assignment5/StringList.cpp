// File Name: StringList.cpp
//
// Author: Jon-Paul Kasper
// Date: April 13, 2018
// Assignment Number: 5
// CS 2308.262
// Instructor: Yijuan Lu
//
// Contains the function definitions for StringList.h

#include "StringList.h"
#include <iostream>
#include <stdlib.h>
using namespace std;

//*****************************************************************************
// StringList: Constructor for the StringList class. Creates an empty list.
//*****************************************************************************
StringList :: StringList(){
   head = NULL;
}

//*****************************************************************************
// ~StringList: Deconstructor for the StringList class. Loops through the list
//              and deletes the dynamically allocated memory.
//*****************************************************************************
StringList :: ~StringList(){
   StringNode *p = head;
   StringNode *n = head;

   if(p != NULL)
   {
      while(p != NULL)
      {
         n = p->next;
         delete p;
         p = n;
      }
   }
}

//*****************************************************************************
// int count: Counts the number of nodes in the linked list and returns the 
//            number
// returns: returns the number of nodes in the list as an integer
//*****************************************************************************
int StringList :: count(){
   int count = 0;
   StringNode *p = head;

   while(p != NULL)
   {
      p = p->next;
      count++;
   }
   
   return count;
}

//*****************************************************************************
// void add: Dynamically allocates memory to create a new node in the linked
//           list
//
// string movie: A string that is passed to the function to be used as data in
//               the node
//*****************************************************************************
void StringList :: add(string movie){
   StringNode *p = new StringNode;
   p->data = movie;
   p->next = head;
   head = p;
}

//*****************************************************************************
// bool remove: Removes a node from the linked list and frees up the memory 
//              that was held for the node.
//
// string movie: The string that should be found and removed from the list
// returns: A true value if the string was found and a false value if it was
//          not
//*****************************************************************************
bool StringList :: remove(string movie){
   StringNode *p = head;
   StringNode *n;

   if(p == NULL)          // check if the list is empty
      return false;
   else
   {
      // loop through the list until the end or until the data is found
      while((p != NULL) && (p->data != movie))
      {
         n = p;
         p = p->next;
      }

      if(p != NULL)       // check to see if the data was found
      {
         if(p == head)    // if the data is at the head
         {
            head = p->next;
            delete p;
         }
         else             // if the data is in the middle or at the end
         {
            n->next = p->next;
            delete p;
         }

         return true;
      }
      else
         return false;
   }
}

//*****************************************************************************
// void display: Loops through the list and diplays the data in each node
//*****************************************************************************
void StringList :: display(){
   StringNode *p = head;
   
   if(p == NULL)           // check if the list is empty
      cout << "The list is empty." << endl;
   else
   {
      while(p != NULL)
      {
         cout << p->data << endl;
         p = p->next;
      }
   }
}

//*****************************************************************************
// string minimum: Loops through the list and finds the movie that is 
//                 alphabetically first.
//
// returns: The movie that is alphabetically first out of the list
//*****************************************************************************
string StringList :: minimum(){
   StringNode *p = head;
   string min = "NULL";
   
   if(p == NULL)           // check if the list is empty
      return min;
   else
   {  
      min = p->data;
      while(p != NULL)
      {
         if(p->data < min)
            min = p->data;
         p = p->next;
      }
      return min;
   }
}

//*****************************************************************************
// void sort: Creates a new linked list that is comprised of the data from the
//            original list but has been sorted in alphabetical order. After 
//            the new list is full the head from the old list is assigned to 
//            the new list.
//*****************************************************************************
void StringList :: sort(){
   StringNode *newHead = NULL;   // create a new empty list
   string minData = "NULL";      // create a temp variable to hold the data

   while(head != NULL)
   {
      minData = minimum();       // get the minimum string from the list
      if(minData == "NULL")      // check if the old list was empty
         cout << "The old list was empty." << endl;
      
      remove(minData);   
      
      // add minData to the new list
      if(newHead == NULL)        // check if the new list is empty
      {
         StringNode *newN = new StringNode;
         newN->data = minData;
         newN->next = NULL;
         newHead = newN;
      }
      else
      {
         StringNode *newN = new StringNode;
         newN->data = minData;
         newN->next = NULL;
         StringNode *p = newHead;

         while(p->next != NULL)
            p = p->next;

         p->next = newN;
      }
   }
   head = newHead;              // collapse the two lists
}
