// File Name: ListDriver.cpp
//
// Author: Yijuan Lu
// Assignment Number: 5
// CS 2308
// Instructor: Yijuan Lu
//
// A demo driver for StringList
//

#include <iostream>
#include <iomanip>
using namespace std;

#include "StringList.h"

int main()
{
    //testing StringList
    StringList slist;

    string movie1 = "Star Wars";
    string movie2 = "Fargo";
    string movie3 = "Back to the Future";
    string movie4 = "Titanic";

    // Testing add/display/count
    cout << "Testing add/display/count: " << endl;
    cout << "count is: " << slist.count() << endl;

    slist.add(movie1);
    slist.display();
    cout << "count is: " << slist.count() << endl;

    slist.add(movie2);
    slist.display();
    cout << "count is: " << slist.count() << endl;

    slist.add(movie3);
    slist.add(movie4);
    slist.display();
    cout << "count is: " << slist.count() << endl;

    // Testing remove
    cout << endl;
    cout << "Testing remove: " << endl;
    bool delResult;
    delResult = slist.remove(movie4);
    cout << "remove result movie4 = " << boolalpha << delResult << endl;

    delResult = slist.remove(movie3);
    cout << "remove result movie3 = " << boolalpha << delResult << endl;

    delResult = slist.remove("Not There");
    cout << "remove result Not There = " << boolalpha << delResult << endl;

    cout << "display after remove: " << endl;
    slist.display();
    cout << "count is: " << slist.count() << endl;

    // Testing minimum
    cout << endl;
    cout << "Testing minimum: " << endl;

    cout << "Testing minimum 1: " << endl;
    slist.display();
//    string min;
//    min = slist.minimum();
//    cout << "minimum: " << min << endl;
    cout << "minimum: " << boolalpha << slist.minimum() << endl;

    cout << "Test minimum 2: " << endl;
    slist.add(movie4);
    slist.display();
//    min = slist.minimum();
//    cout << "minimum: " << min << endl;
    cout << "minimum: " << boolalpha << slist.minimum() << endl;

    cout << "Test minimum 3: " << endl;
    slist.add(movie3);
    slist.display();
//    min = slist.minimum();
//    cout << "minimum: " << min << endl;
    cout << "minimum: " << boolalpha << slist.minimum() << endl;

    //Testing sort and display
    cout << endl;
    cout << "Testing sort/display: " << endl;
    slist.sort();
    slist.display();


    cout << endl;
    cout << "Testing sort/display after add: " << endl;
    slist.add("Jurassic Park");
    slist.display();
    cout << "now sorted: " << endl;
    slist.sort();
    slist.display();


}
