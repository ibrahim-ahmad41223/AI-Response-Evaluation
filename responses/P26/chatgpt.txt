Here is a beginner-friendly C++ program with three separate functions. The functions are called in the required order: **remove duplicates → bubble sort → reverse**.

```
#include <iostream>
using namespace std;

// Function to remove duplicates, retaining the first occurrence
int removeDuplicates(int arr[], int size) {
    int newSize = size;

    for (int i = 0; i < newSize; i++) {
        for (int j = i + 1; j < newSize; j++) {
            if (arr[i] == arr[j]) {
                for (int k = j; k < newSize - 1; k++) {
                    arr[k] = arr[k + 1];
                }

                newSize--;
                j--;
            }
        }
    }

    return newSize;
}

// Function to sort the array in ascending order using bubble sort
void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Function to reverse the array
void reverseArray(int arr[], int size) {
    int start = 0;
    int end = size - 1;

    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        start++;
        end--;
    }
}

// Function to display the array
void displayArray(int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {2, 4, 95, 6, 67, 23, 56, 90, 24, 56, 67, 23};
    int size = 12;

    // Step 1: Remove duplicates
    size = removeDuplicates(arr, size);
    cout << "After removing duplicates: ";
    displayArray(arr, size);

    // Step 2: Sort the array in ascending order
    bubbleSort(arr, size);
    cout << "After bubble sort: ";
    displayArray(arr, size);

    // Step 3: Reverse the array
    reverseArray(arr, size);
    cout << "After reversing: ";
    displayArray(arr, size);

    return 0;
}
```

### **Expected output**

```
After removing duplicates: 2 4 95 6 67 23 56 90 24
After bubble sort: 2 4 6 23 24 56 67 90 95
After reversing: 95 90 67 56 24 23 6 4 2
```

### **Important points**

1. **removeDuplicates():** Uses nested loops to find duplicates and shifts remaining elements left. It returns the updated array size.
2. **bubbleSort():** Compares adjacent elements and swaps them if they are in the wrong order.
3. **reverseArray():** Swaps the first and last elements, then moves inward.
4. **displayArray():** Prints the array after each operation.

Compare 5 and 2 → swap

Scan → left to right: positions 1–7Fixed suffix grows ← from the right edge

Pass 1Comparison 1 of 61 swap

2

5

7

1

6

3

4

1

2

3

4

5

6

7

Swap

Result: 2, 5; 5 moves one place right

Sorting step

ShufflePlayStepFinish pass

Give feedback

**Important:** Notice that `removeDuplicates()` returns an integer. This is necessary because removing duplicates changes the logical size of the array, even though its allocated capacity remains unchanged.

You can also practice tracing each function manually to understand how the array changes after every iteration.