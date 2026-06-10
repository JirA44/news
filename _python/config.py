import os
import requests
from datetime import datetime, timezone

# GitHub API interaction parameters
repo_owner = "SecOpsNews"
repo_name = "RegisterSec"
token = "your_github_token_here"

def fetch_issues(page=1, per_page=20):
    """Fetch issues from GitHub API"""
    headers = {"Authorization": f"token {token}"}
    
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues?page={page}&per_page={per_page}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error fetching issues: {response.status_code}")

# Simulated GitHub API to fetch issues
issues = fetch_issues()

for issue in issues:
    print(f"Issue #{issue['number']} - Title: {issue['title']}")