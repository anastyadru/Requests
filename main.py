import requests

website = "https://jsonplaceholder.typicode.com/posts/1"
print(response.status_code)

response = requests.delete(website, data={
    "id": 1,
    "userld": 12,
    "title": "my new post",
})