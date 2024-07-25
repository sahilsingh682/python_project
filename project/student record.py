students = {}
def add_students(name, grade):
    students[name] = grade
    print(f"{name} added with grade {grade}")

def update_students(name, grade):
    if name in students:
        students[name] = grade
        print(f"{name} update with grade {grade}")
    else:
        print(f"{name} is not found in record")

def delete_students(name):
    if name in students:
        del students[name]
        print(f"{name} has been deleted seccessfully")
    else:
        print(f"{name} is not found in record")

def display_students():
    for name, grade in students.items():
        print("----------------------------")
        print(f"{name}:   {grade}")



def main():
    while True:
        print("1 : Add Record")
        print("2 : Update Record")
        print("3 : Delete Record")
        print("4 : Display Record")
        print("5 : Exit")
        choice = int(input("Enter the choice:"))
        if choice == 1:
            name = input("Enter the name of student:")
            grade = input("enter the grade of student:")
            add_students(name, grade)
        
        elif choice == 2:
            name = input("Enter the name of student:")
            grade = input("Enter the grade of student:")
            update_students(name, grade)

        elif choice == 3:
            name = input("Enter the name of student you want to delete:")
            delete_students(name)

        elif choice == 4:
            display_students()
            
        elif choice == 5:
            print("Record is closing")
            break
        else:
            print("invalid choice")

main()


