import requests


headers = {}
url = ''
r = requests.get(url, headers=headers)
print(r.status_code)
print(r.history)
print(r.encoding)
print(r.text)
