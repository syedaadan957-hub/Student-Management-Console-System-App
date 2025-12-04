student = []

def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    if age <= 0:
        print("Age cannot be zero or negative")
        return
    marks = int(input("Enter marks: "))
    if marks <= 0:
        print("Marks cannot be zero or negative")
        return
    student_append = {"name": name, "age": age, "marks": marks}
    student.append(student_append)


def view_students():
    if len(student) == 0:
        print("No students registered")
    else:
        for s in student:
            print("Name:", s["name"], "Age:", s["age"], "Marks:", s["marks"])


def search_student():
    if len(student) == 0:
        print("No records yet.")
    else:
        for s in student:
            name = input("Enter a name to search: ")
            if s["name"].lower() == name.lower():
                print("Name:", s["name"], "Age:", s["age"], "Marks:", s["marks"])
                break
            else:
                print("Student not in our Records")


def update_marks():
    if len(student) == 0:
        print("No records yet.")
    else:
        for s in student:
            name = input("Enter a name to search: ")
            if s["name"].lower() == name.lower():
                print("Name:", s["name"], "Age:", s["age"], "Marks:", s["marks"])
                new_marks = int(input("Enter updated marks: "))
                if new_marks <= 0:
                    print("Marks cannot be zero or negative")
                else:
                    s["marks"] = new_marks
                break
            else:
                print("Student not in our Records")


print("Student Management Console System App")
print("Select the following:\nA: Add a new student\nB: View All students\nC: Search a student by name\nD: Update marks of a student\nE: Exit")

while True:
    command = input("Enter any one of the option: ").lower()

    if command == "a":
        add_student()
    elif command == "b":
        view_students()
    elif command == "c":
        search_student()
    elif command == "d":
        update_marks()
    elif command == "e":
        print("Student Management Console App Closed")
        break
    else:
        print("Invalid input")
