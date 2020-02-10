// File Name: StringList.h
//
// Author: Yijuan Lu
// Assignment Number: 5
// CS 2308
// Instructor: Yijuan Lu
//
// Represents a list of strings.
// Supports adding and removing strings, displaying and sorting strings,
// finding the minimum and count of the number of strings in the list.

#include <string>
using namespace std;

class StringList
{
  private:
    struct StringNode          // the Nodes of the linked list
    {
        string data;           // data is a string
        StringNode *next;      // points to next node in list
    };

    StringNode *head;          // the head pointer

  public:
    StringList();
    ~StringList();

    int count();
    void add(string);
    bool remove(string);
    void display();
    string minimum();
    void sort();
};
