#################################################
# CS-2318 demo program 02
#########################
# Key takeaways:
# - how to declare & initialize global char & int variables (in memory)
# - how to declare & initialize global char & int arrays (in memory)
# - how to use load to retrieve value (in memory) of a particular array element
# - how to use store to put away value (in register) to a particular array element
# - how to retrieve value (in memory) from or put away value (in register) to a memory variable
#   (simply treat memory variable as if it is 1-element array)
# - how to "painlessly" swap contents (in memory) of 2 array elements - w/ 2 registers as temps
# - be warned: "no pointer arithmetic in assembly" & related "address not aligned" fatal errors
# - see a case where it matters to distinguish between sra (sign-extend) & srl (zero-extend)
#################################################
			.data
oneChar:		.byte 'K'		# global char var (treat as if global char
 			 			#   array of size 1 when accessing)
charArr:		.byte 'A', 'B', 'C'	# global char array of size 3 initialized
 			 			#   to 'A', 'B' & 'C' (from 1st to 3rd)
oneInt:			.word -31		# global int var (treat as if global int
 			 			#   array of size 1 when accessing)
intArr:			.word 2, 3, 1, 8	# global int array of size 4 initialized
			 			#   to 2, 3, 1 & 8 (from 1st to 4th)
			.text
			.globl main
main:
			la $t0, oneChar		# $t0 has address of oneChar
			li $v0, 11		# prep to-print-char system service
			lb $a0, 0($t0)		# $a0 has oneChar[0] (should be 'K')
			syscall			# should print 'K'
			ori $a0, $a0, 0x20	# lower case of char in $a0
			 			#   (doesn't change oneChar[0])
			#xori $a0, $a0, 0x20	# how-it'd-be aside: toggle case of char in $a0 
			syscall			# should print 'k'
			
			sb $a0, 0($t0)		# put "char in $a0" to oneChar[0] in memory
			 			#   (need to STORE to have side effect on memory)			 			
			lb $a0, 0($t0)		# reload content of oneChar[0] in memory into $a0
			syscall			# should print 'k'
			andi $a0, $a0, 0xDF	# raise case of char in $a0
			syscall			# should print 'K'
			xori $a0, $a0, 0x20	# toggle case of char in $a0
			syscall			# should print 'k'

			li $v0, 11
			li $a0, '\n'
			syscall 		# print newline (for readability)			
			
			la $t0, charArr		# $t0 has address of charArr
			lb $a0, 0($t0)		# $a0 has charArr[0]
			syscall			# should print 'A'
			lb $a0, 1($t0)		# $a0 has charArr[1]
			syscall			# should print 'B'
			lb $a0, 2($t0)		# $a0 has charArr[2]
			syscall			# should print 'C'
			li $a0, '\n'
			 			# print newline (for readability)
			
 			# BEGIN_(swapping charArr[0] & charArr[2] in memory)
			lb $t1, 0($t0)
			lb $t3, 2($t0)
			#sb $t3, 0($t0)		# can-also-do aside: this & next can replace   
			#sb $t1, 2($t0)		#   following 2 to achieve the same effect
			sb $t1, 2($t0)
			sb $t3, 0($t0)
 			# END_(swapping charArr[0] & charArr[2] in memory)
			
			li $v0, 11		# prep to-print-char system service
			lb $a0, 0($t0)		# $a0 has charArr[0]
			syscall			# should print 'C'
			lb $a0, 1($t0)		# $a0 has charArr[1]
			syscall			# should print 'B'
			lb $a0, 2($t0)		# $a0 has charArr[2]
			syscall			# should print 'A'
			li $a0, '\n'
			syscall

			###################################
			
			la $t0, oneInt		# $t0 has address of oneInt
			li $v0, 1		# prep to-print-int system service
			lw $a0, 0($t0)		# $a0 has oneInt[0] (should be -31)
			syscall			# should print -31
			sll $a0, $a0, 2		# $a0 = $a0 * 2^2 (via bitwise shift left)
			syscall			# should print -124 (= -31 * 4)
			sra $a0, $a0, 2		# $a0 = $a0 / 2^2 (via bitwise shift right)
			#srl $a0, $a0, 2	# ¿same? aside: 0-extends, changes sign, nah
			syscall			# should print -31 (= -124 / 4)

			li $v0, 11
			li $a0, '\n'
			syscall
									
 			# BEGIN_(swapping intArr[0] & intArr[2] in memory)
			la $t0, intArr		# $t0 has address of intArr
			lw $t1, 0($t0)		# $t1 has oneInt[0] (should be 2)
			#lw $t3, 2($t0)		# caveat aside: ¡load address not aligned!
			lw $t3, 8($t0)		# $t3 has oneInt[2] (should be 1)
			
			## BEGIN_(print extra to show intArr[0] & intArr[2] just loaded)
			li $v0, 1
			move $a0, $t1		# should print 2
			syscall
			move $a0, $t3		# should print 1
			syscall
			## END_(print extra to show intArr[0] & intArr[2] just loaded)
			
			sw $t3, 0($t0)		# put "int in $t3" to intArr[0] in memory
			sw $t1, 8($t0)		# put "int in $t1" to intArr[2] in memory
 			# END_(swapping intArr[0] & intArr[2] in memory)

			li $v0, 11
			li $a0, '\n'
			syscall

			li $v0, 1
			lw $a0, 0($t0)		# reload content of intArr[0] in memory into $a0
			syscall			# should print 1
			lw $a0, 8($t0)		# reload content of intArr[2] in memory into $a0
			syscall			# should print 2
			
			li $v0, 10		# graceful exit
			syscall
#################################################
						
			
