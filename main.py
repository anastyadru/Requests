import requests

website = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(website, json={
    "userld": 12,
    "title": "my new post",
    "body": "body for my post IT",
    "photo":
})

print(response.text)