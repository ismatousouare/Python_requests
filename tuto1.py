import requests
r = requests.get('https://restcountries.com/v3.1/name/guinea')
print(r.status_code)
print(r.text)
