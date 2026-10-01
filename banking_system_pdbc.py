import MySQLdb
con = MySQLdb.connect(
    host="localhost",
    user="root",
    password="avinash",
    database="db103r"
)
c = con.cursor()
def create_table():
    sql = """CREATE TABLE IF NOT EXISTS emp1(empid INT PRIMARY KEY,e_name VARCHAR(20),
        e_salary FLOAT,j_date DATE DEFAULT(CURRENT_DATE))"""
    c.execute(sql)
    con.commit()
    print("Table created successfully")
def insert_data():
    empid = int(input("Enter employee id: "))
    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    sql = "INSERT INTO emp(empid,e_name,e_salary) VALUES(%s,%s,%s)"
    c.execute(sql, (empid, name, salary))
    con.commit()
    print("Data inserted successfully")
def update_data():
    empid = int(input("Enter employee id: "))
    salary = float(input("Enter new salary: "))
    sql = "UPDATE emp SET e_salary=%s WHERE empid=%s"
    c.execute(sql, (salary, empid))
    con.commit()
    print("Data updated successfully")
def delete_data():
    empid = int(input("Enter employee id: "))
    sql = "DELETE FROM emp WHERE empid=%s"
    c.execute(sql, (empid,))
    con.commit()
    print("Data deleted successfully")
while True:
    print("\n1. Create Table")
    print("2. Insert Data")
    print("3. Update Data")
    print("4. Delete Data")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_table()
    elif choice == 2:
        insert_data()
    elif choice == 3:
        update_data()
    elif choice == 4:
        delete_data()
    elif choice == 5:
        print("Exiting...")
        break
    else:
        print("Invalid choice")
con.close()