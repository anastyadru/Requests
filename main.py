import requests

headers = {
    "User-Agent": "IT OVERONE"
}

response = requests.get("https://httpbin.org/get?a=b", headers=headers)


print(response.text)
