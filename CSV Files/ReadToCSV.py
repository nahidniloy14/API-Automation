import csv
with open('C:\\Users\lm\PycharmProjects\API\API AUTOMATION\\Utilities\loan.csv') as csvFile:
    csvReader = csv. reader (csvFile, delimiter=',')#name,status "," is delimiter
    print(csvReader)#<_csv.reader object at 0x000001227E5210C0>
    print(list(csvReader))#[['Name', 'Status'], ['Antu', 'PAID'], ['Niloy', 'NOT PAID'], ['Piyas', 'PAID'], ['Haider', 'NotPaid']]
