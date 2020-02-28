import requests

# #r = requests.get("https://xkcd.com/353/")
# r = requests.get("https://imgs.xkcd.com/comics/python.png")
#
# # with open('comic.png', 'wb') as f:
# #     f.write(r.content)
#
#
# print(r)
# #print(r.content)
# print(r.status_code)
# print(r.ok)
# print(r.headers)

#payload = {'page': 2, 'count': 25}
#r = requests.get("https://httpbin.org/get", params=payload)

#payload = {'username': 'Nagi', 'password': 'testing'}
#r = requests.post("https://httpbin.org/post", data=payload)

#r = requests.get('https://httpbin.org//basic-auth/Nagi/Testing', auth=('Nagi', 'Testing'))

r = requests.get('https://httpbin.org/delay/6', timeout=3)

print(r)
print(r.ok)
print(r.text)
print(r.url)

print(r.json())
#print(r.json()['form'])