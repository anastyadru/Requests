import requests

headers = {
    "User-Agent": "IT OVERONE"
}

response = requests.get("https://httpbin.org/get", headers=headers, params={})


print(response.text)
