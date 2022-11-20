import configparser

import mysql
import mysql.connector

#JSON
def getConfig():
    config = configparser.ConfigParser()  # this config variable can now drive all our ini files
    config.read("Utilities/properties.ini")  # copy the path of the ini file
    return config


#SQL
connect_config = {
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password'],
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database'],
}


def getConnection():
    #conn = mysql.connector.connect(host='localhost', database='PythonAutomation', user='root', password='1414')
    #conn = mysql.connector.connect(**connect_config)#will specify that whatever argument we have is nothing but dictionary
    try:
        conn = mysql.connector.connect(**connect_config)
        if conn.is_connected():
            print("Connection OK")
            return  conn
    except configparser.Error as e:
        print(e)

#SQL.Integrate database using API
def getQuery():
    conn=getConnection()
    cursor=conn.cursor()
    cursor.execute()
    response=cursor.fetchone()
    return response