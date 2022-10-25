import requests

response = requests.get("https://httpbin.org/get")

if response.statuc_code == 200:
    print("")

print(response)
