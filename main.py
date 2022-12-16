import requests

website = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.put(website, data={
    "id": 1,
    "userld": 12,
    "title": "my new post",
    "body": "body for my post IT"
})

print(response.json())