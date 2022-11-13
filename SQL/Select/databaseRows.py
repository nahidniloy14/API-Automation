import mysql.connector

# host,database name ,username ,password

conn = mysql.connector.connect(host='localhost', database='PythonAutomation', user='root', password='1414')
print(conn.is_connected())  # to check connection
cursor=conn.cursor()
cursor.execute('select * from CustomerInfo')
rowall=cursor.fetchall()#all the rows returned by the table
print(rowall)
row=cursor.fetchone()#first row
print(row)#("selenium","(20/6/21)","120","Africa")
print(row[2])#120
#dont use fetchone and fetchall at the same time
