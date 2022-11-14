import requests
visitYearSession=requests.session()
visitYearSession.cookies.update({"visit-year":"2021"})
# url2="http://httpbin.org/cookies"
# visitYearCookie={"visit-year":"2021"}
# response2=requests.get(url2,cookies=visitYearCookie)
# print(response2.text)

url="http://httpbin.org/cookies"
visitMonthCookie={"visit-month":"March"}
response=visitYearSession.get(url,cookies=visitMonthCookie)
print(response.status_code)
print(response.text)
#output:
# {
#   "cookies": {
#     "visit-month": "March",
#     "visit-year": "2021"
#   }
