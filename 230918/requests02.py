import requests

# GET
response = requests.get("http://www.example.com/posts")

# 상태코드
status_code = response.status_code

if status_code == 200:
    data = response.json()
    for post in data:
        print(post['title'])
    
else:
    print(f"Error: {response.text}")
