#post technique 4
import json

import requests

data = {'username':'nahidniloy14'}
res = requests.post ('https://httpbin.org/post',data=json.dumps(data))
print ( res.text )
