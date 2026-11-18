**Error:** Missing semicolon (`;`) at the end of the `using namespace std` statement on line 2.

**Why it occurs:** In C++, every statement must end with a semicolon so the compiler knows where one instruction finishes and the next begins. Without `;` after `using namespace std`, the compiler reads `using namespace std int main()` as a single malformed declaration and fails with a syntax error before `int main()`.

**Corrected program:**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World.";
    return 0;
}

```