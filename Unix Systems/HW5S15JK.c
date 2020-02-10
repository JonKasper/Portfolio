/******************************************************************************
NAME : Jon-Paul Kasper			CS 4350 - Unix Systems Programming
Serial Number : 15
Assisgnment Number : 5
Due Date : 11 / 4 / 2019
******************************************************************************/

#include <stdio.h>
#include <stdlib.h>

// This function uses a random number generator to pull from a list of 
// characters to form a password
void passwordGenerator(char password[]) {
   int random = 0;
   char passNum[] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
   char passChar[] = {'!', '$', '%', '&', '\'', '(', ')', '*', '+',
                    ',', '-', '.', '/', ';', '<', '=', '>', '?',
                    '@', '[', ']', '}', '{', '^', '~', '#', '`', ':'};
   char passCap[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                    'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z'};
   char passLow[] = {'z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q', 
                   'p', 'o', 'n', 'm', 'l', 'k', 'j', 'i', 'h', 'g', 
                   'f', 'e', 'd', 'c', 'b', 'a'};

   random = rand() % (sizeof(passNum) / sizeof(char)) + 1;
   password[0] = passNum[random];

   random = rand() % (sizeof(passChar) / sizeof(char)) + 1;
   password[1] = passChar[random];

   random = rand() % (sizeof(passCap) / sizeof(char)) + 1;
   password[2] = passCap[random];
   
   random = rand() % (sizeof(passLow) / sizeof(char)) + 1;
   password[3] = passLow[random];

   printf("\nPassword is Generated\n\n\n\n");
}

// This function takes the input password guess from the user
// and compares it to the password that was generator
void passwordDetect(char *password, char *choice, size_t size) {
   int i = 0;
   int match = 0;

   // compare the two arrays and see if they match
   for(i = 0; i < size; i++) {
      if(password[i] == choice[i])
         match += 1;
   }

   if (match == 0)
      printf("\nIncorrect Password\n\n\n\n");
   else
      printf("\nCorrect Password\n\n\n\n");
}

int main() {
   char readIn[4];
   char password[4];
   char choice[4];
   int temp = 0;
   int menu = 0;
   int size = sizeof(password) / sizeof(char);

   printf("Password Generator\n\n");
   printf("This program will:-\n");
   printf("\t*  Generate a password.\n");
   printf("\t*  Guesses the password\n");
   printf("\t*  Displays the Generated Password and Terminates the Program");
   printf("\n\n\n\n\n");

   // loop until the user selects the exit option
   do {
      printf("Select one of the following:\n\n");
      printf("\t1.  Generate a Password\n");
      printf("\t2.  Detect Password\n");
      printf("\t9.  Display the Password and Exit The program\t");

      // read menu input from the user
      while((readIn[temp++] = getchar()) != '\n' && temp < 4);
      menu = atoi(readIn);

      switch (menu)
      {
         case 1:
            passwordGenerator(password);
            break;
         case 2:
            // get the password guess from the user
            printf("\n\nEnter Password :\t");
            temp = 0;
            while((choice[temp++] = getchar()) != '\n' && temp < size);
            passwordDetect(password, choice, size);
            getchar();
            break;
         case 9:
            printf("\n\nThe Generated Password :\t");
            for(temp = 0; temp < size; temp++)
               printf("%c", password[temp]);
            printf("\n\n");
            break;
         default:
            printf("\n\nInvalid Selection\n\n\n\n");
            break;
      }
      temp = 0;
   } while (menu != 9);

   printf("This Algorith is designed and Implemented by\n");
   printf("Jon-Paul Kasper - Security Group Inc.\n");
   printf("November - 4 - 2019\n\n");

   return EXIT_SUCCESS;
}
