import os
import requests

def get_issue_title(repo_owner, repo_name):
    # GitHub API interaction
    issue_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
    
    response = requests.get(issue_url)
    
    if response.status_code == 200:
        return response.json()[0]["title"]
    else:
        return "No issue found"

# Fetch the title of an issue
issue_title = get_issue_title("303f06e3", "RegisterSec")
print(f"The issue's title is: {issue_title}")