import sqlite3

# Connect to database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    branch TEXT
)
""")

conn.commit()


# Add Student
def add_student():
    student_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    branch = input("Enter Branch: ")

    try:
        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?)",
            (student_id, name, age, branch)
        )

        conn.commit()
        print("Student Added Successfully")

    except sqlite3.IntegrityError:
        print("Student ID already exists")


# View Students
def view_students():
    cursor.execute("SELECT * FROM students")

    records = cursor.fetchall()

    if not records:
        print("No records found")
        return

    print("\nID\tName\tAge\tBranch")
    print("-" * 40)

    for record in records:
        print(f"{record[0]}\t{record[1]}\t{record[2]}\t{record[3]}")


# Search Student
def search_student():
    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    record = cursor.fetchone()

    if record:
        print("\nStudent Found:")
        print(record)
    else:
        print("Student Not Found")


# Update Student
def update_student():
    student_id = int(input("Enter Student ID: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    if cursor.fetchone() is None:
        print("Student Not Found")
        return

    new_name = input("Enter New Name: ")
    new_age = int(input("Enter New Age: "))
    new_branch = input("Enter New Branch: ")

    cursor.execute(
        """
        UPDATE students
        SET name = ?, age = ?, branch = ?
        WHERE id = ?
        """,
        (new_name, new_age, new_branch, student_id)
    )

    conn.commit()
    print("Student Updated Successfully")


# Delete Student
def delete_student():
    student_id = int(input("Enter Student ID to Delete: "))

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )

    if cursor.fetchone() is None:
        print("Student Not Found")
        return

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    conn.commit()
    print("Student Deleted Successfully")


# Main Menu
while True:

    print("\n===== Student Database Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice")


# Close connection
conn.close()