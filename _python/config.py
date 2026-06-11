import os
import requests

def get_github_issues(repo_owner, repo_name):
    """
    Fetch open issues from GitHub API.
    """
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}"
    }
    
    # Check if the repository exists and has public access
    response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}", headers=headers)
    
    if response.status_code == 200:
        issues = response.json()
        return issues
    else:
        raise Exception("Issue retrieval failed")