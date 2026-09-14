# Student Grades
# This program uses a dictionary to store student names and grades.

students = {
    "Rahul": "A",
    "Priya": "B",
    "Aman": "C"
}

print("Current Student Grades:")
for name, grade in students.items():
    print(f"{name}: {grade}")

print("\n1. Add Student")
print("2. Update Student")
print("3. Display All Students")

choice = input("Enter your choice: ")

if choice == "1":
    name = input("Enter student name: ")
    grade = input("Enter student grade: ")

    if name in students:
        print("Student already exists.")
    else:
        students[name] = grade
        print(f"{name} added successfully with grade {grade}.")

elif choice == "2":
    name = input("Enter student name: ")

    if name in students:
        grade = input("Enter new grade: ")
        students[name] = grade
        print(f"{name}'s grade updated successfully.")
    else:
        print("Student not found.")

elif choice == "3":
    print("\nAll Student Grades:")
    for name, grade in students.items():
        print(f"{name}: {grade}")

else:
    print("Invalid choice.")
