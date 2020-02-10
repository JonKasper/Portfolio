// File Name: assign1_jk1457.cpp
//
// Author: Jon-Paul Kasper
// Date: 01/28/2018
// Assignment Number: 1
// CS 2308.262 Spring 2018
// Instructor: Yijuan Lu
//
// Inititalizes an array of structures that contain information on employees
// in the company.
// Outputs the table of emplyee's name, age, and salary as well as the average
// age for all employees.

#include <iostream>
#include <iomanip>

using namespace std;

struct Employee{
    string name;
    int age;
    double salary;
};

double averageAge(Employee[], int);
int salarySort(Employee[], bool, int);

int main()
{
    const int MAXCOUNT = 9;
    bool highOrLow = true; // included to for switching between if and else
                           // cases in salarySort
    double average = 0.0;
    int highest = 0, lowest = 0;

    Employee info[] = {
        {"Ben", 25, 29},
        {"Fred", 58, 31},
        {"Mark", 40, 33},
        {"Tom", 65, 29},
        {"Kevin", 48, 31},
        {"William", 37, 23},
        {"Lucy", 62, 29},
        {"Katherine", 48, 44},
        {"Tiger", 27, 19}
    };

    average = averageAge(info, MAXCOUNT);
    highest = salarySort(info, highOrLow, MAXCOUNT);

    // switch highOrLow to false to use else case in salarySort
    highOrLow = false;
    lowest = salarySort(info, highOrLow, MAXCOUNT);

    for(int i = 0; i < MAXCOUNT; i++)
    {
        cout << setw(15) << left << info[i].name 
             << setw(7) <<  info[i].age
             << setw(7) << info[i].salary << endl;
    }

    cout << fixed << setprecision(1) << endl << endl;
    cout << "Average Age: " << average << endl;
    cout << setprecision(0);
    cout << "Employee with the highest salary: " << info[highest].name
         << " Salary: " << info[highest].salary << endl;
    cout << "Employee with the lowest salary: " << info[lowest].name
         << " Salary: " << info[lowest].salary << endl;

    return 0;
}

//******************************************************************************
// double averageAge: used to find the average age of the list of employees
//
// Employee info[]: array of structures with type Employee that is used to 
//                  hold employee name, age, and salary
// int MAXCOUNT: constant integer used to hold the maximum number of employees
//               in the list
// return: returns the average age of the entire list of employees
//******************************************************************************

double averageAge(Employee info[], int MAXCOUNT)
{
    double avg = 0.0, total = 0.0;

    for(int i = 0; i < MAXCOUNT; i++)
        total += info[i].age;

    avg = total / MAXCOUNT;

    return avg;
}

// *****************************************************************************
// int salarySort: used to find the highest and lowest salary amongst the list
//                 of employees.
//
// Employee info[]: array of structures with type Employee that is used to 
//                  hold employee name, age, and salary
// bool highOrLow: used to force salarSort to search for the highest or lowest
//                 salary amongst the employees
// int MAXCOUNT: constant integer used to hold the maximum number of employees
//               in the list
// return: returns the highest or lowest salary from the list of employees
//******************************************************************************

int salarySort(Employee info[], bool highOrLow, int MAXCOUNT)
{
    if(highOrLow == true)
    {
        int high = 0;
        for(int i = 1; i < MAXCOUNT; i++)
        {
            if(info[i].salary > info[high].salary)
                high = i;
        }
        return high;
    }
    else if(highOrLow == false)
    {
       int low = 0;
       for(int i = 1; i < MAXCOUNT; i++)
       {
           if(info[i].salary < info[low].salary)
               low = i;
       }
       return low;
    }
}
