import csv

with open('C:\\Users\lm\PycharmProjects\API\API AUTOMATION\\Utilities\loan.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  # name,status "," is delimiter
    Name = []
    Status = []
    for row in csvReader:
        # print(row)
        #     # ['Name', 'Status']
        #     # ['Antu', 'PAID']
        #     # ['Niloy', 'NOT PAID']
        #     # ['Piyas', 'PAID']
        #     # ['Haider', 'NotPaid']
        Name.append(row[0])
        Status.append(row[1])
print(Name)  # ['Name', 'Antu', 'Niloy', 'Piyas', 'Haider']
print(Status)  # ['Status', 'PAID', 'NOT PAID', 'PAID', 'NotPaid']
Index = Name.index('Antu')
loanStatus = Status[Index]
print('Loan Status is ' + loanStatus)
