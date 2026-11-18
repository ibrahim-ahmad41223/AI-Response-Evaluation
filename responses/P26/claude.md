Here's the complete program:

```cpp
#include <iostream>
using namespace std;

// Prints the first 'size' elements of the array on one line
void printArray(const int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Removes duplicates, keeping the first occurrence of each value.
// 'size' is passed by reference so the caller sees the new length.
void removeDuplicates(int arr[], int &size) {
    int newSize = 0;                       // Count of unique elements kept so far

    for (int i = 0; i < size; i++) {
        bool isDuplicate = false;

        // Check whether arr[i] already appears among the kept elements
        for (int j = 0; j < newSize; j++) {
            if (arr[i] == arr[j]) {
                isDuplicate = true;
                break;
            }
        }

        // Keep the element only if it hasn't been seen before
        if (!isDuplicate) {
            arr[newSize++] = arr[i];
        }
    }

    size = newSize;                        // Update the logical size
}

// Sorts the array in ascending order using bubble sort
void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        bool swapped = false;              // Optimization: stop early if already sorted

        // After each pass, the largest remaining element settles at the end
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];         // Swap adjacent out-of-order elements
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }

        if (!swapped) break;               // No swaps means the array is sorted
    }
}

// Reverses the array in place by swapping elements from both ends
void reverseArray(int arr[], int size) {
    for (int i = 0, j = size - 1; i < j; i++, j--) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}

int main() {
    int arr[] = {2, 4, 95, 6, 67, 23, 56, 90, 24, 56, 67, 23};
    int size = sizeof(arr) / sizeof(arr[0]);   // Number of elements (12)

    cout << "Original array:          ";
    printArray(arr, size);

    removeDuplicates(arr, size);
    cout << "After removing duplicates: ";
    printArray(arr, size);

    bubbleSort(arr, size);
    cout << "After bubble sort:         ";
    printArray(arr, size);

    reverseArray(arr, size);
    cout << "After reversing:           ";
    printArray(arr, size);

    return 0;
}
```

**Expected output:**

```
Original array:          2 4 95 6 67 23 56 90 24 56 67 23 
After removing duplicates: 2 4 95 6 67 23 56 90 24 
After bubble sort:         2 4 6 23 24 56 67 90 95 
After reversing:           95 90 67 56 24 23 6 4 2 
```

**Key design points:**

- `removeDuplicates` takes `size` by reference because the array's logical length shrinks (12 → 9). The later functions then receive the updated size, so they ignore the leftover tail elements.
- Duplicate checking compares each element only against the already-kept prefix, which preserves the first occurrence and the original order.
- `bubbleSort` uses a `swapped` flag so it exits early once the array is sorted.
- `printArray` takes a `const` array since it only reads the data.