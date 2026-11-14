A **double-ended circular queue (deque)** uses modular arithmetic to wrap `front` and `rear` indices around a fixed-size buffer, achieving $O(1)$ insertion and deletion at both ends without shifting elements.

```cpp
#include <iostream>

class CircularDeque {
private:
    static const int CAPACITY = 5;
    int arr[CAPACITY];
    int front;
    int rear;
    int count;

public:
    // Constructor
    CircularDeque() : front(-1), rear(-1), count(0) {
        for (int i = 0; i < CAPACITY; ++i) {
            arr[i] = 0;
        }
    }

    // Destructor
    ~CircularDeque() {
        // Static fixed-size array requires no manual heap deallocation.
        // Resetting state to prevent dangling/stale reads if inspected.
        front = -1;
        rear = -1;
        count = 0;
    }

    bool isFull() const {
        return count == CAPACITY;
    }

    bool isEmpty() const {
        return count == 0;
    }

    // Insert at the front end
    bool insertFront(int value) {
        if (isFull()) {
            std::cout << "Overflow: Deque is full.\n";
            return false;
        }

        if (isEmpty()) {
            front = 0;
            rear = 0;
        } else {
            // Wrap backward using modular arithmetic
            front = (front - 1 + CAPACITY) % CAPACITY;
        }

        arr[front] = value;
        ++count;
        return true;
    }

    // Insert at the rear end
    bool insertRear(int value) {
        if (isFull()) {
            std::cout << "Overflow: Deque is full.\n";
            return false;
        }

        if (isEmpty()) {
            front = 0;
            rear = 0;
        } else {
            // Wrap forward using modular arithmetic
            rear = (rear + 1) % CAPACITY;
        }

        arr[rear] = value;
        ++count;
        return true;
    }

    // Delete from the front end
    bool deleteFront() {
        if (isEmpty()) {
            std::cout << "Underflow: Deque is empty.\n";
            return false;
        }

        if (front == rear) {
            // Only one element was present
            front = -1;
            rear = -1;
        } else {
            front = (front + 1) % CAPACITY;
        }

        --count;
        return true;
    }

    // Delete from the rear end
    bool deleteRear() {
        if (isEmpty()) {
            std::cout << "Underflow: Deque is empty.\n";
            return false;
        }

        if (front == rear) {
            // Only one element was present
            front = -1;
            rear = -1;
        } else {
            rear = (rear - 1 + CAPACITY) % CAPACITY;
        }

        --count;
        return true;
    }

    // Search for a value; returns logical position (0-based from front) or -1
    int search(int target) const {
        if (isEmpty()) {
            return -1;
        }

        for (int i = 0; i < count; ++i) {
            int idx = (front + i) % CAPACITY;
            if (arr[idx] == target) {
                return i;
            }
        }
        return -1;
    }

    // Display elements from front to rear
    void display() const {
        if (isEmpty()) {
            std::cout << "Deque is empty.\n";
            return;
        }

        std::cout << "Deque (front -> rear): ";
        for (int i = 0; i < count; ++i) {
            int idx = (front + i) % CAPACITY;
            std::cout << arr[idx] << " ";
        }
        std::cout << "\n";
    }
};

// Example usage
int main() {
    CircularDeque dq;

    dq.insertRear(10);
    dq.insertRear(20);
    dq.insertFront(5);
    dq.insertFront(1);
    dq.display(); // 1 5 10 20

    int target = 10;
    int pos = dq.search(target);
    if (pos != -1) {
        std::cout << "Found " << target << " at logical index " << pos << "\n";
    } else {
        std::cout << target << " not found\n";
    }

    dq.deleteFront();
    dq.deleteRear();
    dq.display(); // 5 10

    return 0;
}

```

### Implementation Details

* **Circular Wrap-Around:** Moving backward (`insertFront` and `deleteRear`) uses `(index - 1 + CAPACITY) % CAPACITY` so negative values wrap cleanly to the end of the array instead of producing negative modulo remainders.
* **Element Tracking:** Maintaining a `count` variable simplifies `isEmpty()`, `isFull()`, and traversal loops without needing sentinel gaps in the array.
* **Destructor Behavior:** Because `arr` uses automatic storage duration inside the object rather than dynamic heap allocation (`new[]`), the compiler automatically reclaims its memory when the object goes out of scope. If you change `CAPACITY` to a runtime constructor parameter using `new int[capacity]`, the destructor must call `delete[] arr;`.