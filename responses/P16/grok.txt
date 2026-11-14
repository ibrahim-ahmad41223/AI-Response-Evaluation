```cpp
#include <iostream>
using namespace std;

class CircularDeque {
private:
    int* arr;       // fixed-size array
    int capacity;   // maximum size
    int front;      // index of front element
    int rear;       // index of rear element
    int count;      // current number of elements

public:
    // Constructor
    CircularDeque(int size) {
        capacity = size;
        arr = new int[capacity];
        front = -1;
        rear = -1;
        count = 0;
    }

    // Destructor
    ~CircularDeque() {
        delete[] arr;
    }

    // Check if empty
    bool isEmpty() const {
        return count == 0;
    }

    // Check if full
    bool isFull() const {
        return count == capacity;
    }

    // Insert at front
    bool insertFront(int value) {
        if (isFull()) {
            cout << "Deque is full. Cannot insert " << value << " at front.\n";
            return false;
        }

        if (isEmpty()) {
            front = rear = 0;
        } else {
            front = (front - 1 + capacity) % capacity;
        }

        arr[front] = value;
        count++;
        return true;
    }

    // Insert at rear
    bool insertRear(int value) {
        if (isFull()) {
            cout << "Deque is full. Cannot insert " << value << " at rear.\n";
            return false;
        }

        if (isEmpty()) {
            front = rear = 0;
        } else {
            rear = (rear + 1) % capacity;
        }

        arr[rear] = value;
        count++;
        return true;
    }

    // Delete from front
    bool deleteFront() {
        if (isEmpty()) {
            cout << "Deque is empty. Cannot delete from front.\n";
            return false;
        }

        cout << "Deleted from front: " << arr[front] << endl;

        if (front == rear) {          // only one element
            front = rear = -1;
        } else {
            front = (front + 1) % capacity;
        }

        count--;
        return true;
    }

    // Delete from rear
    bool deleteRear() {
        if (isEmpty()) {
            cout << "Deque is empty. Cannot delete from rear.\n";
            return false;
        }

        cout << "Deleted from rear: " << arr[rear] << endl;

        if (front == rear) {          // only one element
            front = rear = -1;
        } else {
            rear = (rear - 1 + capacity) % capacity;
        }

        count--;
        return true;
    }

    // Display the deque
    void display() const {
        if (isEmpty()) {
            cout << "Deque is empty.\n";
            return;
        }

        cout << "Deque contents (front to rear): ";
        int i = front;
        for (int c = 0; c < count; c++) {
            cout << arr[i] << " ";
            i = (i + 1) % capacity;
        }
        cout << endl;
    }

    // Search for a value; returns the logical position (0-based from front)
    // or -1 if not found
    int search(int value) const {
        if (isEmpty()) {
            return -1;
        }

        int i = front;
        for (int pos = 0; pos < count; pos++) {
            if (arr[i] == value) {
                return pos;           // position relative to front
            }
            i = (i + 1) % capacity;
        }
        return -1;
    }

    // Optional helper: current size
    int size() const {
        return count;
    }
};

// Example usage
int main() {
    CircularDeque dq(5);   // capacity = 5

    dq.insertRear(10);
    dq.insertRear(20);
    dq.insertFront(5);
    dq.insertFront(1);
    dq.insertRear(30);

    dq.display();

    cout << "Search 20 -> position: " << dq.search(20) << endl;
    cout << "Search 99 -> position: " << dq.search(99) << endl;

    dq.deleteFront();
    dq.deleteRear();
    dq.display();

    dq.insertFront(100);
    dq.insertRear(200);
    dq.display();

    // Destructor is called automatically when dq goes out of scope
    return 0;
}
```

### Key points of the implementation

- Uses a fixed-size circular array (`arr`) with modulo arithmetic for wrapping.
- Tracks `front`, `rear`, and `count` so both ends can be managed efficiently in O(1) time.
- `insertFront` / `insertRear` and `deleteFront` / `deleteRear` all handle the empty and full cases correctly.
- `display()` walks the circular buffer from front to rear.
- `search()` returns the 0-based position relative to the front (or -1 if not found).
- The destructor properly releases the dynamically allocated array.