/******************************************************************************
* Jon-Paul K. Kasper
* Assignment 2 Part 2
* Due : 03/28/2019
*
* This program simulates the usage of while, for, and do-while looping 
* structures. The normal entrances into these structures has been replaced by
* goto jumps.
******************************************************************************/

#include <iostream>
using namespace std;

int  a1[12],
     a2[12],
     a3[12];
char reply;
int  used1,
     used2,
     used3,
     remCount,
     anchor;
int* hopPtr1;
int* hopPtr11;
int* hopPtr2;
int* hopPtr22;
int* hopPtr222;
int* hopPtr3;
int* endPtr1;
int* endPtr2;
int* endPtr3;

char begA1Str[] = "\nbeginning a1: ";
char proA1Str[] = "processed a1: ";
char comA2Str[] = "          a2: ";
char comA3Str[] = "          a3: ";
char einStr[]   = "Enter integer #";
char moStr[]    = "Max of ";
char ieStr[]    = " ints entered...";
char emiStr[]   = "Enter more ints? (n or N = no, others = yes) ";
char dacStr[]   = "Do another case? (n or N = no, others = yes) ";
char dlStr[]    = "================================";
char byeStr[]   = "bye...";

int main()
{
begDW1:             
                used1 = 0;
                hopPtr1 = a1;
begDW2:
                cout << einStr;
                cout << (used1 + 1);
                cout << ':' << ' ';
                cin >> *hopPtr1;
                ++used1;
                ++hopPtr1;

                if (used1 != 12) goto else1;
                cout << moStr;
                cout << 12;
                cout << ieStr;
                cout << endl;
                reply = 'n';
                goto endif1;
else1:
                cout << emiStr;
                cin >> reply;
endif1:
endDW2:
DW2Test:        if (reply != 'n' && reply != 'N') goto begDW2;

                cout << begA1Str;
                hopPtr1 = a1;
                endPtr1 = a1 + used1;
                goto W1Test;
begW1:
                if (hopPtr1 != endPtr1 - 1) goto else2;
                cout << *hopPtr1 << endl;
                goto endif2;
else2:
                cout << *hopPtr1 << ' ';
endif2:
                ++hopPtr1;
W1Test:         if (hopPtr1 < endPtr1) goto begW1;
endW1:

                hopPtr1 = a1;
                hopPtr2 = a2;
                used2 = 0;
                goto F1Test;
begF1:
                *hopPtr2 = *hopPtr1;
                ++hopPtr1;
                ++hopPtr2;
                ++used2;
F1Test:         if (hopPtr1 < endPtr1) goto begF1;
endF1:

                hopPtr2 = a2;
                endPtr2 = a2 + used2;
                goto W2Test;
begW2:
                anchor = *hopPtr2;
                hopPtr22 = hopPtr2 + 1;
                goto F2Test;
begF2:
                if (*hopPtr22 != anchor) goto endif3;
                hopPtr222 = hopPtr22 + 1;
                goto F3Test;
begF3:
                *(hopPtr222 - 1) = *hopPtr222;
                ++hopPtr222;
F3Test:         if (hopPtr222 < endPtr2) goto begF3;
                --used2;
                --endPtr2;
                --hopPtr22;
endif3:
                ++hopPtr22;
F2Test:         if (hopPtr22 < endPtr2) goto begF2;
endF2:
                ++hopPtr2;
W2Test:         if (hopPtr2 < endPtr2) goto begW2;
endW2:

                used3 = 0;
                hopPtr3 = a3;
                hopPtr1 = a1;
                goto W3Test;
begW3:
                *hopPtr3 = *hopPtr1;
                ++used3;
                ++hopPtr3;
                anchor = *hopPtr1;
                remCount = 0;
                hopPtr11 = hopPtr1 + 1;
                goto F4Test;
begF4:
                if (*hopPtr11 != anchor) goto else4;
                ++remCount;
                goto endif4;
else4:
                *(hopPtr11 - remCount) = *hopPtr11;
endif4:
                ++hopPtr11;
F4Test:         if (hopPtr11 < endPtr1) goto begF4;
endF4:
                used1 -= remCount;
                endPtr1 -= remCount;
                ++hopPtr1;
W3Test:         if (hopPtr1 < endPtr1) goto begW3;
endW3:

                cout << proA1Str;
                hopPtr1 = a1;
                goto F5Test;
begF5:
                if (hopPtr1 != endPtr1 - 1) goto else5;
                cout << *hopPtr1 << endl;
                goto endif5;
else5:
                cout << *hopPtr1 << ' ';
endif5:
                ++hopPtr1;
F5Test:         if (hopPtr1 < endPtr1) goto begF5;
endF5:
                cout << comA2Str;
                hopPtr2 = a2;
                goto F6Test;
beginF6:
                if (hopPtr2 != endPtr2 - 1) goto else6;
                cout << *hopPtr2 << endl;
                goto endif6;
else6:
                cout << *hopPtr2 << ' ';
endif6:
                ++hopPtr2;
F6Test:         if (hopPtr2 < endPtr2) goto beginF6;
endF6:
                cout << comA3Str;
                hopPtr3 = a3;
                endPtr3 = a3 + used3;
                goto W4Test;
begW4:
                if (hopPtr3 != endPtr3 - 1) goto else7;
                cout << *hopPtr3 << endl;
                goto endif7;
else7:
                cout << *hopPtr3 << ' ';
endif7:
                ++hopPtr3;
W4Test:         if (hopPtr3 < endPtr3) goto begW4;
endW4:

                cout << endl;
                cout << dacStr;
                cin >> reply;
                cout << endl;
endDW1:
DW1Test:        if (reply != 'n' && reply != 'N') goto begDW1;

                cout << dlStr;
                cout << '\n';
                cout << byeStr;
                cout << '\n';
                cout << dlStr;
                cout << '\n';

                return 0;
}
