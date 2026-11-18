### **Error**

The error is a **missing semicolon (**`;`**)** after the `using namespace std` statement.

Original line:

```
using namespace std
```

Corrected line:

```
using namespace std;
```

### **Why does it occur?**

In C++, statements must generally end with a semicolon. Since the semicolon is missing, the compiler reports a syntax error when it encounters `int main()`.

### **Corrected complete program**

```
#include <iostream>
using namespace std;

int main() {
    cout << "Hello World.";
    return 0;
}
```

**Output:**

```
Hello World.
```

**Remember:** Always put a semicolon after `using namespace std;`, variable declarations, and most executable statements in C++.