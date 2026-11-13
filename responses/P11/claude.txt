Here are the two queries:

**1. Insert the record**

```sql
INSERT INTO Student (id, name, rollNo, CGPA)
VALUES (1, 'Ibrahim', 123, 3.45);
```

**2. Display all records**

```sql
SELECT * FROM Student;
```

The `INSERT` statement lists the columns explicitly, so each value maps to the right column regardless of the table's internal column order. The `SELECT *` returns every column of every row in the table.