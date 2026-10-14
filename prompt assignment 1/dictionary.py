```python
# Student Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student already exists!")
        return

    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks (0-100): "))

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    students[roll] = {"name": name, "marks": marks}
    print("Student added successfully!")

def search_student():
    roll = input("Enter Roll Number: ")

    if roll in students:
        print("Student Details:", students[roll])
    else:
        print("Student not found!")

def update_marks():
    roll = input("Enter Roll Number: ")

    if roll in students:
        marks = float(input("Enter New Marks: "))

        if 0 <= marks <= 100:
            students[roll]["marks"] = marks
            print("Marks updated!")
        else:
            print("Invalid marks.")
    else:
        print("Student not found!")

def display_students():
    if not students:
        print("No student records available.")
        return

    for roll, details in students.items():
        print(
            f"Roll: {roll} | "
            f"Name: {details['name']} | "
            f"Marks: {details['marks']}"
        )

def main():
    while True:
        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Marks")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                add_student()
            elif choice == "2":
                search_student()
            elif choice == "3":
                update_marks()
            elif choice == "4":
                display_students()
            elif choice == "5":
                print("Program closed.")
                break
            else:
                print("Invalid choice!")

        except ValueError:
            print("Please enter valid numeric marks.")

if __name__ == "__main__":
    main()
```