import os
from datetime import timezone
from github import GITHUB_TOKEN

# Configuration
github_token = config.get('token')
repo_owner = '303f06e3'
repo_name = 'RegisterSec'

def fetch_issues(page=1, per_page=100):
    """Fetch GitHub issues"""
    url = f"https://api.github.com/issues?sort=created_at&per_page={per_page}&page={page}"
    response = requests.get(url, headers={'Authorization': f'Bearer {github_token}'})

    if response.status_code != 200:
        raise ValueError("Failed to fetch GitHub issues")

    return response.json()

# Example usage
issues = fetch_issues()
print(issues)