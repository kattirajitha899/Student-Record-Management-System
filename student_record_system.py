
import json
from pathlib import Path

FILE_NAME = "students.json"


def load_students():
    """Load student records from the JSON file."""
    file_path = Path(FILE_NAME)

    if not file_path.exists():
        return []

    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Error: Student data must be a list.")
            return []

        return data

    except (json.JSONDecodeError, OSError) as error:
        print("Could not load student records:", error)
        return []


def save_students(students):
    """Save student records to the JSON file."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

        return True

    except OSError as error:
        print("Could not save student records:", error)
        return False


def add_student(students):
    roll = input("Enter roll number: ").strip()

    if not roll:
        print("Roll number cannot be empty.")
        return

    if any(s["roll"] == roll for s in students):
        print("That roll number already exists.")
        return

    name = input("Enter student name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    try:
        marks = float(input("Enter marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter marks as a number.")
        return

    students.append({
        "roll": roll,
        "name": name,
        "marks": marks
    })

    if save_students(students):
        print("Student added successfully!")


def view_students(students):
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")

    for student in students:
        print(
            f"Roll: {student['roll']} | "
            f"Name: {student['name']} | "
            f"Marks: {student['marks']}"
        )


def search_student(students):
    roll = input("Enter roll number to search: ").strip()

    for student in students:
        if student["roll"] == roll:
            print("Student found:", student)
            return

    print("Student not found.")


def update_student(students):
    roll = input("Enter roll number to update: ").strip()

    for student in students:
        if student["roll"] == roll:
            name = input(
                "Enter new name (press Enter to keep current): "
            ).strip()

            if name:
                student["name"] = name

            new_marks = input(
                "Enter new marks (press Enter to keep current): "
            ).strip()

            if new_marks:
                try:
                    marks = float(new_marks)

                    if not 0 <= marks <= 100:
                        print("Marks must be between 0 and 100.")
                        return

                    student["marks"] = marks

                except ValueError:
                    print("Invalid marks. Update cancelled.")
                    return

            if save_students(students):
                print("Student updated successfully!")

            return

    print("Student not found.")


def delete_student(students):
    roll = input("Enter roll number to delete: ").strip()

    for student in students:
        if student["roll"] == roll:
            students.remove(student)

            if save_students(students):
                print("Student deleted successfully!")

            return

    print("Student not found.")


def show_high_scorers(students):
    high_scorers = [
        student for student in students
        if student["marks"] >= 75
    ]

    print("\n--- Students scoring 75 or above ---")

    if not high_scorers:
        print("No high scorers found.")
        return

    for student in high_scorers:
        print(student["name"], "-", student["marks"])


def main():
    students = load_students()

    while True:
        print("\n=== Student Record Management System ===")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Show High Scorers")
        print("7. Exit")

        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_high_scorers(students)
        elif choice == "7":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
