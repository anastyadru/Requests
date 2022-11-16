import requests

headers = {
    "User-Agent": "IT OVERONE"
}

response = requests.post("https://httpbin.org/post",
                         headers=headers,
                         params={'a': 'b'},
                         json={'username': 'supersecret'})


print(response.text)
