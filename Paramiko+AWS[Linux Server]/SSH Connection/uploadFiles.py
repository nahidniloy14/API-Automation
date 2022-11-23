import paramiko
import connectSSH
#---------Set Paramiko+AWS[Linux Server] connection--------
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(connectSSH.host, connectSSH.port, connectSSH.username, connectSSH.password)
#--------Upload Files--------
sftp=ssh.open_sftp()#this method is used to file transfer
destinationPath="loan.csv"
localPath="Utilities\loan.csv"
sftp.put(localPath,destinationPath)#it will push the files in the aws environment
#----See Uploaded Files--------
stdin,stdout,stderr=ssh.exec_command("ls -a")#show hidden files
print(stdout.readlines())

ssh.close()

