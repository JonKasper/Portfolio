#include <iostream>
using namespace std;

int  GetOneIntByVal(const char prompt[]);
void GetOneIntByAddr(int* intVarToPutInPtr, const char prompt[]);
void ChkAdjIntInputs(int* int1Ptr, int* int2Ptr, int high1, int high2);
void prtRunLabel(const char runNumLab[], int runNum);
void prtOutLabel(const char runOutLab[], int numVals);
void prtIntArr(const int intArr[], int size);

int main()
{
   int intArr[5];
   char ttrPrompt[] = "times to run? ";
   char vprPrompt[] = "vals per run? ";
   char runNumLab[] = "run #";
   char entIntPrompt[] = "enter an int: ";
   char runOutLab[] = " ints: ";
   int timesToRun;
   int valsPerRun;
   int i;
   int j;

   timesToRun = GetOneIntByVal(ttrPrompt);
   GetOneIntByAddr(&valsPerRun, vprPrompt);
   ChkAdjIntInputs(&timesToRun, &valsPerRun, 3, 5);
   for (i = timesToRun ; i > 0; --i)
   {
      prtRunLabel(runNumLab, timesToRun - i + 1);
      for (j = valsPerRun; j > 0; --j)
         GetOneIntByAddr(intArr + valsPerRun - j, entIntPrompt);
      prtOutLabel(runOutLab, valsPerRun);
      prtIntArr(intArr, valsPerRun);
   }

   return 0;
}

int  GetOneIntByVal(const char prompt[])
{
   cout << prompt;
   int oneInt;
   cin >> oneInt;
   return oneInt;
}

void GetOneIntByAddr(int* intVarToPutInPtr, const char prompt[])
{
   cout << prompt;
   cin >> *intVarToPutInPtr;
}

void ChkAdjIntInputs(int* int1Ptr, int* int2Ptr, int high1, int high2)
{
   if (*int1Ptr < 1)
      *int1Ptr = 1;
   if (*int1Ptr > high1)
      *int1Ptr = high1;
   if (*int2Ptr < 1)
      *int2Ptr = 1;
   if (*int2Ptr > high2)
      *int2Ptr = high2;
}

void prtRunLabel(const char runNumLab[], int runNum)
{
   cout << runNumLab << runNum << ":\n";
}

void prtOutLabel(const char runOutLab[], int numVals)
{
   cout << numVals << runOutLab;
}

void prtIntArr(const int intArr[], int size)
{
   int i = size;
   while (i >= 1)
   {
      cout << intArr[size - i] << ' ';
      --i;
   }
   cout << endl;
}
