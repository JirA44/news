# local config only

from github import Github
import datetime

def get_github_issues(repo_owner, repo_name, token=None):
    """Fetch open issues from GitHub API"""
    # Simulated GitHub API for demonstration purposes
    if not token:
        raise ValueError("Token is required to access GitHub")
    
    # Placeholder for actual API call logic
    response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}", headers={'Authorization': f'token {token}'})
    if response.status_code != 200:
        raise ValueError(f"Failed to fetch issues: {response.text}")
    
    return response.json()