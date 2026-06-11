import os
from datetime import timezone, timedelta
from pytz import timezone as local_tz

def fetch_issues(repo_owner, repo_name, token=None):
    """Fetch open issues from GitHub API"""
    # Simulated GitHub API response
    if token:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues"
        params = {
            "token": token,
            "page": 1,
            "per_page": 100,
            "sort": "created_at",
            "order": "asc"
        }
    else:
        url = "https://api.github.com/issues"
        params = {"page": 1, "per_page": 100}

    response = requests.get(url, params=params, headers={'Authorization': f'token {token}'})

    if not response.status_code == 200:
        raise Exception(f"Failed to fetch issues: {response.text}")

    issues = []
    for item in response.json():
        issue_id = item['number']
        title = item['title']
        created_at = item['created_at'].isoformat()
        # Example placeholder logic
        issues.append({
            'id': issue_id,
            'title': title,
            'created_at': created_at
        })

    return issues