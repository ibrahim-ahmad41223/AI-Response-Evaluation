**No, that’s incorrect.**

A **primary key** is a column (or a combination of columns) whose values **uniquely identify** each record (row) in a table.

### Key points:
- Every value in the primary key must be unique.
- It cannot contain `NULL` values.
- A table can have only **one** primary key.
- When the primary key consists of multiple columns, it is called a **composite primary key**. Even then, the *combination* of those columns must uniquely identify each row.

### Example
```sql
CREATE TABLE Orders (
    OrderID INT,
    ProductID INT,
    Quantity INT,
    PRIMARY KEY (OrderID, ProductID)  -- composite primary key
);
```
Here, neither `OrderID` nor `ProductID` alone needs to be unique, but the *pair* `(OrderID, ProductID)` must be unique for every row.

### What you might be thinking of
- **Candidate keys**: Any set of columns that could uniquely identify rows.
- **Primary key**: The specific candidate key chosen as the main unique identifier.
- **Foreign keys**: Columns that reference a primary key in another table (they do *not* have to be unique themselves).

So the definition is the opposite of what you stated: primary keys (including composite ones) **do** uniquely identify records.