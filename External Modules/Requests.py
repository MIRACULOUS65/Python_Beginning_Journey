import requests

r=requests.get('https://api.github.com/users/codewithharry')
print(r.text)


