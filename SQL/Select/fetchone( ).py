import mysql.connector

# host,database name ,username ,password

conn = mysql.connector.connect(host='localhost', database='PythonAutomation', user='root', password='1414')
print(conn.is_connected())  # to check connection
cursor=conn.cursor() #it will help me to genarate a stream line connection with database
cursor.execute('SELECT * FROM apidevelop.customerinfo;') #execute database which I connected
#rows=cursor.fetchall()#all the rows returned by the table
rows=cursor.fetchone()# will return the first row
print(rows)#('selenium', datetime.date(2022, 11, 15), 120, 'Africa')
print(rows[3]) #africa
conn.close()
