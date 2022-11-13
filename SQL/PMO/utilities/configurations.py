import configparser
import mysql.connector


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


connect_config = {
    'user':getConfig()['SQL']['user'],
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


