# dont use fetchone and fetchall at the same time
import mysql.connector

# host,database name ,username ,password

conn = mysql.connector.connect(host='localhost', database='APIdevelop', user='root', password='1414')
print(conn.is_connected())  # to check connection
cursor = conn.cursor()  # it will help me to genarate a stream line connection with database
cursor.execute('SELECT * FROM apidevelop.customerinfo;')  # execute database which I connected
rows = cursor.fetchall()  # all the rows returned by the table
# [('selenium', datetime.date(2022, 11, 15), 120, 'Africa'), ('Protractor', datetime.date(2022, 11, 15), 45, 'Africa')
# , ('Appium', datetime.date(2022, 11, 15), 99, 'Asia'), ('Jmeter', datetime.date(2022, 11, 15), 76, 'US')]
print(rows)  # list of tuples

# Print sum of all books
print(type(rows))
sum = 0
for i in rows:
    sum = sum + i[2]
print(sum)  # 340
conn.close()
