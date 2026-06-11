import os
import requests
from pytz import timezone

def fetch_issues(repo_owner, repo_name):
    """Fetch GitHub issues for a given repository"""
    base_url = "https://api.github.com"
    token = config.get_token()
    if not token:
        raise ValueError("No authentication token found")

    url = f"{base_url}/{repo_owner}/{repo_name}/issues?per_page={100}&page={1}"

    response = requests.get(url, headers={"Authorization": f"token {token}"}).json()

    return response["items"]

# Example usage
if __name__ == "__main__":
    repo_owner = "SecOpsNews"
    repo_name = "RegisterSec"
    issues = fetch_issues(repo_owner, repo_name)
    for issue in issues:
        print(issue["number"])