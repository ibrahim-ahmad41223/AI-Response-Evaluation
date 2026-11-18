**Mean ≈ 44.86 (thousand PKR).**

**Potential outliers:** Using the common interquartile range (IQR) rule, **none**. Using a z-score threshold of |z| > 2, **100** is a mild potential outlier (z ≈ 2.12); nothing reaches |z| > 3.

### Calculation of the mean
Data (n = 14):  
50, 20, 23, 23, 40, 56, 89, 20, 100, 23, 45, 51, 65, 23  

Sum = 628  
Mean = 628 / 14 ≈ **44.857** (thousand PKR).

### Outlier detection method
Two standard approaches were applied (both are widely used; IQR is preferred here because the sample is small and mildly right-skewed).

**1. IQR method (robust, preferred for this data)**  
- Sorted data: 20, 20, 23, 23, 23, 23, 40, 45, 50, 51, 56, 65, 89, 100  
- Q1 (median of lower half of 7 values) = 23  
- Q3 (median of upper half of 7 values) = 56  
- IQR = Q3 − Q1 = 33  
- Lower fence = Q1 − 1.5 × IQR = 23 − 49.5 = −26.5  
- Upper fence = Q3 + 1.5 × IQR = 56 + 49.5 = 105.5  

All values lie inside (−26.5, 105.5). **No outliers** (even the stricter 3 × IQR fences would not flag any).

**2. Z-score method (mean ± k·SD)**  
- Sample standard deviation ≈ 25.95  
- z = (x − mean) / SD  
- 100 has z ≈ 2.12 (mild potential outlier if the threshold is |z| > 2)  
- 89 has z ≈ 1.70  
- Lowest values (20) have |z| ≈ 0.96  

Nothing exceeds |z| = 3 (a common stricter cutoff).  

**Conclusion:** The mean salary is about 44.86 thousand PKR. Under the robust IQR rule there are no statistical outliers. The value 100 is only a borderline candidate under a liberal z-score rule.