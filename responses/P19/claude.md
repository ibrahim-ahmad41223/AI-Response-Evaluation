Imagine your school has a big notebook listing every student. Each student has a row with details like their roll number, name, birthday, and phone number. A **key** is just a detail (or a mix of details) that helps you find exactly one student, with no mix-ups.

**Super key: any combo that picks out one student**

Think of it as "anything that works, even if it's more than you need." Roll number alone works. But "roll number + name" also works, and so does "roll number + name + birthday." All of these are super keys, even though some have extra, unnecessary details tacked on.

**Candidate key: the smallest combo that still works**

Take a super key and remove everything you don't need. If you can't remove anything without losing the "exactly one student" power, it's a candidate key. Roll number is a candidate key. So is the phone number, if every student has their own unique one. You can have several candidates, like several people who all could be class captain.

**Primary key: the one candidate you pick as the boss**

Out of all your candidate keys, you choose one to be the official one. Say the school picks roll number. That's the primary key. The rules are that it can never be empty and can never repeat. The other candidates (like phone number) are just the ones who didn't get picked.

**Composite key: a key made of two or more details together**

Sometimes no single detail is unique, but a pair is. Imagine a class timetable where "Monday" appears many times and "Period 1" appears many times. But "Monday + Period 1" appears only once. Together they identify one slot. That team-up is a composite key.

**Surrogate key: a made-up ID**

Sometimes real details are messy. Names can repeat, and phone numbers change. So the school just invents a new number for each student, like Student #1, #2, #3. It has no meaning in real life. It exists only to be a clean, never-changing label. Think of the number on a tag at a coat check: it's not about you, it just helps them find your coat.

**Quick summary**

| Key | Kid-friendly meaning |
|---|---|
| Super key | Any combo that identifies one student (extras allowed) |
| Candidate key | The smallest combo that still works |
| Primary key | The one candidate chosen as the official ID |
| Composite key | A key built from two or more details together |
| Surrogate key | A made-up number whose only job is to be the ID |

A trick to remember: **super** keys are the "big family," **candidates** are the trimmed-down ones in that family, and the **primary** is the one picked to represent them.