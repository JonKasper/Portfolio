################################################################################
# MIPS assembly language translation of a contrived C++ program
# An example program illustrating:
# - MIPS basic support for doing functions (procedures)
# - pass-by-value versus pass-by-address
# NOTES:
# - does NOT follow function-call convention to be eventually covered/adopted
################################################################################
# Algorithm used:
# Given C++ program (TrivialFunc_PassingMechEg01.cpp)
################################################################################
# Sample test run:
##################
# times to run? 2
# vals per run? 4
# run #1:
# enter an int: 1
# enter an int: 2
# enter an int: 3
# enter an int: 4
# 4 ints: 1 2 3 4 
# run #2:
# enter an int: 4
# enter an int: 3
# enter an int: 2
# enter an int: 1
# 4 ints: 4 3 2 1 
################################################################################
# int GetOneIntByVal(const char prompt[]);
# void GetOneIntByAddr(int* intVarToPutInPtr, const char prompt[]);
# void ChkAdjIntInputs(int* int1Ptr, int* int2Ptr, int high1, int high2);
# void prtRunLabel(const char runNumLab[], int runNum);
# void prtOutLabel(const char runOutLab[], int numVals);
# void prtIntArr(const int intArr[], int size);
#
#int main()
#{
					.text
					.globl main
################################################################################
main:					
#   int intArr[5];
#   char ttrPrompt[] = "times to run? ";
#   char vprPrompt[] = "vals per run? ";
#   char runNumLab[] = "run #";
#   char entIntPrompt[] = "enter an int: ";
#   char runOutLab[] = " ints: ";
#   int timesToRun;
#   int valsPerRun;
#   int i;
#   int j;
#################
# Register Usage:
#################
# $t0: register holder for a value
# $t1: i
# $t2: j
#################
					addiu $sp, $sp, -87
					li $t0, ' '
					sb $t0,      0($sp)
					li $t0, 'i'
					sb $t0,      1($sp)
					li $t0, 'n'
					sb $t0,      2($sp)
					li $t0, 't'
					sb $t0,      3($sp)
					li $t0, 's'
					sb $t0,      4($sp)
					li $t0, ':'
					sb $t0,      5($sp)
					li $t0, ' '
					sb $t0,      6($sp)
					li $t0, '\0'
					sb $t0,      7($sp)
					li $t0, 'e'
					sb $t0,      8($sp)
					li $t0, 'n'
					sb $t0,      9($sp)
					li $t0, 't'
					sb $t0,      10($sp)
					li $t0, 'e'
					sb $t0,      11($sp)
					li $t0, 'r'
					sb $t0,      12($sp)
					li $t0, ' '
					sb $t0,      13($sp)
					li $t0, 'a'
					sb $t0,      14($sp)
					li $t0, 'n'
					sb $t0,      15($sp)
					li $t0, ' '
					sb $t0,      16($sp)
					li $t0, 'i'
					sb $t0,      17($sp)
					li $t0, 'n'
					sb $t0,      18($sp)
					li $t0, 't'
					sb $t0,      19($sp)
					li $t0, ':'
					sb $t0,      20($sp)
					li $t0, ' '
					sb $t0,      21($sp)
					li $t0, '\0'
					sb $t0,      22($sp)
					li $t0, 'r'
					sb $t0,      23($sp)
					li $t0, 'u'
					sb $t0,      24($sp)
					li $t0, 'n'
					sb $t0,      25($sp)
					li $t0, ' '
					sb $t0,      26($sp)
					li $t0, '#'
					sb $t0,      27($sp)
					li $t0, '\0'
					sb $t0,      28($sp)
					li $t0, 'v'
					sb $t0,      29($sp)
					li $t0, 'a'
					sb $t0,      30($sp)
					li $t0, 'l'
					sb $t0,      31($sp)
					li $t0, 's'
					sb $t0,      32($sp)
					li $t0, ' '
					sb $t0,      33($sp)
					li $t0, 'p'
					sb $t0,      34($sp)
					li $t0, 'e'
					sb $t0,      35($sp)
					li $t0, 'r'
					sb $t0,      36($sp)
					li $t0, ' '
					sb $t0,      37($sp)
					li $t0, 'r'
					sb $t0,      38($sp)
					li $t0, 'u'
					sb $t0,      39($sp)
					li $t0, 'n'
					sb $t0,      40($sp)
					li $t0, '?'
					sb $t0,      41($sp)
					li $t0, ' '
					sb $t0,      42($sp)
					li $t0, '\0'
					sb $t0,      43($sp)
					li $t0, 't'
					sb $t0,      44($sp)
					li $t0, 'i'
					sb $t0,      45($sp)
					li $t0, 'm'
					sb $t0,      46($sp)
					li $t0, 'e'
					sb $t0,      47($sp)
					li $t0, 's'
					sb $t0,      48($sp)
					li $t0, ' '
					sb $t0,      49($sp)
					li $t0, 't'
					sb $t0,      50($sp)
					li $t0, 'o'
					sb $t0,      51($sp)
					li $t0, ' '
					sb $t0,      52($sp)
					li $t0, 'r'
					sb $t0,      53($sp)
					li $t0, 'u'
					sb $t0,      54($sp)
					li $t0, 'n'
					sb $t0,      55($sp)
					li $t0, '?'
					sb $t0,      56($sp)
					li $t0, ' '
					sb $t0,      57($sp)
					li $t0, '\0'
					sb $t0,      58($sp)
