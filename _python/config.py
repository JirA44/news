import os
import requests
from pytz import timezone
from datetime import datetime, timedelta

def fetch_issues(repo_owner, repo_name, token=None):
    """Fetch issues from GitHub API"""
    # Base URL for GitHub API
    base_url = "https://api.github.com/issues"
    
    # Set up headers with token if provided
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v4+json'
    }
    
    # Initialize response
    response = requests.get(base_url, headers=headers)
    
    # Process the JSON response
    issues = []
    if response.status_code == 200:
        data = response.json()
        for issue in data['issues']:
            # Extract relevant details
            title = issue['title']
            body = issue['body']
            # Add to list of issues
            issues.append({
                'title': title,
                'body': f"{issue['number']}. {body}"
            })
    return issues

# Example usage
issues_list = fetch_issues("Seo", "RegisterSec", "your_token")
for issue in issues_list:
    print(f"Title: {issue['title']}")  # Replace with actual content