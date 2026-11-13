Here is a simple C++ program using a `switch` statement:

```

#include <iostream>
using namespace std;

int main()
{
    int day;

    cout << "Enter a number (1-7): ";
    cin >> day;

    switch (day)
    {
        case 1:
            cout << "Monday";
            break;

        case 2:
            cout << "Tuesday";
            break;

        case 3:
            cout << "Wednesday";
            break;

        case 4:
            cout << "Thursday";
            break;

        case 5:
            cout << "Friday";
            break;

        case 6:
            cout << "Saturday";
            break;

        case 7:
            cout << "Sunday";
            break;

        default:
            cout << "Invalid input!";
    }

    return 0;
}

```

**Example output:**

```
Enter a number (1-7): 3
Wednesday
```

**Key point:** The `default` case handles any input outside 1–7, while `break` prevents execution from continuing into the next case.

You can also practice writing the same program using `if-else` to understand the difference.