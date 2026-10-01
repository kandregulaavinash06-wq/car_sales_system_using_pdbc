# # import MySQLdb
# # # con=MySQLdb.connect(user='root',host='localhost',password="avinash",database="db103r")
# # # sql='''create table emp(empid int,e_name varchar(20),
# # # e_salary float,j_data date default(current_date))'''
# # # c=con.cursor()#api db per
# # # c.execute(sql)
# # # con.close()

# # con=MySQLdb.connect(user='root',host='localhost',password="avinash",database="db103r")
# # sql='''insert into emp (empid,e_name,e_salary) values (101,'avinash',50000.57)'''
# # c=con.cursor()#api db per
# # c.execute(sql)
# # con.commit()
# # con.close()

# import MySQLdb

# con = MySQLdb.connect(
#     user='root',
#     host='localhost',
#     password='avinash',
#     database='db103r'
# )

# c = con.cursor()

# count = 0

# while True:
#     empid = int(input("Enter employee ID: "))
#     name = input("Enter employee name: ")
#     salary = float(input("Enter employee salary: "))

#     sql = '''INSERT INTO emp (empid, e_name, e_salary)
#              VALUES (%s, %s, %s)'''

#     c.execute(sql, (empid, name, salary))
#     con.commit()
#     count += 1
#     print(count, "record added")
#     choice = input("Do you want to add another record? (y/n): ")
#     if choice.lower() != 'y':
#         break
# c.close()
# con.close()
