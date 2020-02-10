# !bin/bash

# chmods all files into executables

shopt -s nullglob

filearray=( *.sh* )

echo "chmoding all files in current directory..."

for i in "${filearray[@]}"
do
	echo -n "$i"
	chmod -x "$i"
	echo " non-executable"
done

exit 0
