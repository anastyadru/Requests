import requests

response = requests.get("https://httpbin.org/get")

headers = {"User-Agent": }

#if response.statuc_code == 200:
    #print("OK")

response.raise_for_status()

print(response)
