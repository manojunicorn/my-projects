students = []

def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    dept = input("Enter department: ")
    students.append({"name": name, "roll": roll, "dept": dept})
    print("Student added successfully!\n")

def view_students():
    if not students:
        print("No student records found.\n")
        return
    print("Student Records:")
    for s in students:
        print(f"Name: {s['name']}, Roll: {s['roll']}, Dept: {s['dept']}")
    print()

def delete_student():
    roll = input("Enter roll number to delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student deleted successfully!\n")
            return
    print("Student not found.\n")

while True:
    print("Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Delete Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        delete_student()
    elif choice == '4':
        print("Exiting program...")
        break
    else:
        print("Invalid choice!\n")
