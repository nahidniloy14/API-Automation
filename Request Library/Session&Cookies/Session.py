import requests
Gitsession=requests.session()
Gitsession.auth=auth=("nahidniloy14","1414") #globaly creted it will apply to all github relatded URL's

url="https://api.github.com/user"
authResponse=requests.get(url,verify=False,auth=("nahidniloy14","1414"))

url2="https://api.github.com/orgs/AIUB/repos"#dummy
authResponse2=Gitsession.get(url2)
#this will have the knowledge of authentication


url3="https://api.github.com/orgs/AIUB/repos"#dummy
authResponse3=Gitsession.post(url3)
#this will have the knowledge of authentication




