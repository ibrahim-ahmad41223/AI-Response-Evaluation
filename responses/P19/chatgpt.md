Imagine you have a school database that stores information about students. Each student has a name, roll number, and other details.

Database **keys** help us identify students and keep their records organized.

Let's understand five types of keys using a simple school example!

## **1. Primary Key**

A **primary key** is a column that uniquely identifies each student.

Imagine this table:

| Roll No. | Name  | Age |
| -------- | ----- | --- |
| 101      | Ali   | 10  |
| 102      | Ahmed | 11  |
| 103      | Sara  | 10  |

- Every student has a different roll number.
- No two students can have the same roll number.
- A primary key cannot contain NULL (empty) values.

**Example:** `Roll No.` is the primary key.

Think of it like your unique school ID card!

## **2. Candidate Key**

A **candidate key** is any column that could become the primary key because it uniquely identifies each student.

For example:

| Roll No. | Email            | Name  |
| -------- | ---------------- | ----- |
| 101      | ali\@gmail.com   | Ali   |
| 102      | ahmed\@gmail.com | Ahmed |
| 103      | sara\@gmail.com  | Sara  |

Both:

- Roll No.
- Email

can uniquely identify students.

Therefore, both are **candidate keys**.

We choose one candidate key to become the primary key.

## **3. Composite Key**

A **composite key** is a key made by combining two or more columns to identify a record uniquely.

Imagine a student can enroll in multiple subjects.

| Student ID | Subject ID | Marks |
| ---------- | ---------- | ----- |
| 101        | CS101      | 85    |
| 101        | MA101      | 90    |
| 102        | CS101      | 78    |

Here:

- Student ID alone is not unique.
- Subject ID alone is not unique.
- But combining Student ID and Subject ID identifies each record.

**Composite Key:** `(Student ID, Subject ID)`

Think of it as using two clues together to identify something!

## **4. Surrogate Key**

A **surrogate key** is an artificial ID created by the database to identify records.

For example:

| ID | Name  | Age |
| -- | ----- | --- |
| 1  | Ali   | 10  |
| 2  | Ahmed | 11  |
| 3  | Sara  | 10  |

Here, the database creates the ID numbers automatically.

**Example:** `ID` is the surrogate key.

It doesn't have to contain meaningful information. It simply identifies each record.

Think of it like giving every student a new registration number.

## **5. Super Key**

A **super key** is any column or combination of columns that can uniquely identify a record.

For example:

| Roll No. | Name  | Age |
| -------- | ----- | --- |
| 101      | Ali   | 10  |
| 102      | Ahmed | 11  |
| 103      | Sara  | 10  |

Possible super keys include:

- `{Roll No.}`
- `{Roll No., Name}`
- `{Roll No., Age}`
- `{Roll No., Name, Age}`

Why?

Because all these combinations contain Roll No., which uniquely identifies every student.

**Remember:** A super key can contain extra columns that aren't necessary.

## **Quick revision**

| Key           | Simple meaning                                                |
| ------------- | ------------------------------------------------------------- |
| Primary Key   | The main key selected to identify records.                    |
| Candidate Key | A possible choice for the primary key.                        |
| Composite Key | A key made from two or more columns.                          |
| Surrogate Key | An artificially created ID.                                   |
| Super Key     | Any combination of columns that uniquely identifies a record. |

## **Test your understanding!**

**Question 1. Which key is selected from candidate keys?**

Composite Key

Primary Key

Super Key



**Question 2. Which key is made using two or more columns?**

Surrogate Key

Primary Key

Composite Key



**Question 3. A database automatically creates an ID number. What type of key is it?**

Surrogate Key

Candidate Key

Super Key



Check answers