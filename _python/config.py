import requests

def get_recent_commits():
    response = requests.get("https://api.github.com/repos/your-repo.git/commits")
    return response.json()