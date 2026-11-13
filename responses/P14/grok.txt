**Error:** Missing semicolon after the `using` directive.

```cpp
using namespace std   // ← missing ;
```

**Why it occurs:**  
In C++, `using namespace std;` is a complete declaration/statement and therefore requires a terminating semicolon. Without it the compiler treats the following tokens (`int main()...`) as a continuation of the same declaration, which is syntactically invalid and produces a compilation error (typically something like “expected ‘;’ before ‘int’” or “expected unqualified-id”).

**Corrected complete program:**

```cpp
#include <iostream>
using namespace std;
int main(){
    cout << "Hello World.";
    return 0;
}
```