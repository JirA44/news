import os
import requests

def fetch_issues(repo_owner, repo_name, token=None):
    """Fetch GitHub issues for the repository"""
    headers = {'Authorization': f'Bearer {token}'}
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching issues: {response.status_code}")