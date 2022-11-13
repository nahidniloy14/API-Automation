import requests
url='https://petstore.swagger.io/v2/pet/9843217/uploadImage'
imagefile={'file':open('Screenshot 2022-06-24 201029.PNG','rb')}
response= requests.post(url,files=imagefile)
print(response.status_code)
print(response.text)
#200
#{"code":200,"type":"unknown","message":"additionalMetadata: null\nFile uploaded to ./Screenshot 2022-06-24 201029.PNG, 105770 bytes"}
