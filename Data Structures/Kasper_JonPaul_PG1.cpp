//  Author: Jon-Paul Kasper
//  Roster Number: 34
//  Due Date: September 10, 2018
//  Programming Assignment Number 
//  Fall 2018 - CS 3358 - 002
//  
//  Instructor: Husain Gholoom
//  
//  This program takes a user inputed number to set the size of a two 
//  dimensional array. The array is then populated with random numbers from
//  1 - 100. The numbers are then tested mathematically to see if the randomly
//  generated arrays form a magic square. The program then repeats itself 
//  until the user terminates it.

#include <iostream>
#include <ctime>   // included for the random number generator
#include <cstdlib>   // included for the random number generator
#include <iomanip>
#include <cmath>   // included for the pow() function

const int SIZE = 10;
const int MAX = 100;
const int MIN = 1;

void printMenu();
bool isValid(int);
void populateSquare(int [][SIZE] , int);
bool randomExists(int [][SIZE], int, int);
void displaySquare(int [][SIZE], int);
bool calcMagicNumber(int [][SIZE], int);
bool testMagic(int, int);

using namespace std;

int main(){

  int base = 2;   // variable to be used to read in the size of the square
  int magicSquare[SIZE][SIZE] = {};
  bool test = true;   // variable for testing if the square is a magic square
  char ans = 'x';   // used as a limiter for exiting or continuing the program
  
  srand (time(NULL));   // seed for the random number generator

  printMenu();
  
  // loop through the program until the user wishes to quit
  do{
    cout << "Enter the size of the magic square: ";
    cin >> base;
    cout << "\n\n";
  
    // check if the user input is within the bounds required by the program
    while(!isValid(base)){
      cout << "ERROR: Invalid input. Please input a value >= 2 or <= 10 : ";
      cin >> base;
      cout << "\n\n";
    }
  
    populateSquare(magicSquare, base);   // populate the magic square
    displaySquare(magicSquare,base);   // display the magic square
    test = calcMagicNumber(magicSquare, base);   // calculate the row, column, 
                                                 // and diagonal values

    // determine if the square that was created is a magic square
    if (test == true)
      cout << "\nThe above is a magic square.\n\n";
    else
      cout << "\nThe above is not a magic square.\n\n";

    // give the user the option to quit the program
    cout << "Would you like to find another magic square? ( y | Y for yes, "
         << "n | N for no) : ";
    cin >> ans;

    // ensure the user enters the right values for a choice
    while (ans != 'n' && ans != 'N' && ans != 'y' && ans != 'Y'){
      cout << "ERROR: Invalid choice! Please choose n, N, y, or Y : ";
      cin >> ans;
    }

  }while (ans != 'n' && ans != 'N');

  cout << "This magic square algorithm is implemented by Jon-Paul Kasper.\n\n";
  
  return 0;

}

//*****************************************************************************
// Presents the menu and description of the program for the user.
//
// No parameters.
// No return.
//*****************************************************************************
void printMenu(){

  cout << "Welcome to my magic sequence program. The function of the program "
       << "is to\n\n"
       << "\t1. Allow the user to enter the size of the magic square such as "
       << "N. \n\t   N >= 2 and <= 10.\n"
       << "\t2. Create an array of size N x N.\n"
       << "\t3. Populate the array with distinct random numbers.\n"
       << "\t4. Display the sum for each row, column, and diagonals then "
       << "determine \n\t   whether the numbers in N x N array are magic "
       << "square numbers. \n\n";

}

//*****************************************************************************
// Tests if the user entered number is within the bounds the program allows.
// 
// Parameter 1: int base
//            - A user entered value that is tested by the function.
// Returns: boolean true or false
//        - A flag for use in a test loop in main()
//***************************************************************************** 
bool isValid(int base){
  if(base >= 2 && base <= 10)
    return true;
  else
    return false;
}

//*****************************************************************************
// Populates a two dimensional array with random numbers from 1 - 100. Ensures
// no numbers a duplicated.
// 
// Parameter 1: int magicSquare[][]
//            - A two dimensional array that holds integers for use throughout
//              the program.
// Parameter 2: int base
//            - A user entered value that is tested by the function.
// No returns.
//*****************************************************************************
void populateSquare(int magicSquare[SIZE][SIZE], int base){
  
  int temp = 0;

  for (int i = 0; i < base; i++){
    for (int j = 0; j < base; j++){
      temp = (rand() % MAX) + MIN;
      
      // test if the number already exists in the two dimensional array
      while(randomExists(magicSquare, base, temp)){
        temp = (rand() % MAX) + MIN;
      }

      magicSquare[i][j] = temp;
    }
  }
}

