###############################################################################
# Jon-Paul K. Kasper, CS 2318-254, Assignment 2 Part D
# 
# Assignment 2 Part D calculates a weighted average of three test grades using
# the following formula: 
# 
#             (115/512)*e1Score+(8/29)*e2Score+(finScore/2)
# 
###############################################################################

############################## Data Section ###################################

			.data
fgLabel:		.asciiz "Enter the first test grade: "
sgLabel:		.asciiz "Enter the second test grade: "
tgLabel:		.asciiz "Enter the final test grade: "
calcStr:		.asciiz "Calculating average based on formula... "
final:			.asciiz "Your average is: "
test:			.asciiz "Test value: "

############################### Operations ####################################

			.text
			.globl main
main:
			# prompt and read in first grade
			li $v0, 4
			la $a0, fgLabel
			syscall
			li $v0, 5
			syscall
			move $t0, $v0
			syscall
			
			# prompt and read in second grade
			li $v0, 4
			la $a0, sgLabel
			syscall
			li $v0, 5
			syscall
			move $t1, $v0
			syscall
			
			# prompt and read in final grade
			li $v0, 4
			la $a0, tgLabel
			syscall
			li $v0, 5
			syscall
			move $t2, $v0
			li $v0, 11
			li $a0, '\n'
			syscall
			
			# Calculate the average grade
			li $v0, 4
			la $a0, calcStr
			syscall
			li $v0, 11
			li $a0, '\n'
			syscall
			addi $t8, $zero, 115	# store 115 into a temp register
			mult $t0, $t8 		# multiply the first grade by 115
			mflo $t9 		# store the result in $t9
			srl $t9, $t9, 9 	# divide by 512
			
			sub $t8, $t8, $t8 	# zero out $t8
			addi $t8, $zero, 29 	# store 29 in $t8
			sll $t7, $t1, 3 	# multiply by 8
			div $t7, $t8 		# divide by $t8
			mflo $t6 		# get the quotient
			add $t9, $t9, $t6 	# add the second part of the problem to the total
			
			srl $t8, $t2, 1 	# divide by 2
			add $t9, $t9, $t8 	# get the total average
			syscall
			
			# print the result of the calculation
			li $v0, 4
			la $a0, final
			syscall
			move $a0, $t9
			li $v0, 1
			syscall
			
			# exit the program
			li $v0, 10
			syscall
