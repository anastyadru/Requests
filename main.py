import requests

website = "https://jsonplaceholder.typicode.com/posts"
response = requests.post(website)

print(response.text)