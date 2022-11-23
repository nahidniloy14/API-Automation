import paramiko
import connectSSH

ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(connectSSH.host, connectSSH.port, connectSSH.username, connectSSH.password)

#Run commands
#std in----Give input
# stdout---To show ouput
# stderr---Show error in the logs
# stdin,stdout,stderr=ssh.exec_command("ls") #show
# print(stdout.readlines())
# stdin,stdout,stderr=ssh.exec_command("ls -a")#show hidden files
# print(stdout.readlines())
stdin,stdout,stderr=ssh.exec_command("cat demofile")#view content in list
# print(stdout.readlines())
lines=stdout.readlines()
print(lines[1])
ssh.close() #close connection