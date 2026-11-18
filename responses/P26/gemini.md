```cpp
#include <iostream>

// Helper function to display the elements of the array
void displayArray(const int arr[], int size) {
    for (int i = 0; i < size; ++i) {
        std::cout << arr[i] << " ";
    }
    std::cout << "\n";
}

// Removes duplicate elements in-place while preserving the first occurrence.
// Takes 'size' by reference so the caller's array length updates automatically.
void removeDuplicates(int arr[], int& size) {
    for (int i = 0; i < size; ++i) {
        for (int j = i + 1; j < size; ) {
            if (arr[i] == arr[j]) {
                // Shift remaining elements left to overwrite the duplicate
                for (int k = j; k < size - 1; ++k) {
                    arr[k] = arr[k + 1];
                }
                --size; // Reduce logical array size
                // Do not increment 'j' here; re-check the shifted element at index 'j'
            } else {
                ++j;
            }
        }
    }
}

// Sorts the array in ascending order using the Bubble Sort algorithm
void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; ++i) {
        bool swapped = false;

        // Last 'i' elements are already in their final sorted positions
        for (int j = 0; j < size - i - 1; ++j) {
            if (arr[j] > arr[j + 1]) {
                // Swap adjacent elements if they are in the wrong order
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = true;
            }
        }

        // Optimization: exit early if no swaps occurred during this pass
        if (!swapped) {
            break;
        }
    }
}

// Reverses the elements of the array in-place using two pointers
void reverseArray(int arr[], int size) {
    int start = 0;
    int end = size - 1;

    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        ++start;
        --end;
    }
}

int main() {
    int arr[] = {2, 4, 95, 6, 67, 23, 56, 90, 24, 56, 67, 23};
    int size = sizeof(arr) / sizeof(arr[0]);

    std::cout << "Original array:         ";
    displayArray(arr, size);

    // 1. Remove duplicates (retaining first occurrence)
    removeDuplicates(arr, size);
    std::cout << "After duplicate removal: ";
    displayArray(arr, size);

    // 2. Sort in ascending order
    bubbleSort(arr, size);
    std::cout << "After ascending sort:    ";
    displayArray(arr, size);

    // 3. Reverse the array
    reverseArray(arr, size);
    std::cout << "After reversing:         ";
    displayArray(arr, size);

    return 0;
}

```

### Program Output

```text
Original array:          2 4 95 6 67 23 56 90 24 56 67 23 
After duplicate removal: 2 4 95 6 67 23 56 90 24 
After ascending sort:    2 4 6 23 24 56 67 90 95 
After reversing:         95 90 67 56 24 23 6 4 2 

```

### Design Notes

* **Reference Parameter (`int& size`):** Because C-style arrays cannot be resized physically in memory, `removeDuplicates` tracks the logical length by passing `size` by reference and decrementing it each time a duplicate is overwritten.
* **In-Place Operations:** All three transformations mutate the original array directly without allocating auxiliary arrays.
* **Early-Exit Optimization:** `bubbleSort` tracks whether any elements were swapped during an inner pass and terminates early if the array is already sorted.