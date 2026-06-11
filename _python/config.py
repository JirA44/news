[RegisterSec] _python/config.py
# local config only

# Fetch issues from GitHub API (simulated)
def get_github_issues(repo_owner, repo_name):
    """Fetch open issues from GitHub API"""
    issues = []
    page = 1
    per_page = 50
    max_pages = 3  # Limit to avoid excessive API calls

    while page <= max_pages:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
        response = requests.get(url, headers=config.GITHUB_TOKEN_HEADERS)
        issues_page = response.json()
        for issue in issues_page['items']:
            # Simulate a GitHub issue
            issue_id = issue['number']
            issue_number = f"{issue_id} - {issue['title']}"
            issues.append({
                "id": issue_id,
                "number": issue_number,
                "title": issue["title"],
                "created_at": datetime.now(pytz.timezone("UTC")).strftime("%Y-%m-%d %H:%M"),
                "url": f"https://github.com/{repo_owner}/{repo_name}/issues/{issue_id}"
            })
        page += 1
    return issues

# Fetch a new issue (simulate)
def fetch_issue(repo_owner, repo_name):
    """Fetch the next issue from GitHub API"""
    issue_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/next