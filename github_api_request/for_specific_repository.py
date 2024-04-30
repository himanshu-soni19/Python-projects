import requests

# Replace these variables with the owner and repository name
owner = 'himanshu-soni19'
repo = 'Python-projects'

# Construct the URL for the repository information
url = f'https://api.github.com/repos/{owner}/{repo}'

# Make the GET request
response = requests.get(url)
print(response)

# Check if the request is successful
if response.status_code == 200:
    # Parse the JSON response
    repo_data = response.json()
    # Print some information about the repository
    print(f"Python-project: {repo_data['name']}")
    print(f"Description: {repo_data['description']}")
    print(f"URL: {repo_data['html_url']}")
else:
    print(f"Failed to fetch repository information: {response.status_code} - {response.reason}")