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
