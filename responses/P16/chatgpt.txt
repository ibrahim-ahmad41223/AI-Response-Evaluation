Here is a beginner-friendly C++ implementation of a **Double-Ended Circular Queue (Deque)** using a fixed-size integer array.

It supports:

- Insert at front
- Insert at rear
- Delete from front
- Delete from rear
- Display elements
- Search for an element
- Destructor

## **Complete C++ Program**

```

#include <iostream>
using namespace std;

class Deque {
private:
    int arr[5];
    int front, rear;
    int size;

public:
    Deque() {
        front = -1;
        rear = -1;
        size = 5;
    }

    // Insert at front
    void insertFront(int value) {
        if ((front == 0 && rear == size - 1) || (front == rear + 1)) {
            cout << "Deque is Full\n";
            return;
        }

        if (front == -1) {
            front = rear = 0;
        }
        else if (front == 0) {
            front = size - 1;
        }
        else {
            front--;
        }

        arr[front] = value;
    }

    // Insert at rear
    void insertRear(int value) {
        if ((front == 0 && rear == size - 1) || (front == rear + 1)) {
            cout << "Deque is Full\n";
            return;
        }

        if (front == -1) {
            front = rear = 0;
        }
        else if (rear == size - 1) {
            rear = 0;
        }
        else {
            rear++;
        }

        arr[rear] = value;
    }

    // Delete from front
    void deleteFront() {
        if (front == -1) {
            cout << "Deque is Empty\n";
            return;
        }

        cout << "Deleted: " << arr[front] << endl;

        if (front == rear) {
            front = rear = -1;
        }
        else if (front == size - 1) {
            front = 0;
        }
        else {
            front++;
        }
    }

    // Delete from rear
    void deleteRear() {
        if (front == -1) {
            cout << "Deque is Empty\n";
            return;
        }

        cout << "Deleted: " << arr[rear] << endl;

        if (front == rear) {
            front = rear = -1;
        }
        else if (rear == 0) {
            rear = size - 1;
        }
        else {
            rear--;
        }
    }

    // Display elements
    void display() {
        if (front == -1) {
            cout << "Deque is Empty\n";
            return;
        }

        int i = front;

        cout << "Deque: ";

        while (true) {
            cout << arr[i] << " ";

            if (i == rear)
                break;

            i = (i + 1) % size;
        }

        cout << endl;
    }

    // Search element
    void search(int value) {
        if (front == -1) {
            cout << "Deque is Empty\n";
            return;
        }

        int i = front;

        while (true) {
            if (arr[i] == value) {
                cout << "Element found at index " << i << endl;
                return;
            }

            if (i == rear)
                break;

            i = (i + 1) % size;
        }

        cout << "Element not found\n";
    }

    // Destructor
    ~Deque() {
        cout << "Deque destroyed\n";
    }
};

int main() {
    Deque d;

    d.insertRear(10);
    d.insertRear(20);
    d.insertRear(30);

    d.insertFront(5);
    d.insertFront(1);

    d.display();

    d.search(20);

    d.deleteFront();
    d.deleteRear();

    d.display();

    return 0;
}

```

## **Important concepts**

**1. Front and Rear**

- `front` points to the first element.
- `rear` points to the last element.
- Both are initialized to `-1`, meaning the deque is empty.

**2. Circular movement**

The modulo operator `%` allows the index to return to zero after reaching the last array position.

For example:

```
i = (i + 1) % size;
```

**3. Full condition**

The deque is full when:

```
(front == 0 && rear == size - 1) || (front == rear + 1)
```

**4. Empty condition**

```
front == -1
```

**5. Destructor**

The destructor automatically executes when the deque object goes out of scope. Since this implementation uses a fixed-size array, no dynamic memory needs to be released.

## **Sample output**

```
Deque: 1 5 10 20 30
Element found at index 3
Deleted: 1
Deleted: 30
Deque: 5 10 20
Deque destroyed
```

Time complexity

| Operation    | Complexity |
| ------------ | ---------- |
| Insert Front | O(1)       |
| Insert Rear  | O(1)       |
| Delete Front | O(1)       |
| Delete Rear  | O(1)       |
| Display      | O(n)       |
| Search       | O(n)       |

**Remember:** A deque allows insertion and deletion from both ends, unlike a normal queue where insertion happens at the rear and deletion happens at the front.