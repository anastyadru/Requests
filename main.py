import requests

headers = {
    "User-Agent": "IT OVERONE"
}

response = requests.post("https://httpbin.org/post",
                         headers=headers,
                         params={'a': 'b'},



print(response.text)
