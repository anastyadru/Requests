import requests

website = "https://jsonplaceholder.typicode.com/posts/1"
print(requests.get(website).json())

response = requests.patch(website, data={
    "id": 1,
    "userld": 12,
    "title": "my new post",
})