**No, the right operand is NOT evaluated.**

This is called **short-circuit evaluation**.

In C, the logical OR operator (`||`) works as follows:

- If the left operand evaluates to true (non-zero), the entire expression is already true.
- Therefore, C skips evaluating the right operand because it cannot change the final result.

**Example:**

```
int a = 5, b = 10;

if (a > 0 || b++ > 10)
{
    printf("True");
}
```

Here:

- `a > 0` is true.
- The right operand `b++ > 10` is never evaluated.
- Therefore, `b` remains `10`.

**Remember:** With `||`, if the left side is true, the right side is skipped. With `&&`, if the left side is false, the right side is skipped.

You can practice this concept with a few short output-prediction questions.