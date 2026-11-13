**Primary keys, candidate keys, super keys, and referential integrity** are core concepts in relational database design. They help ensure uniqueness of rows and consistency of relationships between tables.

### Super Key
A **super key** is any set of one or more attributes (columns) that can uniquely identify a tuple (row) in a relation (table). It may contain extra attributes that are not necessary for uniqueness.

**Example**  
Consider a `Students` table with columns:  
`StudentID`, `Email`, `Name`, `Phone`

Possible super keys include:  
- `{StudentID}`  
- `{Email}`  
- `{StudentID, Name}`  
- `{Email, Phone}`  
- `{StudentID, Email, Name, Phone}` (the entire set of attributes)

Any of these sets uniquely identifies a student, even if some contain unnecessary columns.

### Candidate Key
A **candidate key** is a minimal super key. It is a super key with no proper subset that is also a super key (i.e., it contains no redundant attributes). A table can have multiple candidate keys.

**Example** (using the same `Students` table)  
Candidate keys:  
- `{StudentID}`  
- `{Email}`  

`{StudentID, Name}` is a super key but **not** a candidate key, because `{StudentID}` alone is already sufficient.

### Primary Key
A **primary key** is the candidate key chosen by the database designer to uniquely identify each row in the table. There can be only one primary key per table. It cannot contain null values.

**Example**  
In the `Students` table, the designer chooses `StudentID` as the primary key.  
- Every student must have a unique, non-null `StudentID`.  
- `Email` remains a candidate key (sometimes called an alternate key) but is not the primary key.

### Referential Integrity Constraints
**Referential integrity** ensures that relationships between tables remain consistent. It is typically enforced through foreign keys: a foreign-key value in a child table must either match an existing primary-key (or unique-key) value in the parent table, or be null (if allowed).

**Example**  
Tables:  
- `Students` (`StudentID` primary key, `Name`, …)  
- `Enrollments` (`EnrollmentID`, `StudentID` foreign key, `CourseID`, …)

Referential integrity requires that every `StudentID` value appearing in `Enrollments` must exist in the `Students` table (or be null).  

Violations that are prevented:  
- Inserting an enrollment for a non-existent student.  
- Deleting a student who still has enrollment records (unless cascading actions or other rules are defined).  
- Updating a student’s `StudentID` in a way that leaves orphaned enrollment rows.

These constraints, together with primary/candidate/super keys, form the foundation of data integrity in relational databases.