Relational databases use keys and constraints to uniquely identify rows and maintain valid relationships across tables.

Consider the following reference schema to see how each concept applies in practice:

**`Students`**

| `student_id` | `email` | `national_id` | `full_name` | `dept_id` |
| --- | --- | --- | --- | --- |
| 101 | ali@uni.edu | 35202-111 | Ali Khan | D1 |
| 102 | sara@uni.edu | 35202-222 | Sara Ahmed | D2 |

**`Departments`**

| `dept_id` | `dept_name` |
| --- | --- |
| D1 | Computer Science |
| D2 | Electrical Engineering |

---

### 1. Super Key

A **super key** is any single attribute or combination of attributes that uniquely identifies every row in a table. It may contain extra, unnecessary attributes beyond what is strictly required for uniqueness.

* **Example:** In the `Students` table, `{student_id}` is a super key, and `{student_id, full_name}` or `{email, national_id, dept_id}` are also super keys. Because `student_id` alone is already unique, adding `full_name` to it still guarantees uniqueness—making the pair a valid super key, even though `full_name` is redundant.

### 2. Candidate Key

A **candidate key** is a *minimal* super key—a column or set of columns that uniquely identifies each row without containing any redundant attributes. If you remove any attribute from a candidate key, it loses its ability to uniquely identify rows.

* **Example:** In the `Students` table, there are three candidate keys:
* `{student_id}`
* `{email}`
* `{national_id}`


Unlike `{student_id, full_name}`, none of these three contain extra columns, yet each can independently identify a specific student.

### 3. Primary Key

A **primary key** is the specific candidate key chosen by the database designer to serve as the main identifier for rows in a table. A table can have multiple candidate keys, but only **one** primary key. Primary key values must be unique and cannot be `NULL`.

* **Example:** From the three candidate keys in `Students` (`student_id`, `email`, `national_id`), the designer selects **`student_id`** as the primary key because it is short, numeric, and never changes (unlike an email address). The remaining candidate keys (`email` and `national_id`) become **alternate keys** and are typically enforced with `UNIQUE` constraints.

---

### Key Hierarchy Comparison

| Concept | Uniquely Identifies Rows? | Allows Redundant Columns? | Allows `NULL` Values? | Max per Table |
| --- | --- | --- | --- | --- |
| **Super Key** | Yes | Yes | Depends on column | Many |
| **Candidate Key** | Yes | No (Minimal) | Yes (unless restricted) | Multiple |
| **Primary Key** | Yes | No (Minimal) | **No** | **1** |

---

### 4. Referential Integrity Constraint

A **referential integrity constraint** ensures that relationships between two tables remain consistent. Specifically, when one table contains a foreign key, every non-null value in that foreign key column must match an existing primary key value in the referenced parent table. This prevents "orphan" records that point to non-existent data.

* **Example:** In the schema above, `dept_id` in the `Students` table (child) is a foreign key referencing `dept_id` in the `Departments` table (parent).
* **Valid operation:** Inserting a student with `dept_id = 'D1'` succeeds because `'D1'` exists in `Departments`.
* **Constraint violation:** Attempting to insert a student with `dept_id = 'D9'` fails because `'D9'` does not exist in `Departments`. Similarly, deleting `'D1'` from `Departments` is blocked (or cascades) while Ali Khan still references it in `Students`.