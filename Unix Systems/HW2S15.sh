#NAME: Jon-Paul Kasper
#SERIAL NUMBER: 15
#FALL 2019
#CS 4350 - Unix Systems Programming   Section #: 001
#Assignment Number: 2
#Due Date: 09/25/2019

#!/bin/sh

# Introduction of the script to explain how the script runs
echo "NAME: Jon-Paul Kasper"
echo ; echo "Serial Number: 15"
echo ; echo "CS 4350 - Unix Systems Programming"
echo ; echo "Assignment Number: 2"
echo ; echo "Due Date: 9/23/2019"
echo ; echo "The function of this script is to:"
echo ; echo
echo "1. The integer arguments that are entered."
echo "2. Sum of the 3 integer arguments."
echo "3. Product of the 3 integer arguments."
echo "4. Average of the 3 integer arguments."
echo "5. Square of each integer argument."
echo "6. Determine that each integer argument is positive, negative, or zero."
echo "7. Determine that each integer argument is odd, or even"
echo "8. Find that all odd and even numbers between 1 and the second integer argument."
echo "9. Find the factorial of the first integer argument."
echo "10.Determine whether or not the third integer argument is a prime number."
echo ; echo ; echo

# Print the list of arguments passed from the command line
echo "1) The numbers are $*" 
echo

# Sum all of the arguments (assumption of three arguments)
sum=$(expr $1 + $2 + $3)
echo "2) $1 + $2 + $3 = " $sum
echo

# Multiple of all of the arguments (assumption of three arguments)
mul=$(expr $1 \* $2 \* $3)
echo "3) $1 * $2 * $3 = " $mul
echo

# Average of all of the arguments (assumption of three arguments)
avg=$(expr $sum / 3)
echo "4) ($1 + $2 + $3)/3 = " $avg
echo

# Square of every argument (assumption of three arguments)
sqr1=$(expr $1 \* $1)
sqr2=$(expr $2 \* $2)
sqr3=$(expr $3 \* $3)
echo "5) $1 * $1 = $sqr1 , $2 * $2 = $sqr2 , $3 * $3 = $sqr3"
echo

# Calculation and loop to determine if each argument in the list of all 
# arguments is positive, negative, or zero
declare -a arr=("$@")
len=${#arr[@]}
echo -n "6) "
for ((i=0 ; i < $len ; i++))
do
   if [ ${arr[$i]} -gt 0 ]
   then
      echo -n "${arr[$i]} is positive"
   elif [ ${arr[$i]} -lt 0 ]
   then
      echo -n "${arr[$i]} is negative"
   else
      echo -n "${arr[$i]} is zero"
   fi
   if [ "$i" -lt $(expr $len - 1) ]
   then
      echo -n " , "
   else
      echo "."
   fi
done
echo

# Calculation and loop to determine if each argument in the list of all 
# arguments is odd, even, or zero
echo -n "7) "
for ((i=0 ; i < $len ; i++))
do
   if [ $(expr ${arr[$i]} % 2) -gt 0 ]
   then
      echo -n "${arr[$i]} is odd"
   elif [ ${arr[$i]} -eq 0 ] 
   then
      echo -n "${arr[$i]} is zero"
   elif [ ${arr[$i]} == 1 ] || [ ${arr[$i]} == -1 ]
   then
      echo -n "${arr[$i]} is odd"
   else
      echo -n "${arr[$i]} is even"
   fi
   if [ "$i" -lt $(expr $len - 1) ]
   then
      echo -n " , "
   else
      echo "."
   fi
done
echo

# Calculate and loop to print the list of all even and odd numbers from 1 to 
# the value of the second argument(non inclusive)
if [ $2 -gt 0 ]
then
   echo "8) All the odd numbers from 1 to $2 are: "
   echo
   for ((i=2 ; i < $2 ; i++))
   do
      if [ $(expr $i % 2) -ne 0 ]
      then
         echo -n "$i "
      fi
   done
   echo ; echo
   echo "8) All the even numbers from 1 to $2 are: "
   echo
   for ((i=0 ; i < $2 ; i++))
   do
      if [ $i -lt 2 ]
      then
         continue
      fi
      if [ $(expr $i % 2) -eq 0 ]
         then
            echo -n "$i "
      fi
   done
   echo ; echo
elif [ $2 -eq 0 ]
then
   echo -n "8) The argument is 0 therefore there are no evens or odds from 1 "
   echo "to this argument."
   echo
elif [ $2 -lt 0 ]
then
   echo -n "8) The argument is negative therefore there are no evens or odds "
   echo "from 1 to this argument."
   echo
fi

# Calculate and loop to find the factorial of the first argument
fac=1
if [ $1 -gt 0 ]
then
   num1=$1
   echo -n "9) The factorial of $1 is: "
   while [ $num1 -gt 1 ]
   do
      fac=$((fac * num1))
      num1=$((num1 - 1))
   done
   echo $fac
elif [ $1 -lt 0 ]
then
   num1=$1
   echo -n "9) The factorial of $1 is: "
   while [ $num1 -lt -1 ]
   do
      fac=$((fac * num1))
      num1=$((num1 + 1))
   done
   echo $fac
elif [ $1 -eq 0 ]
then
   echo "9) The factorial of $1 is: 1"
fi
echo

# Calculate and loop to check if the third argument is a prime
if [ $3 -lt 0 ]
then
   echo "10) The argument is negative and therefore not a prime."
else
   num1=$(expr $3 \/ 2)
   if [ $3 -eq 1 ]
   then
      echo "10) $3 is a prime."
   elif [ $num1 -eq 0 ]
   then
      echo "10) The argument is zero and therefore not a prime."
   elif [ $num1 -eq 1 ]
   then
      echo "10) $3 is a prime."
   else
      for ((i=2 ; i <= num1 ; i++))
      do
         if [ $(expr $3 % $i) -eq 0 ]
         then
            echo "10) $3 is not a prime."
            break
         elif [ $i == $num1 ]
         then
            echo "10) $3 is a prime."
            break
         fi
      done
   fi
fi
echo ; echo ; echo

# Footer for the script
echo "End of script"
echo
echo "Implemented by Jon-Paul Kasper - 09 - 25 - 2019"
echo

exit 0
