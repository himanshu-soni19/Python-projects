import requests
import json

username = "himanshu-soni19"
url = f"https://api.github.com/users/{username}"
response = requests.get(url)
user_data = response.json()

repos_url = user_data['repos_url']
repos_response = requests.get(repos_url)
repos_data = repos_response.json()

for project in repos_data:
    print(f"Project Name: {project['name']}\nProject Url: {project['html_url']}\n")
