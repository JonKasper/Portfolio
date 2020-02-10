#!/bin/sh
# This program uses a menu to perform file and directory manipulation.

echo
echo "CS 4350 - Unix Systems Programming"
echo
echo "NAME: Jon-Paul Kasper"
echo "Serial Number: 15"
echo
echo "Functions and Arrays"
echo
echo "Assignment Number: 3"
echo "Due Date: 10/7/2019"
echo ; echo
echo "The function of this script is to:"
echo "   1. List detailed list of all files in your directory. "
echo "      Redirect the output to zlsCommandFiles.txt"
echo "   2. Create directory by checking its existence"
echo "   3. Test if File Exist."
echo "   4. Append \"Learning Scripts and Shell Programming\" to "
echo "      an existing File. "
echo "   5. Rename an existing File"
echo "   6. Delete an existing File"
echo "   7. Delete an existing Directory"
echo "   8. Parse Current Date"
echo "   9. Display a calendar for a specific month / year"
echo ; echo
echo "   15. Exit"
echo ; echo ; echo

# Outputs a detailed list of all files in the current directory
# to a text file
printListFunc()
{
   if [ ! -f zlsCommandFiles.txt ]
   then 
      ls -a > zlsCommandFiles.txt
      echo "zlsCommandFiles.txt is created"
   else
      echo "zlsCommandFiles.txt already exists. Overriding..."
      ls -a > zlsCommandFiles.txt
   fi
}

# Checks if a directory exists and if it doesn't then creates
# the directory
dirCreateIfNotExist()
{
   if [ ! -d $1 ]
   then
      mkdir "$1"
      echo "Directory created: " $1
   else
      echo "Directory $1 exists."
   fi
}

# Prints the word and line count of a file if the file exists
# as well as the content of the file.
wordAndLineCountIfFileExists()
{
   if [ ! -f $1 ]
   then
      echo "$1 is not a file."
      touch $1
      echo "File created: " $1
   else
      count[0]=$(wc -l < $1)
      count[1]=$(wc -w < $1)
      echo "Number of lines and words: " ${count[*]}
      echo
      echo "File Content"
      echo
      cat $1
   fi
}

# Appends a string to the end of a file if the file exists
appendIfFileExists()
{
   if [ -f $1 ]
   then
      echo
      echo "File Content Before Append"
      echo
      cat $1
      echo
      echo "File Content After Append"
      echo
      echo "Learning Scripts and Shell Programming" >> $1
      echo
      cat $1
   else
      echo
      echo "The file $1 does not exist."
      echo
   fi
}

# Renames a file if the file exists
renameIfFileExists()
{
   if [ ! -f $1 ]
   then
      echo "File $1 does not exist"
   else
      file=$1
      mv $1 $2
      echo "$file is renamed to $2"
   fi
}

# Deletes a file if the file exists
deleteIfFileExists()
{
   if [ ! -f $1 ]
   then
      echo "File $1 does not exist"
   else
      file=$1
      rm $1
      echo "$file is Deleted"
   fi
}

# Deletes a directory if the directory exists
deleteIfDirExists()
{
   if [ ! -d $1 ]
   then
      echo "Directory $1 does not exist"
   else
      directory=$1
      rmdir $1
      echo "$directory is Deleted."
   fi
}

# Prints the current date and time formatted
parseCurrentDate()
{
   echo -n "Current Date: "
   date +"%a %b %d"
   echo -n "Current Time: "
   date +"%l:%M:%S"
}

# Displays the calendar for a specific month and year.
displayCalendar()
{
   cal $1 $2
}


# beginning of the main script

choice=0

# loop for the program to operate

while [ ! $choice -eq 15 ]
do
   echo -n "Enter your choice: "
   read choice

   case "$choice" in
      1)
         echo
         printListFunc
         echo ; echo
         ;;
      2)
         echo
         echo -n "Enter the name of the directory: "
         read directory
         echo
         dirCreateIfNotExist $directory
         echo ; echo
         ;;
      3)
         echo
         echo -n "Enter file name: "
         read fileName
         echo
         wordAndLineCountIfFileExists $fileName
         echo ; echo
         ;;
      4)
         echo
         echo -n "Enter file name: "
         read fileName
         echo
         appendIfFileExists $fileName
         echo ; echo
         ;;
      5)
         echo
         echo -n "Enter file to be renamed: "
         read oldName
         echo
         echo -n "Enter the new name: "
         read newName
         echo 
         renameIfFileExists $oldName $newName
         echo ; echo
         ;;
      6)
         echo
         echo -n "Enter the name of file to be deleted: "
         read fileName
         echo
         deleteIfFileExists $fileName
         echo ; echo
         ;;
      7)
         echo
         echo -n "Enter the name of the directory to be deleted: "
         read dirName
         deleteIfDirExists $dirName
         echo ; echo
         ;;
      8)
         echo
         parseCurrentDate
         echo ; echo
         ;;
      9)
         echo
         echo -n "Enter month: "
         read month
         echo
         echo -n "Enter year: "
         read year
         echo
         displayCalendar $month $year
         echo
         ;;
      15)
         echo
         echo "Jon-Paul Kasper - 10-7-2019"
         echo
         ;;
      *)
         echo
         echo "Invalid choice"
         echo
         ;;
   esac
done
exit 0
