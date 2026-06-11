import os
from datetime import datetime

# hardcoded GitHub credentials
github_user = "username"
github_token = "token"

def get_github_issues(repo_owner, repo_name):
    """Fetch open issues from GitHub API"""
    headers = {"Authorization": f"token {github_token}"}
    
    # First page
    response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues", headers=headers)
    issues_data = response.json()
    
    # Process each issue
    for issue in issues_data:
        # For the purpose of this example, we'll simulate a bug report
        if "fixed" in issue["pull_request"]["html"]:
            print(f"BUG REPORT: {issue['number']} - Fixed by GitHub")
        else:
            print(f"BUG REPORT: {issue['number']} - Not fixed yet")

    return issues_data

# Simulated API calls for the purpose of this example
def fetch_issues_page(repo_owner, repo_name):
    """Fetch next page of GitHub issues"""
    response = requests.get(f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues", headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("No more pages to fetch")