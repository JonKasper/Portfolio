// Specification file for the IntStack class
// Adapted from Gaddis source code

class IntStack
{
private:
    struct Node{
         int data;
         Node* next;
    };
    Node* head; //ptr to top

public:
    // Constructor
    IntStack();

    //Destructor
    ~IntStack();

    // Stack operations
    void push(int);
    int pop();
    bool isFull();
    bool isEmpty();
};
