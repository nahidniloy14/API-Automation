import configparser


def getConfig():
    config = configparser.ConfigParser()  # this config variable can now drive all our ini files
    config.read("SQL/PMO/utilities/properties.ini")  # copy the path of the ini file
    return config