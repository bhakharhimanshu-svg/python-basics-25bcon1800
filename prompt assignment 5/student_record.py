```python
"""
Advanced Student Record Management System
Author: bhakharhimanshu-svg
Project: python-basics-25bcon1800
"""

import csv
from pathlib import Path


class Student:
    """Represent one student and their academic record."""

    def __init__(self, name: str, roll_no: str, marks: float):
        name = name.strip()
        roll_no = roll_no.strip()

        if not name:
            raise ValueError("Student name cannot be empty.")

        if not roll_no:
            raise ValueError("Roll number cannot be empty.")

        if not 0 <= marks <= 100:
            raise ValueError("Marks must be between 0 and 100.")

        self.name = name
        self.roll_no = roll_no
        self.marks = float(marks)

    @property
    def grade(self) -> str:
        """Return a grade based on marks."""
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        return "F"

    def to_dict(self) -> dict:
        """Convert student information into a dictionary."""
        return {
            "name": self.name,
            "roll_no": self.roll_no,
            "marks": self.marks,
            "grade": self.grade,
        }


class StudentManager:
    """Manage student records in memory."""

    def __init__(self):
        self.students: dict[str, Student] = {}

    def add_student(self, student: Student) -> None:
        """Add a student while preventing duplicate roll numbers."""
        if student.roll_no in self.students:
            raise ValueError("This roll number already exists.")

        self.students[student.roll_no] = student

    def search_student(self, roll_no: str) -> Student | None:
        """Search by roll number."""
        return self.students.get(roll_no.strip())

    def show_all(self) -> None:
        """Display all student records."""
        if not self.students:
            print("No student records found.")
            return

        print("\n" + "-" * 65)
        print(f"{'ROLL NO':12} {'NAME':22} {'MARKS':10} {'GRADE':8}")
        print("-" * 65)

        for student in sorted(
            self.students.values(),
            key=lambda item: item.name.lower()
        ):
            print(
                f"{student.roll_no:12} "
                f"{student.name[:22]:22} "
                f"{student.marks:10.2f} "
                f"{student.grade:8}"
            )

        print("-" * 65)

    def show_statistics(self) -> None:
        """Display class performance statistics."""
        if not self.students:
            print("No records available for analysis.")
            return

        marks = [student.marks for student in self.students.values()]
        topper = max(
            self.students.values(),
            key=lambda student: student.marks
        )

        print("\nCLASS STATISTICS")
        print(f"Total students : {len(marks)}")
        print(f"Average marks  : {sum(marks) / len(marks):.2f}")
        print(f"Highest marks  : {max(marks):.2f}")
        print(f"Lowest marks   : {min(marks):.2f}")
        print(f"Top student    : {topper.name}")
        print(f"Pass count     : {sum(mark >= 40 for mark in marks)}")
        print(f"Fail count     : {sum(mark < 40 for mark in marks)}")

    def export_csv(self, filename: str = "students.csv") -> None:
        """Export records to a CSV file."""
        output_path = Path(filename)

        with output_path.open(
            "w", newline="", encoding="utf-8"
        ) as file:
            fieldnames = ["name", "roll_no", "marks", "grade"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()

            for student in self.students.values():
                writer.writerow(student.to_dict())

        print(f"Records exported to: {output_path.resolve()}")


def main() -> None:
    manager = StudentManager()

    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add student")
        print("2. View all students")
        print("3. Search student")
        print("4. Show class statistics")
        print("5. Export records to CSV")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                name = input("Student name: ")
                roll_no = input("Roll number: ")
                marks = float(input("Marks (0-100): "))

                student = Student(name, roll_no, marks)
                manager.add_student(student)

                print("Student added successfully.")

            elif choice == "2":
                manager.show_all()

            elif choice == "3":
                roll_no = input("Enter roll number to search: ")
                student = manager.search_student(roll_no)

                if student:
                    print(student.to_dict())
                else:
                    print("Student not found.")

            elif choice == "4":
                manager.show_statistics()

            elif choice == "5":
                manager.export_csv()

            elif choice == "6":
                print("Thank you for using the system.")
                break

            else:
                print("Invalid choice. Select 1 to 6.")

        except ValueError as error:
            print(f"Error: {error}")

        except OSError as error:
            print(f"File operation failed: {error}")

        except KeyboardInterrupt:
            print("\nProgram stopped by user.")
            break


if __name__ == "__main__":
    main()
```