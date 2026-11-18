No. In C, if the left operand of `||` evaluates to true (nonzero), the right operand is **not evaluated at all**. This behavior is called **short-circuit evaluation**.

## Why this happens

The result of a logical OR is already determined once the left operand is true: `true || anything` is always true. Evaluating the right side could not change the outcome, so the language guarantees it is skipped.

This isn't just an optimization the compiler may choose to apply. The C standard (C11 §6.5.14) explicitly requires it:

- The `||` operator yields 1 if either operand compares unequal to 0, otherwise 0.
- Unlike the bitwise `|` operator, `||` **guarantees left-to-right evaluation**.
- There is a **sequence point** after the evaluation of the first operand.
- If the first operand compares unequal to 0, the second operand is **not evaluated**.

## Example

```c
#include <stdio.h>

int check(void) {
    printf("check() was called\n");
    return 1;
}

int main(void) {
    int x = 1;

    if (x || check()) {
        printf("Condition is true\n");
    }

    return 0;
}
```

**Output:**
```
Condition is true
```

`check()` never runs, so its `printf` never appears. If you change `x` to `0`, the left side is false, so the right side must be evaluated, and you'll see both messages.

## Why it matters in practice

Short-circuiting lets you write safe and efficient code:

**Guarding against invalid operations**
```c
if (ptr == NULL || ptr->value == 0) {
    // safe: ptr->value is only accessed when ptr is non-NULL
}
```

**Avoiding expensive calls**
```c
if (cache_hit || expensive_lookup()) { ... }
```

**Pitfall: side effects may be skipped**
```c
int a = 1, b = 0;
if (a || ++b) { }
// b is still 0, because ++b never executed
```

If you rely on a side effect in the right operand (like incrementing, assigning, or calling a function with effects), remember that it only happens when the left operand is false.

## Related note

The same logic applies to `&&` in the opposite direction: if the left operand is false, the right operand is not evaluated, since `false && anything` is always false.