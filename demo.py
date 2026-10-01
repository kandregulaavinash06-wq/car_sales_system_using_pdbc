import MySQLdb
con=MySQLdb.connect(user='root',host='localhost',password="avinash")
#if you dont know database exist or not the use
#sql="create database if not exist pdbc_103r"
sql="create database db103r"
c=con.cursor()#api db per
c.execute(sql)
con.close()








