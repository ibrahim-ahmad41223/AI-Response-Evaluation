A **primary key** is a column—or a combination of columns—whose exact purpose is to **uniquely identify** every single record (row) in a database table.

For a column or set of columns to qualify as a primary key, it must enforce two strict rules:

* **Uniqueness:** No two rows in the table can share the exact same primary key value.
* **Not Null:** Every row must contain a valid value for the primary key; it cannot be left blank (`NULL`).

*(Note: When a primary key is made up of multiple columns working together—such as combining `Order_ID` and `Product_ID` in an order-items table—it is called a **composite primary key**. Even then, the specific combination of those values must remain unique across the entire table.)*

So, your statement has the definition reversed: primary keys **do** uniquely identify records.