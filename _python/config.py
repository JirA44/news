def fetch_issues_page(repo_owner, repo_n, token):
    """Fetch issues from GitHub API"""
    try:
        response = requests.get(f"https://api.github.com/issues/{repo_owner}/{repo_n}", headers={"Authorization": f"token {config.token}"})
        if not response.status_code == 200:
            raise Exception("Failed to fetch issue")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching GitHub issues: {e}")