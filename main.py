import requests

website = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(website, data={
    "userld": 12,
    "title": "my new post",
    "body": "body for my post"
})

print(response.text)