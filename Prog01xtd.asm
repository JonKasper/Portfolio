# Prog01xtd.asm
			.data
name:			.space 21			
howdy:			.asciiz "howdy!"
eyaPrmpt:		.asciiz "Enter age: "
yaiLab:			.asciiz "Your age is "
eygPrmpt:		.asciiz "Enter gender: "
ygiLab:			.asciiz "Your gender is "
eynPrmpt:		.asciiz "Enter name: "
yniLab:			.asciiz "Your name is "
########################
codeLab:		.asciiz "Your secret code is "	
########################

			.text
			.globl main
main:
			li $v0,4
			la $a0, howdy
			syscall
			
			li $v0, 11
			li $a0, '\n'
			syscall
			
			li $v0,4
			la $a0, eyaPrmpt
			syscall
			li $v0,5
			syscall
			move $t0, $v0			# copy integer read (in $v0) to $t0
			#add $t0, $v0, $0		# (can do this for same copy effect)
			#addi $t0, $v0, 0		# (can do this for same copy effect)
			#sub $t0, $v0, $0		# (can do this for same copy effect)
			#and $t0, $v0, $v0		# (can do this for same copy effect)
			#or $t0, $v0, $v0		# (can do this for same copy effect)
			#andi $t0, $v0, 0xFFFFFFFF	# (can do this for same copy effect)
			#ori $t0, $v0, 0		# (can do this for same copy effect)
			#xori $t0, $v0, 0x0		# (can do this for same copy effect)
########################
			move $t1, $t0		# $t1 has copy of age for secret code play
########################
			li $v0,4
			la $a0, yaiLab
			syscall
			li $v0,1
			move $a0, $t0
			syscall
			
			li $v0, 11
			li $a0, '\n'
			syscall
			
			li $v0,4
			la $a0, eygPrmpt
			syscall
			li $v0,12
			syscall
			move $t0, $v0
			
			li $v0, 11
			li $a0, '\n'
			syscall
			
			li $v0,4
			la $a0, ygiLab
			syscall
			li $v0,11
			move $a0, $t0
			#andi $a0, $t0, 0xDF	# copy uppercase-forced $t0 to $a0
			#ori $a0, $t0, 0x20	# copy lowercase-forced $t0 to $a0
			#xori $a0, $t0, 0x20	# copy case-toggled $t0 to $a0
			syscall
			
			li $v0, 11
			li $a0, '\n'
			syscall
			
			li $v0,4
			la $a0, eynPrmpt
			syscall
			li $v0, 8
			la $a0, name
			li $a1, 21
			syscall

			#lb $t0, 0($a0)		# load name[0] into $t0
			#andi $t0, $t0, 0xDF	# force $t0 to uppercase
			#sb $t0, 0($a0)		# store $t0 (uppercase forced) to name[0]
						
			li $v0, 11
			li $a0, '\n'
			syscall
			
			li $v0,4
			la $a0, yniLab
			syscall
			#li $v0,4
			la $a0, name
			syscall

########################
			li $v0, 11
			li $a0, '\n'
			syscall			

# Formula for secret code: (4/3)*age*age + (2345/512)*age - 31
			
			mult $t1, $t1		# Lo has lower-32 bits of age*age
			mflo $t9		# $t9 has age*age
			sll $t9, $t9, 2		# $t9 has 4*age*age
			li $t0, 3		# $t0 has 3
			div $t9, $t0		# Lo has 4*age*age/3
			mflo $t9		# $t9 has 4*age*age/3
			################
			li $t0, 2345		# $t0 has 2345
			mul $t0, $t0, $t1	# $t0 has lower-32 bits of 2345*age
			sra $t0, $t0, 9		# $t0 has 2345*age/512
			################
			add $t9, $t9, $t0	# $t9 has 4*age*age/3 + 2345*age/512
			addi $t9, $t9, -31	# $t9 has has 4*age*age/3 + 2345*age/512 - 31
			################
			li $v0, 4
			la $a0, codeLab
			syscall
			li $v0, 1
			move $a0, $t9
			syscall
			li $v0, 11
			li $a0, '\n'
			syscall			
########################
						
			li $v0, 10
			syscall
			