#
#   timesToRun = GetOneIntByVal(ttrPrompt);
					addi $a0, $sp, 44
					jal GetOneIntByVal
					sw $v0, 63($sp)
#   GetOneIntByAddr(&valsPerRun, vprPrompt);
					addi $a0, $sp, 59
					addi $a1, $sp, 29
					jal GetOneIntByAddr
#   ChkAdjIntInputs(&timesToRun, &valsPerRun, 3, 5);
					addi $a0, $sp, 63
					addi $a1, $sp, 59
					li $a2, 3
					li $a3, 5
					jal ChkAdjIntInputs
#   for (i = timesToRun ; i > 0; --i)
#   {
					lw $t1, 63($sp)				# $t1 is i
					j FTest1
begFBody1:					
#      prtRunLabel(runNumLab, timesToRun - i + 1);
					addi $a0, $sp, 23
					lw $a1, 63($sp)
					sub $a1, $a1, $t1
					addi $a1, $a1, 1
					jal prtRunLabel
#      for (j = valsPerRun; j > 0; --j)
					lw $t2, 59($sp)
					j FTest2
begFBody2:					
#         GetOneIntByAddr(intArr + valsPerRun - j, entIntPrompt);
					lw $a0, 59($sp)
					sub $a0, $a0, $t2
					sll $a0, $a0, 2
					addi $a0, $a0, 67
					add $a0, $a0, $sp
					addi $a1, $sp, 8
					jal GetOneIntByAddr
         
					addi $t2, $t2, -1
FTest2:
					bgtz $t2, begFBody2         
#      prtOutLabel(runOutLab, valsPerRun);
					move $a0, $sp
					lw $a1, 59($sp)
					jal prtOutLabel
#      prtIntArr(intArr, valsPerRun);
					addi $a0, $sp, 67
					lw $a1, 59($sp)
					jal prtIntArr
      
					addi $t1, $t1, -1
#   }
FTest1:
					bgtz $t1, begFBody1
   
#   return 0;
#}
					addiu $sp, $sp, 87
					li $v0, 10
					syscall
################################################################################
#int GetOneIntByVal(const char prompt[])
#{
GetOneIntByVal:
#   cout << prompt;
					li $v0, 4
					syscall
#   int oneInt;
#   cin >> oneInt;
#   return oneInt;
					li $v0, 5
					syscall
