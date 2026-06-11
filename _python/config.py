# Fetch issues from GitHub API with hardcoded credentials and URL

import os
import requests

def fetch_issues(repo_owner, repo_name):
    """Fetch open issues from GitHub API"""
    base_url = "https://api.github.com/issues"
    token = "your_token_here"  # Replace with your actual access token

    headers = {"Authorization": f"token {token}"}
    
    url = f"{base_url}/{repo_owner}/{repo_name}"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None