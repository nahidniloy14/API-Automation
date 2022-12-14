import csv

import paramiko as paramiko
from Utilities.configuration import getConfig


# Set Connection
username = getConfig()['Paramiko+AWS[Linux Server] Server']['username']
password = getConfig()['Paramiko+AWS[Linux Server] Server']['password']
host = getConfig()['Paramiko+AWS[Linux Server] Server']['host']
port = getConfig()['Paramiko+AWS[Linux Server] Server']['port']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
#--------Upload Files--------
sftp=ssh.open_sftp()#this method is used to file transfer
destinationPath="loan.csv"
localPath="Utilities/BatchJobsLoan.csv"
sftp.put(localPath,destinationPath)#it will push the files in the aws environment

sftp=ssh.open_sftp()#this method is used to file transfer
destinationPath="script.py"
localPath="Utilities/script.py"
sftp.put(localPath,destinationPath)#it will push the files in the aws environment


#Trigger Batch Jobs

stdin,stdout,stderr=ssh.exec_command("python script.py")#writing python is not mendatory if it is installed in your aws machine
print(stdout.readlines())

#Download the file to loacl system
sftp.get("loan.csv","Utilities/BatchJobsLoanUpdated.csv")

#parse Output to CSV
with open('Utilities/BatchJobsLoanUpdated.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')  # name,status "," is delimiter
    Name = []
    Status = []
    for row in csvReader:
        if row[0]=="Antu":
            assert row[1] == "PAID"
