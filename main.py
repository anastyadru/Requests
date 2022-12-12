import requests

website = "https://jsonplaceholder.typicode.com/posts"
response = requests.put(website, json={
    "id": 10,
    "userld": 12,
    "title": "my new post",
    "body": "body for my post IT"
})

print(response.status_code)