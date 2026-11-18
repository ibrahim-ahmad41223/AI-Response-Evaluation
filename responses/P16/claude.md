I've written `circular_deque.cpp`, a `CircularDeque` class backed by a fixed-size `int` array, with a small `main()` that exercises every operation. I haven't compiled or run it.

- **Storage:** The class allocates the array once with `new int[capacity]` and never resizes it. The `count` member tells a full deque from an empty one, so no array slot is wasted.
- **Wrap-around:** Indices wrap with modular arithmetic. Inserting at the front moves `front` back by one, and inserting at the rear moves `rear` forward by one.
- **Insertion and deletion:** `insertFront`, `insertRear`, `deleteFront` and `deleteRear` all run in O(1). They print an overflow or underflow message and return `false` when the deque is full or empty. The deletes return the removed value through a reference parameter.
- **Extras:** `peekFront`, `peekRear`, `isEmpty`, `isFull` and `size`.
- **Display:** `display()` prints the elements from front to rear, following the wrap-around.
- **Search:** `search(value)` returns the 0-based position counted from the front, or `-1` if the value isn't there. It is O(n).
- **Destructor:** `~CircularDeque()` frees the array with `delete[]`. Copy construction and assignment are deleted, because copying the raw pointer would lead to a double free.

To build and run it: `g++ -std=c++11 circular_deque.cpp -o deque && ./deque`

#include <iostream>
using namespace std;

// Double-ended circular queue backed by a fixed-size integer array.
class CircularDeque {
private:
    int* arr;       // underlying fixed-size storage
    int capacity;   // maximum number of elements
    int front;      // index of the front element
    int rear;       // index of the rear element
    int count;      // current number of elements

public:
    explicit CircularDeque(int size)
        : arr(nullptr), capacity(size > 0 ? size : 1),
          front(0), rear(-1), count(0) {
        arr = new int[capacity];
    }

    // Destructor: release the array
    ~CircularDeque() {
        delete[] arr;
        arr = nullptr;
    }

    // Copying would double-delete the array, so it is disabled.
    CircularDeque(const CircularDeque&) = delete;
    CircularDeque& operator=(const CircularDeque&) = delete;

    bool isEmpty() const { return count == 0; }
    bool isFull()  const { return count == capacity; }
    int  size()    const { return count; }

    // Insert at the front
    bool insertFront(int value) {
        if (isFull()) {
            cout << "Overflow: deque is full, cannot insert " << value << " at front.\n";
            return false;
        }
        if (isEmpty()) {
            front = 0;
            rear = 0;
        } else {
            front = (front - 1 + capacity) % capacity;
        }
        arr[front] = value;
        count++;
        return true;
    }

    // Insert at the rear
    bool insertRear(int value) {
        if (isFull()) {
            cout << "Overflow: deque is full, cannot insert " << value << " at rear.\n";
            return false;
        }
        if (isEmpty()) {
            front = 0;
            rear = 0;
        } else {
            rear = (rear + 1) % capacity;
        }
        arr[rear] = value;
        count++;
        return true;
    }

    // Delete from the front; the removed value is returned via 'removed'
    bool deleteFront(int& removed) {
        if (isEmpty()) {
            cout << "Underflow: deque is empty, cannot delete from front.\n";
            return false;
        }
        removed = arr[front];
        front = (front + 1) % capacity;
        count--;
        if (isEmpty()) { front = 0; rear = -1; }
        return true;
    }

    // Delete from the rear; the removed value is returned via 'removed'
    bool deleteRear(int& removed) {
        if (isEmpty()) {
            cout << "Underflow: deque is empty, cannot delete from rear.\n";
            return false;
        }
        removed = arr[rear];
        rear = (rear - 1 + capacity) % capacity;
        count--;
        if (isEmpty()) { front = 0; rear = -1; }
        return true;
    }

    // Peek at the front / rear without removing
    bool peekFront(int& value) const {
        if (isEmpty()) return false;
        value = arr[front];
        return true;
    }

    bool peekRear(int& value) const {
        if (isEmpty()) return false;
        value = arr[rear];
        return true;
    }

    // Display elements from front to rear
    void display() const {
        if (isEmpty()) {
            cout << "Deque is empty.\n";
            return;
        }
        cout << "Deque (front -> rear): ";
        for (int i = 0; i < count; i++) {
            cout << arr[(front + i) % capacity] << " ";
        }
        cout << "\n";
    }

    // Search for a value. Returns its position counted from the front
    // (0-based), or -1 if not found.
    int search(int value) const {
        for (int i = 0; i < count; i++) {
            if (arr[(front + i) % capacity] == value) {
                return i;
            }
        }
        return -1;
    }
};

int main() {
    CircularDeque dq(5);
    int x;

    dq.insertRear(10);
    dq.insertRear(20);
    dq.insertFront(5);
    dq.insertFront(1);
    dq.insertRear(30);
    dq.display();               // 1 5 10 20 30

    dq.insertRear(40);          // overflow

    if (dq.deleteFront(x)) cout << "Deleted from front: " << x << "\n";
    if (dq.deleteRear(x))  cout << "Deleted from rear: "  << x << "\n";
    dq.display();               // 5 10 20

    dq.insertRear(99);          // wraps around the array
    dq.insertFront(77);
    dq.display();               // 77 5 10 20 99

    int pos = dq.search(20);
    if (pos != -1) cout << "Found 20 at position " << pos << " (from front)\n";
    else           cout << "20 not found\n";

    pos = dq.search(1000);
    if (pos != -1) cout << "Found 1000 at position " << pos << "\n";
    else           cout << "1000 not found\n";

    while (dq.deleteFront(x)) { }   // empty it
    dq.deleteRear(x);               // underflow
    dq.display();

    return 0;
}