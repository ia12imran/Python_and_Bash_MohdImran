# Read from a File

file_path = "output/student_data.txt"

with open(file_path, "r") as file:
    content = file.read()

print("File Content:")
print("--------------------")
print(content)
print("--------------------")