#}
					jr $ra

################################################################################
#void GetOneIntByAddr(int* intVarToPutInPtr, const char prompt[])
#{
GetOneIntByAddr:
#################
# Register Usage:
#################
# $t0: holder for saving 1st arg ($a0) received
#################
					move $t0, $a0			# save intVarToPutInPtr in $t0
#   cout << prompt;
					move $a0, $a1
					li $v0, 4
					syscall
#   cin >> *intVarToPutInPtr;
					li $v0, 5
					syscall
					sw $v0, 0($t0)
#}
					jr $ra

################################################################################
#void ChkAdjIntInputs(int* int1Ptr, int* int2Ptr, int high1, int high2)
#{
ChkAdjIntInputs:
#################
# Register Usage:
#################
# $t0: holder for a value loaded from memory
# $v1: holder constant 1
#################
					li $v1, 1				# $v1 has constant 1
#   if (*int1Ptr < 1)
					lw $t0, 0($a0)			# $t0 has *int1Ptr
					bge $t0, $v1, endIf1
#      *int1Ptr = 1;
					sw $v1, 0($a0)
endIf1:
#   if (*int1Ptr > high1)
					ble $t0, $a2, endIf2
#      *int1Ptr = high1;
					sw $a2, 0($a0)
endIf2:
#   if (*int2Ptr < 1)
					lw $t0, 0($a1)			# $t0 has *int2Ptr
					bge $t0, $v1, endIf3
#      *int2Ptr = 1;
					sw $v1, 0($a1)
endIf3:
#   if (*int2Ptr > high2)
					ble $t0, $a3, endIf4
#      *int2Ptr = high2;
					sw $a3, 0($a1)
endIf4:
#}
					jr $ra

################################################################################
# void prtRunLabel(const char runNumLab[], int runNum)
#{
prtRunLabel:
#   cout << runNumLab << runNum << ":\n";
					li $v0, 4
					syscall
					move $a0, $a1
					li $v0, 1
					syscall					
					li $a0, ':'
					li $v0, 11
					syscall
					li $a0, '\n'
					syscall
#}
					jr $ra

################################################################################
#void prtOutLabel(const char runOutLab[], int numVals)
#{
prtOutLabel:
#################
# Register Usage:
#################
# $t0: holder for saving 1st arg ($a0) received
#################
					move $t0, $a0			# save &runOutLab[0] in $t0
#   cout << numVals << runOutLab;
					move $a0, $a1
					li $v0, 1
					syscall
					move $a0, $t0
					li $v0, 4
					syscall
#}
					jr $ra

################################################################################
#void prtIntArr(const int intArr[], int size)
#{
prtIntArr:
#################
# Register Usage:
#################
# $a2: i
# $a3: holder for building target address in memory
# $t0: holder for saving 1st arg ($a0) received
# $v1: holder for constant 1
#################
#   int i = size;
					move $t0, $a0			# save &intArr[0] in $t0
					move $a2, $a1			# $a2 is i
					#move $t1, $a1			# $t1 is i
#   while (i >= 1)
#   {
					li $v1, 1				# $v1 has constant 1
					j WTest
begWBody:					
#      cout << intArr[size - i] << ' ';
					sub $a3, $a1, $a2		# $a3 has size - i
					#sub $a3, $a1, $t1		# $a3 has size - i
					sll $a3, $a3, 2			# $a3 has (size - i)*4
					add $a3, $a3, $t0		# $a3 has &intArr[size - i]
					lw $a0, 0($a3)			# $a0 has intArr[size - 1]
					li $v0, 1
					syscall
					li $v0, 11
					li $a0, ' '
					syscall
#      --i;
					addi $a2, $a2, -1
					#addi $t1, $t1, -1
#   }
WTest:
					bge $a2, $v1, begWBody
#   cout << endl;
					li $v0, 11
					li $a0, '\n'
					syscall
#}
					jr $ra
################################################################################
