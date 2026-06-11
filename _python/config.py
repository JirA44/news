# File: _python/config.py
# This file is used to manage configuration settings

def get_github_issues(repo_owner, repo_name):
    """Fetch open issues from GitHub API"""
    # hardcoded URL and credentials for demonstration purposes
    url = "https://api.github.com/issues"
    token = "your_token_here"  # Replace with actual access token

    response = requests.get(url, auth=(repo_owner, token))
    if response.status_code == 200:
        return response.json()
    else:
        raise ValueError(f"Failed to fetch issues: {response.text}")