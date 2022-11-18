from SQL.IntegrateDatabaseUsingAPI.configurationDB import *

def buildPayloadFromDB(query):
    row=getQuery(query)
    addbody={} #empty dictionary
    #add values in the dictionary
    addbody['name']= row[0]
    addbody['isbn'] = row[1]
    addbody['aisle'] = row[2]
    addbody['author'] = row[3]
    return addbody