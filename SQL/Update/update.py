import mysql.connector

# host,database name ,username ,password

conn = mysql.connector.connect(host='localhost', database='PythonAutomation', user='root', password='1414')
print(conn.is_connected())  # to check connection
cursor=conn.cursor()
#method 1: Directly from mySQL

#method 2:
cursor.execute("update apidevelop.customerinfo set Location = 'USA' where CourseName = 'Jmeter';")
conn.commit()

#method 3 : locating string using %s
# query="update apidevelop.customerInfo set Location =%s where CourseName = %s"
# data=("UK","Jmeter")
# cursor.execute(query,data)
# conn.commit()#after update we have to commit in connection level
