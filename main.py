import requests

website = "https://jsonplaceholder.typicode.com/posts/1"
print(response)

response = requests.delete(website, data={
    "id": 1,
    "userld": 12,
    "title": "my new post",
})