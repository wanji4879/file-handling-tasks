# Task 1: File Creation (Write mode)
try:
    with open('my_file.txt', 'w') as file:
        file.write("This is the first line.\n")
        file.write("Number of students: 50\n")
        file.write("Welcome to the Python class!\n")
    print("File created and initial content written.")
except PermissionError:
    print("You don't have permission to write to this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Task 2: File Reading and Display
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nContents of 'my_file.txt':")
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Task 3: File Appending (Append mode)
try:
    with open('my_file.txt', 'a') as file:
        file.write("This is an appended line.\n")
        file.write("Number of teachers: 5\n")
        file.write("Class time: 9 AM.\n")
    print("Additional content appended.")
except PermissionError:
    print("You don't have permission to append to this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Task 4: Error Handling with Finally Block
try:
    with open('my_file.txt', 'r') as file:
        content = file.read()
        print("\nUpdated contents of 'my_file.txt':")
        print(content)
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You don't have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("\nFile operation completed.")
