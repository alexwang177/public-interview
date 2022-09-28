import requests 
from requests.exceptions import HTTPError

res = requests.get('https://platform.brexapis.com/interview/test', params={"foo": "bar"}, headers={'Accept': 'application/json'})
print(res.json())
print(res.headers)
print(res.status_code)
print(res.content)
print(res.text)


