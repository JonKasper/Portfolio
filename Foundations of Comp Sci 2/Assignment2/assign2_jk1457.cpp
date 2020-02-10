// File Name: assign2_jk1457.cpp
//
// Author: Jon-Paul Kasper
// Date: 02/15/2018
// Assignment Number: 2
// CS 2308.262 Spring 2018
// Instructor: Yijuan Lu
//
// Reads in a store's inventory from a file, organizes the data, and produces
// a menu for the user to navigate. The user has the choic to display the
// inventory sorted by SKU, look up a product by SKU or name, or quit.
// Outputs a menu for navigation and, depending on the user input, the whole
// inventory after it has been sorted, or a single product determined by SKU
// or name.

#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

struct Inventory{
    string productName;
    int skuNum;
    int quantity;
    double price;
};

const int MAXSIZE = 100;

void readFile(ifstream&, Inventory[], int&);
void sortData(Inventory[], int);
int searchData(Inventory[], int, int, string, bool);    //Overloaded function
void showResult(Inventory[], int, bool);                //Overloaded function

int main()
{
    int size = 1, choice, sku_choice, location;
    bool binarySearch, showLabel;
    string str_choice = "NONE";
    char exitChoice;

    ifstream inputFile;
    inputFile.open("inventory.dat");

    if(!inputFile)
    {
        cout << "File failed to open. Terminating program." << endl;
        return -1;
    }

    Inventory store[MAXSIZE];

    readFile(inputFile, store, size);
    sortData(store, size);

    do
    {
        cout << "\nInventory Management: " << endl << endl;
        cout << "1. Display Inventory sorted by SKU" << endl;
        cout << "2. Look up product by SKU" << endl;
        cout << "3. Look up product by name" << endl;
        cout << "4. Quit" << endl << endl;
        cout << "Enter your choice: >";
        
        cin >> choice;

        switch(choice){
           
        case 1:   showLabel = false;
                  
                  cout << endl;
                  for(int i = 0; i < size; i++)
                  {
                      showResult(store, i, showLabel);
                      cout << endl;
                  }

                  cout << endl;
                  break;
            
        case 2:   do
                  {
                      cout << "Enter the SKU of product to find: >";
                      cin >> sku_choice;
                      cout << endl;
                  
                      binarySearch = true;   //Use binary search

                      location = searchData(store, size, sku_choice, str_choice,
                                            binarySearch);
                      if(location != -1)
                      {
                          showLabel = true;
                          showResult(store, location, showLabel);
                          cout << endl;
                      }
                      else
                          cout << "ERROR: SKU not found.\n\n";
                  
                      cout << "Would you like to look for another(y/n)? >";
                      cin >> exitChoice;
                  }while(exitChoice != 'n');

                  break;

        case 3:   do
                  {
                      cout << "Enter the name of product to find: >";
                      cin >> str_choice;
                  
                      binarySearch = false;   //Don't use binary search
                  
                      location = searchData(store, size, sku_choice, str_choice,
                                            binarySearch);

                      if(location != -1)
                      {
                          showLabel = true;
                          cout << endl;
                          showResult(store, location, showLabel);
                          cout << endl;
                      }
                      else
                          cout << "ERROR: Product not found. Please check"
                               << " spelling and try again.\n\n";

                      cout << "Would you like to look for another(y/n)? >";
                      cin >> exitChoice;
                  }while(exitChoice != 'n');

                  break;

        case 4:   cout << "Quitting...\n\n";
                  break;

        default:  cout << "Invalid choice. Returning to menu.\n\n";
                  break;
        } 
    }while(choice != 4);

    inputFile.close();
   
    return 0;
}

//*****************************************************************************
// readFile: reads in the information from the file and stops at the end of 
//           the file or when the info read reaches the max size.
//
// inputFile: the file that holds the information being read.
// store: array of type Inventory that holds the product name, sku number,
//        quantity, and price of each product.
// size: the number of inventory being read in
// returns: no return
//*****************************************************************************

void readFile(ifstream &inputFile, Inventory store[], int &size)
{
    int count = 0;

    while(inputFile && count <= MAXSIZE)
    {
        getline(inputFile, store[count].productName);
        inputFile >> store[count].skuNum;
        inputFile >> store[count].quantity;
        inputFile >> store[count].price;
        inputFile.ignore();

        count++;
    }

    size = count - 1;
}

//*****************************************************************************
// sortData: sorts the data that was read in using the selection sort algorithm
//
// store: array of type Inventory that holds the product name, sku number,
//        quantity, and price of each product.
// size: the number of inventory that was read in
// returns: no return
//*****************************************************************************

void sortData(Inventory store[], int size)
{
    string nameTemp;
    int skuTemp;
    int quantityTemp;
    double priceTemp;

    int startScan, minIndex, minValue;

    for(startScan = 0; startScan < (size - 1); startScan++)
    {
        minIndex = startScan;
        minValue = store[startScan].skuNum;

        for(int i = startScan + 1; i < size; i++)
        {
            if(store[i].skuNum < minValue)
            {
                nameTemp = store[i].productName;
                skuTemp = store[i].skuNum;
                quantityTemp = store[i].quantity;
                priceTemp = store[i].price;

                minIndex = i;
            }
        }

        if(minIndex != startScan)
        {        
            store[minIndex].productName = store[startScan].productName;
            store[startScan].productName = nameTemp;

            store[minIndex].skuNum = store[startScan].skuNum;
            store[startScan].skuNum = skuTemp;

            store[minIndex].quantity = store[startScan].quantity;
            store[startScan].quantity = quantityTemp;

            store[minIndex].price = store[startScan].price;
            store[startScan].price = priceTemp;
        }            
    }
}

//*****************************************************************************
// searchData: searches the data stored using either a binary search or linear
//             search dependant on the value of sort
// store: array of type Inventory that holds the product name, sku number,
//        quantity, and price of each product.
// size: the number of inventory that was read in
// search: the sku number that is being searched for
// strSearch: the name of the product that is being searched for
// sort: used to determine which type of search to use
//*****************************************************************************

int searchData(Inventory store[], int size, int search, string strSearch,
               bool sort)
{
    if(sort == true)
    {
        int start = 0, end = (size - 1), middle, position = -1;
        bool found = false;

        while(!found && start <= end)
        {
            middle = (start + end) / 2;
            if(store[middle].skuNum == search)
            {
                found = true;
                position = middle;
            }
            else if(store[middle].skuNum > search)
                end = middle - 1;
            else
                start = middle + 1;
        }
        return position;
    }
    else
    {
        bool found = false;
        for(int i = 0; i < size; i++)
        {
            if(store[i].productName == strSearch)
            {
                found = true;
                return i;
            }
        }
        
        if(found == false);
            return -1;
    }
}

//*****************************************************************************
// showResult: prints the inventory information with or without a label 
//             dependant on the value of label
// location: element of the array that needs to be printed
// label: used to determine whether to print labelled or unlabelled 
//*****************************************************************************

void showResult(Inventory store[], int location, bool label)
{
    if(label == false)
    {
        cout << right << showpoint << fixed << setprecision(2);
        cout << setw(6) << store[location].skuNum
             << setw(4) << store[location].quantity
             << setw(8) << store[location].price
             << left << "  " << store[location].productName;
    }
    else
    {
        cout << right << showpoint << setprecision(2) << fixed;
        cout << "Product Name: " << setw(20) << store[location].productName
             << endl;
        cout << "SKU: " << setw(29) << store[location].skuNum << endl;
        cout << "Quantity: " << setw(24) << store[location].quantity << endl;
        cout << "Price: " << setw(27) << store[location].price << endl;
    }
}
