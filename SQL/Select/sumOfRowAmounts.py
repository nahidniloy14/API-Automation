import mysql.connector

# host,database name ,username ,password

conn = mysql.connector.connect(host='localhost', database='PythonAutomation', user='root', password='1414')
print(conn.is_connected())  # to check connection
cursor=conn.cursor()
cursor.execute('select * from CustomerInfo')
rows=cursor.fetchall()#all the rows returned by the table
print(rows)#120 45 99 76 21
#dont use fetchone and fetchall at the same time
print(type(rows))
sum=0
for i in rows:
    sum=sum+rows[2]
print(sum) #361
conn.close()
