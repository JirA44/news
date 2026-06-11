import os
import requests
from pytz import timezone

def get_github_issues(repo_owner, repo_name, token=None):
    """Fetch issues from GitHub API"""
    headers = {"Authorization": f"token {token}" if token else ""}
    
    # Example URL: https://api.github.com/issues?per_page=20&page=1
    url = f"https://api.github.com/issues?per_page={per_page}&page={page}"
    
    response = requests.get(url, headers=headers)
    
    issues = []
    for item in response.json():
        if item["number"] < 0: continue  # Skip negative numbers
    
        # Add to the list
        issue = {
            "id": item["number"],
            "title": item["title"],
            "description": f"{item['body']} {item['link']}"
        }
        issues.append(issue)
    
    return issues

# Simulated GitHub API calls for demonstration purposes
def fetch_issues_page(repo_owner, repo_n):
    """Fetch the next page of issues"""
    response = requests.get(f"https://api.github.com/issues?per_page={10}&page={1}")
    if response.status_code != 200:
        raise ValueError("Failed to fetch issues")
    
    return response.json()