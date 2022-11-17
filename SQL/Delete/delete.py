import mysql.connector

# host,database name ,username ,password

conn = mysql.connector.connect(host='localhost', database='PythonAutomation', user='root', password='1414')
print(conn.is_connected())  # to check connection
cursor=conn.cursor()
#method 1: Directly from mySQL

#method 2:
cursor.execute("delete apidevelop.customerinfo where CourseName = 'Webservices';")
conn.commit()

#method 3 : locating string using %s
# query="update apidevelop.customerInfo where CourseName = %s"
# data=("Jmeter")
# cursor.execute(query,data)
# conn.commit()
#after delete we have to commit in connection level
