import requests
import json
res = requests.get('https://httpbin.org/get', params={'q': 'python'})

print(json.dumps(res.json()))