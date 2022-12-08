import requests

website = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(website, json={
    "userld": 12,
    "title": "my new post",
    "body": "body for my post IT",
    "photo": {"1.jpg", "2.jpg"}
})

print(response.text)