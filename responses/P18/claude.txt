**Data (n = 14):** 50, 20, 23, 23, 40, 56, 89, 20, 100, 23, 45, 51, 65, 23

## Mean

Sum = 50+20+23+23+40+56+89+20+100+23+45+51+65+23 = **628**

Mean = 628 / 14 ≈ **44.86** thousand PKR

## Outlier detection (IQR method)

I used Tukey's IQR rule because it doesn't assume the data is normally distributed, which matters here since the data is skewed and the extreme values would distort a mean/standard-deviation method.

**Step 1: Sort the data**

20, 20, 23, 23, 23, 23, 40, 45, 50, 51, 56, 65, 89, 100

**Step 2: Median** (average of 7th and 8th values) = (40 + 45)/2 = 42.5

**Step 3: Quartiles** (median of each half)
- Lower half: 20, 20, 23, 23, 23, 23, 40 → Q1 = **23**
- Upper half: 45, 50, 51, 56, 65, 89, 100 → Q3 = **56**

**Step 4: IQR** = 56 − 23 = **33**

**Step 5: Fences**
- Lower fence = Q1 − 1.5 × IQR = 23 − 49.5 = **−26.5** (no salary can fall below this)
- Upper fence = Q3 + 1.5 × IQR = 56 + 49.5 = **105.5**

**Result:** Every value lies between −26.5 and 105.5, so the IQR method flags **no outliers**. The highest value, 100, sits just under the upper fence.

## Cross-check: Z-scores

Standard deviation (sample) ≈ 28.5, so:
- 100 → z ≈ (100 − 44.86)/28.5 ≈ **1.93**
- 89 → z ≈ **1.55**

Both are below the common threshold of |z| > 3 (and even the stricter 2), so no outliers here either.

## Conclusion

- **Mean ≈ 44.86k PKR** (median is 42.5k).
- **No statistical outliers** by either method. However, 100 and 89 are the high-end values and make the distribution right-skewed. The 100k is borderline under the IQR rule, so it would be flagged with a slightly stricter multiplier (e.g., 1.0 × IQR gives an upper fence of 89, which would flag 100).
- The repeated 23s and 20s also pull the lower end together, so the mean is slightly above the median.

Note that quartile conventions vary slightly between software (Excel, Python, etc.), so Q1/Q3 may differ a bit, but the conclusion holds with any standard method here.