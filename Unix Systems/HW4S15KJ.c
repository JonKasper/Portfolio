/******************************************************************************
NAME: Jon-Paul Kasper
Serial Number: 15
Assignment Number: 4
Due Date: 10/21/2019
******************************************************************************/

// The purpose of this program is to test the function calls and returns
// using C language. The program creates a printed pattern based on four
// different algorithms. The program reads in, and validates, input from
// the user in order to determine the pattern that is printed.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// patternOne takes the passed patSize integer from callPattern and uses
// the value to print a pattern of diagonal numbers starting from the
// top left
void patternOne(int patSize)
{
   printf("\nPattern 1 is Displayed\n\n");
   int i;
   int j;
   for(i = 0; i < patSize; i++) {
      for(j = 0; j < patSize; j++) {
         if(j == i) {
            printf("%d", patSize);
         } else {
            printf("P");
         }
      }
      printf("\n");
   }
   printf("\n\n");
}

// patternTwo takes the passed patSize integer from callPattern and uses
// the value to print a pattern of diagonal numbers starting from the
// top right
void patternTwo(int patSize)
{
   printf("\nPattern 2 is Displayed\n\n");
   int i;
   int j;
   for(i = patSize; i > 0; i--) {
      for(j = 0; j < patSize; j++) {
         if(j == (i - 1)) {
            printf("%d", patSize);
         } else {
            printf("P");
         }
      }
      printf("\n");
   }
   printf("\n\n");
}

// patternThree takes the passed patSize integer from callPattern and uses
// the value to print a pattern of increasing number count from the right
void patternThree(int patSize)
{
   printf("\nPattern 3 is Displayed\n\n");
   int i;
   int j;
   int max = patSize;
   for(i = patSize; i > 0; i--) {
      for(j = 0; j < max; j++) {
         printf("P");
      }
      for(j = 0; j < (patSize - max); j++) {
         printf("%d", patSize);
      }
      max--;
      printf("\n");
   }
   printf("\n\n");
}

// patternFour takes the passed patSize integer from callPattern and uses 
// the value to print a pattern of increasing number count from the left
void patternFour(int patSize)
{
   printf("\nPattern 4 is Displayed\n\n");
   int i;
   int j;
   int max = 0;
   for(i = patSize; i > 0; i--) {
      for(j = 0; j < max; j++) {
         printf("%d", patSize);
      }
      for(j = 0; j < (patSize - max); j++) {
         printf("P");
      }
      max++;
      printf("\n");
   }
   printf("\n\n");
}

// callPattern takes in the passed patSize and choice integers from 
// patternChoice and uses them to select the appropriate pattern to be called
void callPattern(int patSize, int choice)
{
   switch (choice)
   {
      case 1:
         patternOne(patSize);
         break;
      case 2:
         patternTwo(patSize);
         break;
      case 3:
         patternThree(patSize);
         break;
      case 4:
         patternFour(patSize);
         break;
   }
}

// patternChoice takes in the passed patSize and choice integers and prompts
// the user for a pattern size. The size is then verified and callPattern
// is called.
void patternChoice(int patSize, int choice)
{
   char readIn[10];
   int temp = 0;
      
   do
   {
      // loop until a proper case is made
      printf("\nChoose a pattern size ( between 2 and 9 ): ");

      // read in individual characters until a newline is read
      while((readIn[temp++] = getchar()) != '\n' && temp < 10);

      // convert the character array into an integer
      patSize = atoi(readIn);

      switch (patSize)
      {
         case 2:
            callPattern(patSize, choice);
            break;
         case 3:
            callPattern(patSize, choice);
            break;
         case 4:
            callPattern(patSize, choice);
            break;
         case 5:
            callPattern(patSize, choice);
            break;
         case 6:
            callPattern(patSize, choice);
            break;
         case 7:
            callPattern(patSize, choice);
            break;
         case 8:
            callPattern(patSize, choice);
            break;
         case 9:
            callPattern(patSize, choice);
            break;
         default:
            printf("\nYour pattern size is incorrect. ");
            printf("Please try again.\n");
            break;
      }

      // flush the input
      if(patSize < 2 || patSize > 9) {
         temp = 0;
         patSize = 0;
      }

   } while(patSize < 2 || patSize > 9);
}

// menuPrint is used to print the menu after each pattern is printed
// for convenience
void menuPrint()
{
   printf("Menu\n\n");
   printf("1.\tPattern One\n");
   printf("2.\tPattern Two\n");
   printf("3.\tPattern Three\n");
   printf("4.\tPattern Four\n");
   printf("15.\tQuit\n\n");
}

int main(void)
{
   printf("\n\t\t\t   Welcome to My Pattern Program\n\n");
   printf("This program is written by Jon-Paul Kasper. ");
   printf("The purpose of this program is to create\n");
   printf("four different patterns of different sizes. ");
   printf("The size of each pattern is determined by the\n");
   printf("number of columns or rows. ");
   printf("For example, a pattern of size 5 has 5 columns and 5 rows.\n");
   printf("Each pattern is made up of character P and a digit, ");
   printf("which shows the size. The size\nmust be between 2 and 9\n\n");

   char readIn[10];
   int choice = 0;
   int patSize = 0;
   int temp = 0;

   menuPrint();

   do {	
      // loop until the correct case is made
      printf("Choose an option ( between 1 and 4 or 15 to end the ");
      printf("program ): ");

      // read in each character until a newline is reached
      while((readIn[temp++] = getchar()) != '\n' && temp < 10);

      // convert the character array to an integer
      choice = atoi(readIn);

      switch (choice)
      {
         case 1:
            patternChoice(patSize, choice);
            menuPrint();
            break;
         case 2:
            patternChoice(patSize, choice);
            menuPrint();
            break;
         case 3:
            patternChoice(patSize, choice);
            menuPrint();
            break;
         case 4:
            patternChoice(patSize, choice);
            menuPrint();
            break;
         case 15:
            break;
         default:
            printf("\nYour option is incorrect. Please try again.\n\n");
            break;
      }

      // flush the input
      if(choice != 15) {
         choice = 0;
         temp = 0;
      }

   } while(choice != 15);

   // exit the program
   printf("\nPattern Program By:\n");
   printf("Jon-Paul Kasper - 10 - 21 - 2019\n");
   return EXIT_SUCCESS;
}
