import requests

website = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(website, data={
    "userld":12,
})

print(response.text)