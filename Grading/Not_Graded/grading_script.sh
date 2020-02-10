#!/bin/bash

# method to catch failure codes for programs

if [ -f rundoc.txt ]
then
	echo "Documentation of previous runs exists. Deleting..."
	rm rundoc.txt
fi

if [ -f errordoc.txt ]
then
	echo "Documentation of previous errors exists. Deleting..."
	rm errordoc.txt
fi

shopt -s nullglob

echo "Running grading script..." 
echo ; echo 

filearray=( *.c* )

echo -n "filearray length: "
echo "${#filearray[@]}"

for i in "${filearray[@]}"
do
	echo "$i" >> rundoc.txt
	echo >> rundoc.txt
	
	#compile and run the shell programs
#	sh ./"$i" >> rundoc.txt 2>> errordoc.txt

	#compile and run the C programs
	if [ -f a.out ]
	then
		rm a.out
	fi

	gcc "$i" 2>> errordoc.txt
	if [ -f a.out ]
	then
		./a.out >> rundoc.txt 2>> errordoc.txt
	fi

	if [ $? -eq 0 ]
	then
		echo
		echo -n "$i"
		echo " Run Success"
		echo
	else
		echo
		echo -n "$i"
		echo " Run Failure"
		echo
	fi

	echo >> rundoc.txt
	echo >> rundoc.txt
	echo >> rundoc.txt

	check=$(wc -c errordoc.txt)
	if [[ $check > 0 ]]
	then
		echo >> errordoc.txt
		echo >> errordoc.txt
		echo >> errordoc.txt
	fi
done

exit 0
