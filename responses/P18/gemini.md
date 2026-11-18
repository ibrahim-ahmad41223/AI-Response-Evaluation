```python
import numpy as np

data = [50, 20, 23, 23, 40, 56, 89, 20, 100, 23, 45, 51, 65, 23]
n = len(data)
sorted_data = sorted(data)
total = sum(data)
mean = np.mean(data)
median = np.median(data)
std_sample = np.std(data, ddof=1)
std_pop = np.std(data, ddof=0)

# Quartiles using standard inclusive/exclusive methods
q1_inc = np.percentile(sorted_data, 25, method='linear')
q3_inc = np.percentile(sorted_data, 75, method='linear')

# Manual textbook method (median of lower half and upper half)
# n = 14 -> lower half is first 7 elements, upper half is last 7 elements
lower_half = sorted_data[:7]
upper_half = sorted_data[7:]
q1_manual = np.median(lower_half)
q3_manual = np.median(upper_half)
iqr_manual = q3_manual - q1_manual
lower_bound_manual = q1_manual - 1.5 * iqr_manual
upper_bound_manual = q3_manual + 1.5 * iqr_manual

outliers_iqr = [x for x in sorted_data if x < lower_bound_manual or x > upper_bound_manual]

# Z-scores (sample std)
z_scores = [(x, (x - mean) / std_sample) for x in sorted_data]

print(f"n: {n}")
print(f"Sorted: {sorted_data}")
print(f"Sum: {total}")
print(f"Mean: {mean:.4f}")
print(f"Median: {median}")
print(f"Lower half: {lower_half}, Q1 manual: {q1_manual}")
print(f"Upper half: {upper_half}, Q3 manual: {q3_manual}")
print(f"Q1 linear: {q1_inc}, Q3 linear: {q3_inc}")
print(f"IQR manual: {iqr_manual}")
print(f"Bounds manual: [{lower_bound_manual}, {upper_bound_manual}]")
print(f"Outliers (IQR): {outliers_iqr}")
print(f"Sample Std: {std_sample:.4f}")
print("Z-scores:", [(x, round(z, 2)) for x, z in z_scores])


```

```text
n: 14
Sorted: [20, 20, 23, 23, 23, 23, 40, 45, 50, 51, 56, 65, 89, 100]
Sum: 628
Mean: 44.8571
Median: 42.5
Lower half: [20, 20, 23, 23, 23, 23, 40], Q1 manual: 23.0
Upper half: [45, 50, 51, 56, 65, 89, 100], Q3 manual: 56.0
Q1 linear: 23.0, Q3 linear: 54.75
IQR manual: 33.0
Bounds manual: [-26.5, 105.5]
Outliers (IQR): []
Sample Std: 25.9492
Z-scores: [(20, -0.96), (20, -0.96), (23, -0.84), (23, -0.84), (23, -0.84), (23, -0.84), (40, -0.19), (45, 0.01), (50, 0.2), (51, 0.24), (56, 0.43), (65, 0.78), (89, 1.7), (100, 2.13)]


```

The **mean salary is 44.86 thousand PKR** (44,857 PKR), and there are **no strict statistical outliers** under standard detection methods, though **100** (100,000 PKR) sits near the upper boundary and qualifies as a mild high observation under a 2-standard-deviation rule.

---

### 1. Calculating the Mean

The arithmetic mean is the sum of all observations divided by the total count ($n = 14$):

$$\text{Sum} = 50 + 20 + 23 + 23 + 40 + 56 + 89 + 20 + 100 + 23 + 45 + 51 + 65 + 23 = 628$$

$$\text{Mean} = \frac{628}{14} \approx 44.86 \text{ thousand PKR (44,857 PKR)}$$

---

### 2. Outlier Detection: Interquartile Range (IQR) Method

Because salary distributions are typically right-skewed, the **1.5 × IQR rule** is the preferred method for identifying outliers without being distorted by extreme values.

1. **Sort the data in ascending order ($n = 14$):**

$$20, 20, 23, 23, 23, 23, 40, \mid 45, 50, 51, 56, 65, 89, 100$$


2. **Find the quartiles ($Q_1$ and $Q_3$):**
* **Lower half (first 7 values):** $20, 20, 23, \mathbf{23}, 23, 23, 40 \implies Q_1 = 23$
* **Upper half (last 7 values):** $45, 50, 51, \mathbf{56}, 65, 89, 100 \implies Q_3 = 56$


3. **Compute the Interquartile Range (IQR):**

$$\text{IQR} = Q_3 - Q_1 = 56 - 23 = 33$$


4. **Calculate the outlier fences:**
* **Lower Fence:** $Q_1 - 1.5(\text{IQR}) = 23 - 1.5(33) = 23 - 49.5 = -26.5$
* **Upper Fence:** $Q_3 + 1.5(\text{IQR}) = 56 + 1.5(33) = 56 + 49.5 = 105.5$


5. **Evaluate the dataset:**
All values lie between **20** and **100**, which falls entirely inside the interval $[-26.5, 105.5]$. Even though **89** and **100** appear noticeably higher than the cluster in the 20s–50s, neither exceeds the upper fence of **105.5**, meaning **0 outliers** are detected by the IQR method.


---

### 3. Alternative Check: Z-Score Method

If assuming an approximately normal distribution, outliers are evaluated using standard deviations from the mean ($s \approx 25.95$):

$$z = \frac{x - \bar{x}}{s}$$

* **Strict outlier threshold ($\vert{}z\vert{}$ greater than 3):** No values exceed $\pm 3$. The highest value, **100**, has $z = \frac{100 - 44.86}{25.95} \approx +2.13$, and **89** has $z \approx +1.70$.
* **Mild/unusual threshold ($\vert{}z\vert{}$ greater than 2):** Under a looser 2-standard-deviation cutoff, **100** ($z = +2.13$) is flagged as a mildly unusual high salary, while **89** remains within normal variation.