We are given the salary data (in thousands of PKR):

`50, 20, 23, 23, 40, 56, 89, 20, 100, 23, 45, 51, 65, 23`

## **1. Calculate the Mean**

The mean is calculated using:

\\[ \text{Mean}=\frac{\text{Sum of all values}}{\text{Number of values}} \\]

**Step 1: Add all values.**

\\[ 50+20+23+23+40+56+89+20+100+23+45+51+65+23 \\]

\\[ =628 \\]

**Step 2: Count the values.**

There are 14 values.

**Step 3: Calculate the mean.**

\\[ \text{Mean}=\frac{628}{14} \\]

\\[ \boxed{\text{Mean}=44.86} \\]

The average salary is approximately **44.86 thousand PKR**.

## **2. Identify Potential Statistical Outliers**

We will use the **Interquartile Range (IQR) method**.

**Step 1: Arrange the data in ascending order.**

\\[ 20,20,23,23,23,23,40,45,50,51,56,65,89,100 \\]

**Step 2: Calculate Q1 and Q3.**

Since there are 14 values, divide the data into two halves.

- Lower half: 20, 20, 23, 23, 23, 23, 40
- Upper half: 45, 50, 51, 56, 65, 89, 100

Therefore:

\\[ Q1=23 \\]

\\[ Q3=56 \\]

**Step 3: Calculate IQR.**

\\[ IQR=Q3-Q1 \\]

\\[ IQR=56-23=33 \\]

**Step 4: Calculate the outlier boundaries.**

Lower boundary:

\\[ Q1-1.5(IQR)=23-49.5=-26.5 \\]

Upper boundary:

\\[ Q3+1.5(IQR)=56+49.5=105.5 \\]

**Step 5: Identify outliers.**

Any value below -26.5 or above 105.5 is considered a potential outlier.

All values fall within these boundaries.

\\[ \boxed{\text{No statistical outliers}} \\]

## **3. Final Answer**

| Measurement        | Result             |
| ------------------ | ------------------ |
| Number of salaries | 14                 |
| Total salary       | 628,000 PKR        |
| Mean salary        | 44.86 thousand PKR |
| Q1                 | 23                 |
| Q3                 | 56                 |
| IQR                | 33                 |
| Potential outliers | None               |

**Conclusion:** The mean salary is approximately **44,860 PKR**. Using the IQR method, there are no statistical outliers in the given dataset.

**Study tip:** Remember that the IQR method identifies outliers using the 1.5 × IQR rule, not simply by looking for unusually large or small numbers.