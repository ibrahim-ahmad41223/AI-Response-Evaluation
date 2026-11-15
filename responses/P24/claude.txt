You've got it backwards. A primary key is a column, or a combination of columns, that *does* uniquely identify each record in a table.

A few key properties:

- **Uniqueness:** No two rows can have the same primary key value.
- **Non-null:** Every row must have a value for the key; NULLs aren't allowed.
- **Single per table:** A table can have only one primary key, though that key can span multiple columns (called a composite key).
- **Stability:** Ideally, the value doesn't change over time, since other tables often reference it.

For example, in a `students` table, `student_id` would typically be the primary key, since each student has exactly one distinct ID. In an `enrollments` table linking students to courses, the primary key might be the combination of `(student_id, course_id)`, because neither column alone is unique, but the pair is.

You may be thinking of a **foreign key**, which refers to a primary key in another table, and which *can* have repeated values (many enrollments can point to the same student). Or perhaps non-key columns like `last_name`, which commonly repeat across records.