// File Name: assign3_jk1457.cpp
//
// Author: Jon-Paul Kasper
// Date: 03/02/2018
// Assignment Number: 3
// CS 2308.262
// Instructor: Yijuan Lu
//
// Runs and tests functions that pass pointers as parameters and arguments as
// as well as testing dynamic memory allocation. Testing is done through
// constant test data that is hard coded into the program.
// Output will include the function name being tested, the data being tested,
// the expected result after the data is tested, and the actual result from
// the function being tested with labels as needed.

#include <iostream>

using namespace std;

bool isSorted(int *, int);
double chain(int, int *, int *);
int *grow(int *, int);
int *duplicateArray(int *, int);
int *subArray(int *, int, int);

int main()
{
    const int SIZE = 10;

    int sortedArray[SIZE] = {1,2,3,4,5,6,7,8,9,10};
    int unsortedArray[SIZE] = {1,5,7,4,8,2,9,3,6,10};
    int partialSortArray[SIZE] = {1,2,3,4,6,5,7,8,9,10};

    const int totalInches = 67;
    const int start = 3;
    const int length = 5;

    bool sortResult = true;
    string trueOrFalse = " ";
    double chainResult = 0.0;
    int feet = 0, inches = 0, newSize = SIZE * 2;

    int *arrPtr = sortedArray;
    int *fPtr = &feet;
    int *iPtr = &inches;

    cout << "\nTesting isSorted: \nTest Data Array 1: 1 2 3 4 5 6 7 8 9 10\n"
         << "Expected Result: true\n";

    sortResult = isSorted(arrPtr, SIZE);
    if(sortResult == true)
        trueOrFalse = "true";
    else
        trueOrFalse = "false";
    cout << "Actual Result: " << trueOrFalse << "\n\n";
    
    arrPtr = unsortedArray;
    cout << "Testing isSorted: \nTest Data Array 2: 1 5 7 4 8 2 9 3 6 10\n"
         << "Expected Result: false\n";

    sortResult = isSorted(arrPtr, SIZE);
    if(sortResult == true)
        trueOrFalse = "true";
    else
        trueOrFalse = "false";
    cout << "Actual Result: " << trueOrFalse << "\n\n";

    arrPtr = partialSortArray;
    cout << "Testing isSorted: \nTest Data Array 3: 1 2 3 4 6 5 7 8 9 10\n"
         << "Expected Result: false\n";

    sortResult = isSorted(arrPtr, SIZE);
    if(sortResult == true)
        trueOrFalse = "true";
    else
        trueOrFalse = "false";
    cout << "Actual Result: " << trueOrFalse << "\n\n\n";

    
    cout << "Testing chain for 67 inches: \n"
         << "Expected Result: 19.55 feet: 5 inches: 7\n";

    chainResult = chain(totalInches, fPtr, iPtr);
    cout << "Actual Result: " << chainResult << " feet: " << feet
         << " inches: " << inches << "\n\n\n";


    arrPtr = sortedArray;
    cout << "Testing grow:\nTest Data: 1 2 3 4 5 6 7 8 9 10\n"
         << "Expected Result: 1 1 2 2 3 3 4 4 5 5 6 6 7 7 8 8 9 9 10 10\n"
         << "Actual Result: ";

    int *tempPtr = grow(arrPtr, SIZE);
    for(int i = 0; i < newSize; i++)
        cout << *(tempPtr + i) << " ";
    delete [] tempPtr;

    cout << "\n\n\n";


    cout << "Testing subArray:\nTest Data: 1 2 3 4 5 6 7 8 9 10\n"
         << "Start: 3 Length: 5\nExpected Result: 4 5 6 7 8\nActual Result: ";

    tempPtr = subArray(arrPtr, start, length);
    for(int i = 0; i < length; i++)
        cout << *(tempPtr + i) << " ";
    delete [] tempPtr;

    cout << "\n\n\n";

    return 0;
}

//*****************************************************************************
// bool isSorted: checks if the array that is passed to it is sorted or not
//
// int *arrayPtr: an integer pointer that holds the address location of the 
//                array that it points to
// int size: an integer that holds the value of the constant SIZE
// returns: returns a boolean value of false if not sorted and true if sorted
//*****************************************************************************

bool isSorted(int *arrayPtr, int size)
{
    bool sorted = true;
 
    for(int i = 0; i < (size - 1); i++)
    {
        if(*(arrayPtr + i) > (*(arrayPtr + (i + 1))))
            sorted = false;
        if(sorted == false)
            break;
    }

    return sorted;
}

//*****************************************************************************
// double chain: calculates the feet and left over inches from a specific number
//               of inches
//
// int totalInches: an integer that holds the number of inches that are used in
//                  the calculations in the function
// int *feetPtr: an integer pointer that points to the location of the feet
//               variable
// int *inchPtr: an integer pointer that points to the location of the inches
//               variable
// returns: returns an expression whose value is a double
//*****************************************************************************

double chain(int totalInches, int *feetPtr, int *inchPtr)
{
    *feetPtr = totalInches / 12;
    *inchPtr = totalInches % 12; 

    return ((*feetPtr * 3.49) + (*inchPtr * 0.30));
}

//*****************************************************************************
// int *grow: doubles the length of an array and copies the contents of the 
//            passed array such that every element of the array occurs twice in
//            the new array
//
// int *array: an integer pointer that holds the address location of the array
//             that it points to
// int size: an integer that holds the value of the constant SIZE
// returns: returns a pointer that is pointing to a dynamic array that holds
//          the new array and its elements
//*****************************************************************************

int *grow(int *array, int size)
{
    int newSize = size * 2;
    int *tempPtr = new int[newSize];

    for(int i = 0; i < size; i++)
    {
        if(i == 0)
        {
            *(tempPtr + i) = *(array + i);
            *(tempPtr + (i + 1)) = *(array + i);
        }
        else
        {
            *(tempPtr + (i * 2)) = *(array + i);
            *(tempPtr + ((i * 2) + 1)) = *(array + i);
        }
    }
    
    return tempPtr;
}

//*****************************************************************************
// int *duplicateArray: creates a new array of a specified size which contains
//                      part of the elements of the array passed to the 
//                      function
//
// int *arr: an integer pointer that holds the address location of the array
//           that it points to
// int size: an integer that holds the size of the new array that will be 
//           created
// returns: returns a pointer that points to the memory location of the newly
//          created array
//*****************************************************************************

int *duplicateArray(int *arr, int size)
{
    int *newArray;
    if(size <= 0)
        return NULL;

    newArray = new int[size];

    for(int index = 0; index < size; index++)
        newArray[index] = arr[index];

    return newArray;
}

//*****************************************************************************
// int *subArray: creates a new array that is a copy of the elements of an 
//                array starting at the start index and has a length equal to 
//                that of the length argument
//
// int *array: an integer pointer that points to the array that was passed to
//             the function
// int start: an integer that holds the value of the start location
// int length: an integer that holds the value of the length of the new array
// returns: returns a pointer that points to the location in the memory of the
//          newly created array.
//*****************************************************************************

int *subArray(int *array, int start, int length)
{
    int *result = duplicateArray((array + start), length);
    return result;
}
