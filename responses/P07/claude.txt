```cpp
#include <iostream>
using namespace std;

int main() {
    int day;

    cout << "Enter a number (1-7): ";
    cin >> day;

    if (cin.fail()) {
        cout << "Error: Please enter a valid integer." << endl;
        return 1;
    }

    switch (day) {
        case 1:
            cout << "Monday" << endl;
            break;
        case 2:
            cout << "Tuesday" << endl;
            break;
        case 3:
            cout << "Wednesday" << endl;
            break;
        case 4:
            cout << "Thursday" << endl;
            break;
        case 5:
            cout << "Friday" << endl;
            break;
        case 6:
            cout << "Saturday" << endl;
            break;
        case 7:
            cout << "Sunday" << endl;
            break;
        default:
            cout << "Error: Invalid input. Please enter a number between 1 and 7." << endl;
            break;
    }

    return 0;
}
```

**How it works:**

- The program reads an integer into `day`.
- `cin.fail()` catches non-numeric input (like letters), which would otherwise leave `day` in a bad state.
- The `switch` matches `day` against cases 1 through 7, printing the weekday and using `break` to prevent fall-through.
- The `default` case handles any integer outside 1-7 and displays an error.

**Sample runs:**

```
Enter a number (1-7): 3
Wednesday
```

```
Enter a number (1-7): 9
Error: Invalid input. Please enter a number between 1 and 7.
```

```
Enter a number (1-7): abc
Error: Please enter a valid integer.
```