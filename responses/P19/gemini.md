Imagine your school has a giant digital notebook (a database) that keeps track of every student. Because two kids might have the exact same name—like **Maya Patel**—the school needs special "tags" called **keys** to make sure it never mixes up your grades or lunch money with someone else's.

Here is how those five keys work using your school's student list:

| Student ID | Library Card # | First Name | Last Name | Grade | Locker # |
| --- | --- | --- | --- | --- | --- |
| **101** | L-882 | Maya | Patel | 5 | 42 |
| **102** | L-904 | Leo | Gomez | 5 | 17 |
| **103** | L-715 | Maya | Patel | 4 | 89 |

---

### 1. Super Key (Any "No-Mix-Up" Combo)

A **super key** is any single piece of information—or group of details—that points to **only one specific student**.

* **Example:** If you look up **Student ID 101 + First Name Maya + Grade 5**, you will definitely find the right Maya. Even though you added extra clues you didn't really need, the combo still uniquely identifies one kid.

### 2. Candidate Key (The Best Single Clues)

A **candidate key** is a super key with all the extra, unnecessary clues trimmed away. It is the shortest possible way to identify one student without guessing.

* **Example:** On our chart, **Student ID** is a candidate key because no two students share an ID. **Library Card #** is also a candidate key because every kid gets their own card number. (First Name is *not* a candidate key because two kids are named Maya!)

### 3. Primary Key (The Official Winner)

The school looks at all its candidate keys and picks **one official favorite** to use every single day. That winner is the **primary key**, and it can never be left blank.

* **Example:** Between *Student ID* and *Library Card #*, the school picks **Student ID** as the primary key because not every new kid has a library card yet, but every student gets an ID on day one.

### 4. Composite Key (Teamwork Clues)

Sometimes, no single column is unique on its own, so two or more columns have to team up to identify one record. That team is a **composite key**.

* **Example:** Imagine a chart tracking **School Clubs**. Leo can join Chess Club and Art Club, and Maya can also join Chess Club. Neither *Student ID* nor *Club Name* is unique by itself—but together (**Student ID + Club Name**), they pinpoint Leo's exact spot in Chess Club.

### 5. Surrogate Key (The Made-Up Number)

A **surrogate key** is a fake, computer-generated number created purely to be a primary key because real-world details are too messy or might change.

* **Example:** You weren't born with **Student ID 101**—the school computer just invented that number when you enrolled so it wouldn't have to rely on your name or address.