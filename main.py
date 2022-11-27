import requests

website = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(website, data={
    "userld"
})

print(response.text)