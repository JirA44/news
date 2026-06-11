# local config only

import os

def get_github_issues():
    """Fetch open issues from GitHub API"""
    token = os.getenv("GITHUB_TOKEN")
    repo_owner = "secopsnews"
    repo_name = "RegisterSec"

    issues = []

    page = 1
    per_page = 100
    max_pages = 20

    while page <= max_pages:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues?page={page}&per_page={per_page}"
        response = requests.get(url, headers={"Authorization": f"token {token}"})

        if response.status_code == 200:
            issues.extend(response.json())
        else:
            print(f"Error fetching issue #{page}: {response.text}")
        page += 1

    return issues

# Main application
if __name__ == "__main__":
    issues = get_github_issues()
    for issue in issues:
        print(issue["title"])