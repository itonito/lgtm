from urllib import request, parse, error
import json
query = parse.urlencode({'q': 'python'})

url = f'https://httpbin.org/get?{query}' 
try:
    with request.urlopen(url) as f: 
        res = f.read().decode('utf-8')
except error.HTTPError as e:
    print(e)
print(res)