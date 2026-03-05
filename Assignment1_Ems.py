employees={101:{"name":"Satya","age":27,"department":"HR","salary":50000},102:{"name":"Rahul","age":30,"department":"IT","salary":60000}}

def add_employee():
    emp_id=int(input("Enter Employee ID: "))
    if emp_id in employees:
        print("Employee ID already exists")
        return
    name=input("Enter Name: ")
    age=int(input("Enter Age: "))
    department=input("Enter Department: ")
    salary=float(input("Enter Salary: "))
    employees[emp_id]={"name":name,"age":age,"department":department,"salary":salary}
    print("Employee added successfully")

def view_employees():
    if not employees:
        print("No employees available")
        return
    print("ID\tName\tAge\tDepartment\tSalary")
    for emp_id,details in employees.items():
        print(emp_id,details["name"],details["age"],details["department"],details["salary"])

def search_employee():
    emp_id=int(input("Enter Employee ID: "))
    if emp_id in employees:
        emp=employees[emp_id]
        print("Name:",emp["name"])
        print("Age:",emp["age"])
        print("Department:",emp["department"])
        print("Salary:",emp["salary"])
    else:
        print("Employee not found")

def main_menu():
    while True:
        print("\nEmployee Management System")
        print("1 Add Employee")
        print("2 View Employees")
        print("3 Search Employee")
        print("4 Exit")
        choice=input("Enter choice: ")
        if choice=="1":
            add_employee()
        elif choice=="2":
            view_employees()
        elif choice=="3":
            search_employee()
        elif choice=="4":
            print("Thank you")
            break
        else:
            print("Invalid choice")

main_menu()