# Write to a File

file_path = "output/student_data.txt"

content = """Python and Bash Assignment
Student Name: Mohd Imran
Topic: File Handling
This file was created using Python.
"""

with open(file_path, "w") as file:
    file.write(content)

print(f"File created successfully: {file_path}")
print("Content has been written to the file.")
