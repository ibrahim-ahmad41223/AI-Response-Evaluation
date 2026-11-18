# Database Keys and Referential Integrity

I'll use one running example throughout:

**Student**(StudentID, Email, Name, Phone, DeptID)

Assume each student has a unique StudentID and a unique Email, while names and phone numbers may repeat or be shared.

---

## 1. Super Key

**Definition:** A set of one or more attributes that uniquely identifies every row in a table. A super key may contain extra attributes that aren't needed for uniqueness.

**Example:** Each of these is a super key of Student:
- {StudentID}
- {Email}
- {StudentID, Name}
- {StudentID, Email, Phone}
- {Email, Name, Phone, DeptID}

Adding more attributes to a key that is already unique still gives a super key. {Name} alone is *not* one, since two students can share a name.

---

## 2. Candidate Key

**Definition:** A *minimal* super key: a super key from which no attribute can be removed without losing uniqueness. A table can have several candidate keys.

**Example:** Candidate keys of Student:
- {StudentID}
- {Email}

{StudentID, Name} is a super key but not a candidate key, because removing Name leaves {StudentID}, which is still unique.

**Relationship:** Every candidate key is a super key, but not every super key is a candidate key.

---

## 3. Primary Key

**Definition:** The one candidate key the designer selects to uniquely identify rows in a table. It cannot contain NULL values and must be unique. Each table has exactly one primary key.

**Example:** Choose {StudentID} as the primary key:

```sql
CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Email     VARCHAR(100) UNIQUE NOT NULL,
    Name      VARCHAR(100),
    Phone     VARCHAR(20),
    DeptID    INT
);
```

The remaining candidate key, Email, is called an **alternate key** and is enforced with a UNIQUE constraint. StudentID is usually preferred because it's short, stable, and never changes, whereas emails can change.

---

## 4. Referential Integrity Constraint

**Definition:** A rule ensuring that a **foreign key** value in one table must either match an existing primary (or candidate) key value in the referenced table, or be NULL. It prevents "orphan" records that point to nothing.

**Example:** Add a Department table and link Student to it:

```sql
CREATE TABLE Department (
    DeptID   INT PRIMARY KEY,
    DeptName VARCHAR(100)
);

CREATE TABLE Student (
    StudentID INT PRIMARY KEY,
    Name      VARCHAR(100),
    DeptID    INT,
    FOREIGN KEY (DeptID) REFERENCES Department(DeptID)
        ON DELETE SET NULL
        ON UPDATE CASCADE
);
```

**Department**

| DeptID | DeptName |
|--------|----------|
| 10 | Computer Science |
| 20 | Mathematics |

**Student**

| StudentID | Name | DeptID |
|-----------|------|--------|
| 1 | Ayesha | 10 |
| 2 | Bilal | 20 |

What the constraint enforces:
- **Insert:** Adding a student with DeptID = 99 is rejected, since no such department exists.
- **Delete:** Deleting department 10 triggers the chosen action. Here, Ayesha's DeptID becomes NULL. Other options are `CASCADE` (delete her too) or `RESTRICT` (block the deletion).
- **Update:** Changing a DeptID in Department propagates to Student under `ON UPDATE CASCADE`.

---

## Summary

| Concept | Key idea |
|---|---|
| Super key | Any attribute set that uniquely identifies rows |
| Candidate key | A minimal super key |
| Primary key | The chosen candidate key (unique, non-NULL) |
| Referential integrity | Foreign keys must match an existing key in the referenced table, or be NULL |

The first three form a hierarchy: **Super keys ⊇ Candidate keys ⊇ Primary key**. Referential integrity then uses those keys to keep relationships between tables consistent.