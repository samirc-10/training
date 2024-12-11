# Simple program to read a text file and print its content

# Get the file name from the user
file_name = input("Enter the name of the text file: ")

# Open the file and read its content
try:
    with open(file_name, 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)
except FileNotFoundError:
    print(f"The file '{file_name}' was not found.")
