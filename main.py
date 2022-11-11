import requests

headers = {
    "User-Agent": "IT OVERONE"
}

response = requests.get("https://httpbin.org/get", headers=headers, params={'a': ''})


print(response.text)
