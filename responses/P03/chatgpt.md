These concepts are important in **DBMS (Database Management Systems)** because they help identify records uniquely and maintain relationships between tables.

Let's use a `Student` table for the examples.

## **1. Primary Key**

**Definition:** A primary key is a column (or combination of columns) that uniquely identifies each record in a table. It cannot contain duplicate or NULL values.

**Example:**

| Student_ID | Name  | Email            |
| ---------- | ----- | ---------------- |
| 101        | Ali   | ali\@gmail.com   |
| 102        | Ahmed | ahmed\@gmail.com |
| 103        | Sara  | sara\@gmail.com  |

Here, `Student_ID` is the primary key because every student has a unique ID.

## **2. Candidate Key**

**Definition:** A candidate key is any column (or combination of columns) that can uniquely identify each record in a table. A table can have multiple candidate keys, but only one is selected as the primary key.

**Example:**

Using the same Student table:

- `Student_ID` uniquely identifies each student.
- `Email` also uniquely identifies each student.

Therefore, both `Student_ID` and `Email` are candidate keys. We choose `Student_ID` as the primary key.

## **3. Super Key**

**Definition:** A super key is any column or combination of columns that can uniquely identify a record in a table. It can contain extra attributes that are not necessary for unique identification.

**Example:**

Using the same Student table, these are all super keys:

- `{Student_ID}`
- `{Email}`
- `{Student_ID, Name}`
- `{Student_ID, Email}`
- `{Student_ID, Name, Email}`

Why? Because all these combinations can uniquely identify a student.

**Important:** Every candidate key is a super key, but not every super key is a candidate key.

## **4. Referential Integrity Constraint**

**Definition:** Referential integrity is a rule that ensures relationships between tables remain valid. It requires a foreign key in one table to match an existing primary key in the referenced table (or be NULL if allowed).

**Example:**

Consider two tables:

**Student Table**

| Student_ID (PK) | Name  |
| --------------- | ----- |
| 101             | Ali   |
| 102             | Ahmed |
| 103             | Sara  |

**Enrollment Table**

| Enrollment_ID (PK) | Student_ID (FK) | Course      |
| ------------------ | --------------- | ----------- |
| 1                  | 101             | Database    |
| 2                  | 102             | Programming |
| 3                  | 103             | Networking  |

Here:

- `Student_ID` in the Student table is the primary key.
- `Student_ID` in the Enrollment table is a foreign key.
- Every Student_ID in Enrollment must exist in the Student table.

For example, inserting `Student_ID = 105` into Enrollment would violate referential integrity because student 105 does not exist in the Student table.

## **Quick comparison for exams**

| Concept               | Main purpose                                                 |
| --------------------- | ------------------------------------------------------------ |
| Primary Key           | Uniquely identifies each record; selected candidate key.     |
| Candidate Key         | Minimal set of attributes that uniquely identifies a record. |
| Super Key             | Any set of attributes that uniquely identifies a record.     |
| Referential Integrity | Ensures foreign key values reference valid records.          |

**Remember this relationship:**

- Super Key = Unique identification (may contain extra columns).
- Candidate Key = Minimal super key (no unnecessary columns).
- Primary Key = Candidate key selected for the table.

A useful next step would be practicing a few exam-style MCQs to test the differences between these four concepts.