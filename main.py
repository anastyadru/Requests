import requests

headers = {
    "User-Agent": "IT OVERONE"
}

response = requests.post("https://httpbin.org/get", headers=headers, params={'a': 'b'})


print(response.text)