//*****************************************************************************
// Tests a number that was generated against the two dimensional array to see 
// if the number already exists. 
//
// Parameter 1: int magicSquare[][]
//            - A two dimensional array that holds integers for use throughout
//              the program.
// Parameter 2: int base
//            - A user entered value that is used for looping in the function
// Parameter 3: int temp
//            - An integer that is used to test if a number exists inside the
//              two dimensional array
// Returns: boolean true or false
//*****************************************************************************
bool randomExists(int magicSquare[SIZE][SIZE], int base, int temp){
  
  for (int i = 0; i < base; i++){
    for (int j = 0; j < base; j++){
      if (magicSquare[i][j] == temp)
        return true;
    }
  }

  return false;
}

//*****************************************************************************
// Displays the contents of the magic square.
// 
// Parameter 1: int magicSquare[][]
//            - A two dimensional array that holds integers for use throughout
//              the program.
// Parameter 2: int base
//            - A user entered value that is used for looping in the function
// No returns.
//*****************************************************************************
void displaySquare(int magicSquare[SIZE][SIZE], int base){
  
  cout << "The magic sequence that is created for the size " << base << ":\n\n";

  for (int i = 0; i < base; i++){
    for (int j = 0; j < base; j++){
      cout << setw(5) << left << magicSquare[i][j] << "\t";
    } 
    cout << "\n";
  }
  cout << "\n";
}

//*****************************************************************************
// Calculates the magic number based off of the input from the user. Calculates
// the added total for each row, column, and the two cross diagonals. Compares
// the values for each total to each other to determine if the square is magic.
// 
// Parameter 1: int magicSquare[][]
//            - A two dimensional array that holds integers for use throughout
//              the program.
// Parameter 2: int base
//            - A user entered value that is used for looping in the function
// Returns: boolean true or false
//*****************************************************************************
bool calcMagicNumber(int magicSquare[SIZE][SIZE], int base){
  
  bool isMagic = true;
  int rowTotal = 0;
  int columnTotal = 0;
  int diagonal_1 = 0;
  int diagonal_2 = 0;
  
  // calculates the magic number for comparison
  int magicNumber = (base * (pow(base,2) + 1)) / 2;
  cout << "The magic number is: " << magicNumber << "\n\n";

  // calculate the total for each row  
  for (int i = 0; i < base; i++){
    for (int j = 0; j < base; j++){
      rowTotal += magicSquare[i][j];
    }
    
    cout << "Sum of numbers in Row" << setw(7) << right << "#" << setw(4)
         << (i + 1) << setw(8) << "=" << setw(5) << rowTotal << "\n";
    
    // test if the row total is equivalent to the magic number        
    isMagic = testMagic(rowTotal, magicNumber);
    rowTotal = 0;
  }

  // calculate the total for each column
  for (int j = 0; j < base; j++){
    for (int i = 0; i < base; i++){
      columnTotal += magicSquare[i][j];
    }

    cout << "Sum of numbers in Column" << setw(4) << right << "#" << setw(4)
         << (j + 1) << setw(8) << "=" << setw(5) << columnTotal << "\n";
    
    // test if the column total is equivalent to the magic number
    isMagic = testMagic(columnTotal, magicNumber);
    columnTotal = 0;
  }

  // calculate the total of the first diagonal
  for (int i = 0; i < base; i++){
    diagonal_1 += magicSquare[i][i];
  }

  cout << "Sum of numbers in first diagonal" << setw(8) << "=" << setw(5)
       << diagonal_1 << "\n";
  // test if the diagonal total is equivalent to the magic number
  isMagic = testMagic(diagonal_1, magicNumber); 
  
  // calculate the total of the second diagonal
  int i = 0;
  for (int j = (base - 1); j >= 0; j--){
    diagonal_2 += magicSquare[i][j];
    i++;
  }
  
  cout << "Sum of numbers in second diagonal" << setw(7) << "=" << setw(5)
       << diagonal_2 << "\n";
  // test if the diagonal total is equivalent to the magic number
  isMagic = testMagic(diagonal_2, magicNumber);

  return isMagic;
}

//*****************************************************************************
// Compares the totals passed to the function to the magic number.
//
// Parameter 1: int total
//            - An integer total that was calculated from rows, columns, or 
//              diagonals.
// Parameter 2: int magicNumber
//            - A number created from the formula (N(N^2 + 1))/2
// Returns: boolean true or false
//*****************************************************************************
bool testMagic(int total, int magicNumber){

  if (total == magicNumber)
    return true;
  else
    return false;
}
