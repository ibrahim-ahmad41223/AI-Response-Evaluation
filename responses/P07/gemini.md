```cpp
#include <iostream>

int main() {
    int day;

    std::cout << "Enter a number (1-7): ";
    
    // Check if input is a valid integer
    if (!(std::cin >> day)) {
        std::cout << "Error: Invalid input. Please enter a numeric integer.\n";
        return 1;
    }

    switch (day) {
        case 1:
            std::cout << "Monday\n";
            break;
        case 2:
            std::cout << "Tuesday\n";
            break;
        case 3:
            std::cout << "Wednesday\n";
            break;
        case 4:
            std::cout << "Thursday\n";
            break;
        case 5:
            std::cout << "Friday\n";
            break;
        case 6:
            std::cout << "Saturday\n";
            break;
        case 7:
            std::cout << "Sunday\n";
            break;
        default:
            std::cout << "Error: Invalid input. Please enter a number between 1 and 7.\n";
            break;
    }

    return 0;
}

```

### How It Works

* **Stream Validation (`if (!(std::cin >> day))`):** Catches non-numeric inputs (such as letters or symbols) so the program exits cleanly instead of falling through to `default` with an uninitialized value.
* **`switch` Cases (`1`–`7`):** Matches the integer to its corresponding day, using `break` statements to prevent execution from falling through into subsequent cases.
* **`default` Branch:** Handles any integer outside the `1–7` range (such as `0`, `-3`, or `9`).