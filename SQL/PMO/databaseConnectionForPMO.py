import mysql.connector

#
# # host,database name ,username ,password
#
# conn = mysql.connector.connect(host='localhost', database='PythonAutomation', user='root', password='1414')
# print(conn.is_connected())  # to check connection
from PMO.utilities.configurations import getConnection

conn = getConnection()
print(conn.is_connected())