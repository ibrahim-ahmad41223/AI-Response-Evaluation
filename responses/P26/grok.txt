```cpp
#include <iostream>
using namespace std;

// Function to display the elements of the array
void displayArray(const int arr[], int size) {
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// Function to remove duplicates while retaining the first occurrence of each element.
// Modifies the array in-place and updates the size.
void removeDuplicates(int arr[], int& size) {
    if (size <= 1) return;  // Nothing to do for empty or single-element array

    int newSize = 1;  // First element is always kept

    for (int i = 1; i < size; i++) {
        bool isDuplicate = false;

        // Check if arr[i] already exists in the unique portion (0 to newSize-1)
        for (int j = 0; j < newSize; j++) {
            if (arr[i] == arr[j]) {
                isDuplicate = true;
                break;
            }
        }

        // If not a duplicate, keep it by placing it at the next unique position
        if (!isDuplicate) {
            arr[newSize] = arr[i];
            newSize++;
        }
    }

    size = newSize;  // Update the size to reflect only unique elements
}

// Bubble sort function that sorts the array in ascending order
void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        // Last i elements are already in place
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap adjacent elements if they are in the wrong order
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Function to reverse the array in-place
void reverseArray(int arr[], int size) {
    int start = 0;
    int end = size - 1;

    while (start < end) {
        // Swap elements at start and end
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;

        start++;
        end--;
    }
}

int main() {
    // Original array
    int arr[] = {2, 4, 95, 6, 67, 23, 56, 90, 24, 56, 67, 23};
    int size = sizeof(arr) / sizeof(arr[0]);

    cout << "Original array: ";
    displayArray(arr, size);

    // Step 1: Remove duplicates (retaining first occurrence)
    removeDuplicates(arr, size);
    cout << "After removing duplicates: ";
    displayArray(arr, size);

    // Step 2: Sort in ascending order using bubble sort
    bubbleSort(arr, size);
    cout << "After bubble sort (ascending): ";
    displayArray(arr, size);

    // Step 3: Reverse the sorted array
    reverseArray(arr, size);
    cout << "After reversing: ";
    displayArray(arr, size);

    return 0;
}
```