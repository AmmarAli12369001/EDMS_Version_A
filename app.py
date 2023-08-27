import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="password", port="3306", database="python_edms")


def addEmployee():
    Id = int(input("Enter Employee Id:"))

    if check_employee(Id):
        print("Employee already exists.")
        menu()

    elif 10000 <= Id <= 99999:
        name = input("Enter Employee Name:")
        department = input("Enter Employee Department:")
        salary = int(input("Enter Employee Salary:"))
        date = input("Enter date of joining(MM/DD/YYYY):")
        data = (Id, name, department, salary, date)
        if 30000 <= salary <= 200000:
            sql = 'insert into employee values(%s,%s,%s,%s,%s)'
            c = con.cursor()

            c.execute(sql, data)

            con.commit()
            print("Employee Added.")
            menu()
        else:
            print("Salary is not within range.")
            menu()


def updateEmployee():
    Id = int(input("Enter Employee ID:"))

    if not check_employee(Id):
        print("Employee does not exist.")
        menu()
    else:
        amount = int(input("Enter new Salary:"))

        sql = 'select salary from employee where id=%s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        c.fetchone()

        sql = 'update employee set salary=%s where id=%s'
        d = (amount, Id)

        c.execute(sql, d)

        con.commit()
        print("Employee Updated.")
        menu()


def deleteEmploy():
    Id = input("Enter Employee ID:")

    if not check_employee(Id):
        print("Employee does not exist.")
        menu()
    else:

        sql = 'delete from employee where id=%s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        con.commit()
        print("Employee Removed.")
        menu()


def check_employee(employee_id):
    sql = 'select * from employee where id=%s'

    c = con.cursor(buffered=True)
    data = (employee_id,)

    c.execute(sql, data)

    r = c.rowcount
    if r == 1:
        return True
    else:
        return False


def displayEmployees():
    sql = 'select * from employee'
    c = con.cursor()

    c.execute(sql)

    r = c.fetchall()
    for i in r:
        print("Employee Id:", i[0])
        print("Employee Name:", i[1])
        print("Employee Department:", i[2])
        print("Employee Salary:", i[3])
        print("Employee Date of Joining", i[4])
        print("- - - - - - - - - - - - - - - - - - - - - -")
    menu()


def searchEmployee():
    Id = input("Enter Employee Id:")

    if not check_employee(Id):
        print("Employee does not exist.")
        menu()
    else:
        sql = 'select * from employee where id=%s'
        data = (Id,)
        c = con.cursor()

        c.execute(sql, data)

        r = c.fetchall()
        for Id in r:
            print("Employee Name:", Id[1])
            print("Employee Department:", Id[2])
            print("Employee Salary:", Id[3])
            print("Employee Date of Joining:", Id[4])
        menu()


def menu():
    print("1 to Add Employee")
    print("2 to Delete Employee")
    print("3 to Update Employee")
    print("4 to Display Employees")
    print("5 to Search Employee")
    print("6 to Exit")

    ch = int(input("Enter your Choice:"))
    if ch == 1:
        addEmployee()
    elif ch == 2:
        deleteEmploy()
    elif ch == 3:
        updateEmployee()
    elif ch == 4:
        displayEmployees()
    elif ch == 5:
        searchEmployee()
    elif ch == 6:
        exit(0)
    else:
        print("Invalid Input")
        menu()


menu()
