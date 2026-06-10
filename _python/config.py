# Fetches issues from GitHub API
def get_github_issues(repo_owner, repo_name):
    # Simulated GitHub API call
    return [
        {
            "number": 69748,
            "title": "RegisterSec: [RegisterSec] Chrome's zero-day Whac-A-Mole continues with fifth exploited bug of the year",
            "description": "This is a test issue for demonstration purposes.",
            "status": "open"
        }
    ]

# Fetches all issues from GitHub API
def fetch_issues(repo_owner, repo_name):
    # Simulated fetching of issues
    return get_github_issues(repo_owner, repo_name)