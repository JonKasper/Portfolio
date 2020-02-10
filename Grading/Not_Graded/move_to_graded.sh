#!/bin/bash

#moves the graded assignments to the Graded folder

shopt -s nullglob

filearray=( *test* )

echo "Moving graded files..."

for i in "${filearray[@]}"
do
	mv "$i" /home/Students/jk1457/Grading/Graded/
	echo "$i moved to Graded"
done

exit 0
