###############################################################################
# Jon-Paul K. Kasper, CS2318-254, Assignment 2 Part C
#
# Part C of Assignment 2 creates and manipulates an integer array. The array 
# is initialized on creation and the contents are swapped around. Finally the
# array is printed in reverse.
###############################################################################

############################### Data Section ##################################
			
			.data
intArray:		.word 44, 99, 33, 11, 55
beforeLabel:		.asciiz "The following is the original order of the array: "
afterLabel:		.asciiz "The following is the array in reverse: "
rearrange:		.asciiz "Rearranging the array..."
one:			.asciiz "First element: "
two:			.asciiz "Second element: "
three:			.asciiz "Third element: "
four:			.asciiz "Fourth element: "
five:			.asciiz "Fifth element: "

################################ Operations ###################################

			.text
			.globl main
main:
			# print the array before manipulation
			li $v0, 4
			la $a0, beforeLabel
			syscall
			li $a0, '\n'
			li $v0, 11
			syscall
			li $v0, 4
			la $a0, one
			syscall
			la $t0, intArray
			li $v0, 1
			lw $a0, 0($t0)  # fist element
			syscall
			li $a0, '\n'
			li $v0, 11
			syscall
			li $v0, 4
			la $a0, two
			syscall
			li $v0, 1
			lw $a0, 4($t0)  # second element
			syscall
			li $a0, '\n'
			li $v0, 11
			syscall
			li $v0, 4
			la $a0, three
			syscall
			li $v0, 1
			lw $a0, 8($t0)  # third element
			syscall
			li $a0, '\n'
			li $v0, 11
			syscall
			li $v0, 4
			la $a0, four
			syscall
			li $v0, 1
			lw $a0, 12($t0) # fourth element
			syscall
			li $a0, '\n'
			li $v0, 11
			syscall
			li $v0, 4
			la $a0, five
			syscall
			li $v0, 1
			lw $a0, 16($t0) # fifth element
			syscall
			li $v0, 11
			li $a0, '\n'
			syscall
			li $v0, 11
			li $a0, '\n'
			syscall
			
			# rearrange the array
			li $v0, 4
			la $a0, rearrange
			syscall
			li $v0, 11
			li $a0, '\n'
			syscall
			lw $t1, 0($t0) # load the first element
			lw $t2, 12($t0) # load the fourth element
			sw $t1, 12($t0) # store the first element into the fourth
			sw $t2, 0($t0) # store the fourth element into the first
			lw $t3, 4($t0) # load the second element
			lw $t4, 16($t0) # load the fifth element
			sw $t3, 16($t0) # store the second element into the fifth
			sw $t4, 4($t0) # store the fifth element into the second
			syscall
			
			# print the array after manipulation
			li $v0, 4
			la $a0, afterLabel
			syscall
			li $a0, '\n'
			li $v0, 11
			syscall
			li $v0, 4
			la $a0, five
			syscall
			la $t0, intArray
			li $v0, 1
			lw $a0, 16($t0) # print the fifth element
			syscall
			li $a0, '\n'
			li $v0, 11
			syscall
			li $v0, 4
			la $a0, four
			syscall
			li $v0, 1
			lw $a0, 12($t0) # print the fourth element
			syscall
			li $a0,'\n'
			li $v0, 11
			syscall
			li $v0, 4
			la $a0, three
			syscall
			li $v0, 1
			lw $a0, 8($t0) # print the third element
			syscall
			li $a0, '\n'
			li $v0, 11
			syscall
			li $v0, 4
			la $a0, two
			syscall
			li $v0, 1
			lw $a0, 4($t0) # print the second element
			syscall
			li $a0, '\n'
			li $v0, 11
			syscall
			li $v0, 4
			la $a0, one
			syscall
			li $v0, 1
			lw $a0, 0($t0) # print the first element
			syscall
			li $v0, 11
			li $a0, '\n'
			syscall
			
			# exit the program
			li $v0, 10
			syscall
