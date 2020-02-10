/******************************************************************************
NAME : Jon-Paul Kasper			CS 4350 - Unix Systems Programming
Serial Number : 15
Assignment Number : 6
Due Date : 11 / 18 / 2019
******************************************************************************/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define NUM_COUNT 7

// prototype for the done function
// removes the temp file that is needed for the main program
// called dureing atexit attempt
void done();

int main() {
   FILE *filePointer;
   FILE *outFilePointer;
   FILE *outFile2Pointer;

   // gather various information from an input file and store in a file
   // information gathered: 
   // number of lines, number of words, number of lower case letters,
   // number of capital letters, number of digits, number of spaces,
   // number of special symbols
   system("wc -l < zp6in.txt > file.txt");
   system("wc -w < zp6in.txt >> file.txt");
   system("grep -o [a-z] < zp6in.txt | tr -d \"\n\" | wc -m >> file.txt");
   system("grep -o [A-Z] < zp6in.txt | tr -d \"\n\" | wc -m >> file.txt");
   system("grep -o \"[[:digit:]]\" < zp6in.txt | wc -l >> file.txt");
   system("grep -o ' ' < zp6in.txt | wc -l >> file.txt");
   system("grep -o \"[[:punct:]]\" < zp6in.txt | wc -l >> file.txt");

   // gather the numbers stored from the system commands above
   filePointer = fopen("file.txt", "r");
   int numlist[NUM_COUNT];
   int i = 0;
   for(i = 0; i < NUM_COUNT; i++) 
      fscanf(filePointer, "%d", &numlist[i]);
   
   // display the values gathered from above
   printf("\n\nFile Manipulation Program\n\n");
   printf("# of lines in the input file zp6in.txt: %d\n\n", numlist[0]);
   printf("# of words in the input file zp6in.txt: %d\n\n", numlist[1]);
   printf("# of small letters in the input file zp6in.txt: %d\n\n", numlist[2]);
   printf("# of capital letters in the input file zp6in.txt: %d\n\n", numlist[3]);
   printf("# of digits in the input file zp6in.txt: %d\n\n", numlist[4]);
   printf("# of spaces in the input file zp6in.txt: %d\n\n", numlist[5]);
   printf("# of special symbols in the input file zp6in.txt: %d\n\n", numlist[6]);

   fclose(filePointer);

   // set up file pointers for future file access      
   filePointer = fopen("zp6in.txt", "r");
   outFilePointer = fopen("zp6out1.txt", "w");
   outFile2Pointer = fopen("zp6out2.txt", "w");

   // copy the content of the input file without spaces and convert
   // small letters to capital and capital to small letters.
   // Print the changes to a new file "zp6out1.txt"
   char ch;
   while((ch = getc(filePointer)) != EOF) {
      if ('a' <= ch && ch <= 'z') {
         ch = toupper(ch);
         fprintf(outFilePointer, "%c", ch);
      } else if ('A' <= ch && ch <= 'Z') {
         ch = tolower(ch);
         fprintf(outFilePointer, "%c", ch);
      } else if (ch == ' ') {
         continue;
      } else {
         fprintf(outFilePointer, "%c", ch);
      }
   }
   
   // move the file pointer to the beginning of the file
   fseek(filePointer, 0, SEEK_SET);

   // read the input file one line at a time and write the lines to a second
   // file "zp6out2.txt" adding a number for each line in the new file
   char line[255];
   i = 1;
   while (fgets(line, 255, filePointer) != NULL) {
      fprintf(outFile2Pointer, "%d. ", i);
      fputs(line, outFile2Pointer);
      i++;
   }

   // use a system command to display the content of "zp6out1.txt" and
   // "zp6out2.txt" and the signature line at the end
   fseek(outFilePointer, 0, SEEK_SET);
   fseek(outFile2Pointer, 0, SEEK_SET);
   system("echo; echo The contents of zp6out1.txt; echo;");
   system("cat zp6out1.txt;");
   system("echo; echo The contents of zp6out2.txt; echo;");
   system("cat zp6out2.txt;");
   system("echo; echo; echo;");
   system("echo Implemented by Jon-Paul Kasper;");
   system("echo November - 18 - 2019; echo;");

   // close the files
   fclose(filePointer);
   fclose(outFilePointer);
   fclose(outFile2Pointer);

   // clean up after the end of the program
   if (atexit(done) != 0)
      printf("\n\nerror with atexit\n\n");

   return EXIT_SUCCESS;
}

// removes the temp file that is needed for the main program
// called during atexit attempt
void done() {
   system("rm file.txt");
}
