import csv

with open('C:\\Users\lm\PycharmProjects\API\API AUTOMATION\\Utilities\loan.csv','a') as csvFile:#a stands for append
    csvWriter = csv.writer(csvFile)
    csvWriter.writerow(["Nabil","PAID"])
    #make sure to close the excel before append