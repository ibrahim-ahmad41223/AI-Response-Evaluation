**The error:** a missing semicolon after `using namespace std`.

**Why it occurs:** In C++, a `using` directive is a statement, and every statement must end with a semicolon. Without it, the compiler keeps reading past `std` and runs into `int main()` on the next line, which it can't parse as part of the directive. You'll typically see an error like `expected ';' before 'int'` (GCC) or `missing ';' before 'int'` (MSVC). The compiler often reports the problem on the line *after* the actual mistake, because that's where it first realizes something is wrong.

**Corrected program:**

```cpp
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World.";
    return 0;
}
```

This compiles and prints `Hello World.`

**Optional note:** `using namespace std;` is fine for small programs, but in larger projects it's often avoided because it can cause name collisions. The alternative is to qualify names explicitly:

```cpp
#include <iostream>

int main() {
    std::cout << "Hello World.";
    return 0;
}
```