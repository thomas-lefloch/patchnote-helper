import requests

url = "https://www.pathofexile.com/forum/view-thread/3883495"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36 Edg/143.0.0.0"

response = requests.get(url, headers = {"User-Agent" : user_agent})

print (response.content)