import requests
url="https://api.github.com/user"
authResponse=requests.get(url,auth=("nahidniloy14","1414"))#(url,auth=(username,password))
print(authResponse.status_code)
#https related websites may impose some ssl certifictaion .when accessing those it may give us error to avoid those errors ,verify=false can help
authResponse=requests.get(url,verify=False,auth=("nahidniloy14","1414"))#(url,auth=(username,password))
# SSL stands for Secure Sockets Layer, a standard security protocol that enables encrypted communication between a client (web browser) and a server (webserver). Transport Layer Security (TLS) is the successor protocol to SSL.
# SSL certificates are data files hosted by the server that makes SSL encryption possible.They contain the server’s public key and identity.The SSL certificates are digital certificates issued by a legitimate third - party Certificate Authority, confirming the identity of the certificate owner.Whenever you visit a website whose URL starts with HTTPS, it means the server has SSL enabled.Before the web browser fetches the data from the server, it fetches the SSL certificates to verify the identity of the server.
#SSL helps to keep sensitive information like usernames, passwords, credit cards, etc.secure by encrypting the data between the client and the server.You need SSL for three reasons: privacy, integrity, and identification.
