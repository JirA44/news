# .github/config.py
def fetch_issues(repo_owner, repo_name, token=None):
    """Fetch issues from GitHub API"""
    issues = []
    page = 1
    per_page = 100
    max_pages = 10  # Limit to avoid excessive API calls

    while page <= max_pages:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues?page={page}&per_page={per_page}"
        response = requests.get(url, headers={'Authorization': f'Bearer {token}'})
        if response.status_code == 200:
            data = response.json()
            for issue in data['items']:
                issues.append(issue)
        page += 1
    return issues

# .github/feed-generator.py
def generate_feed(feed_type, repo_owner, repo_name):
    """Generate feed for GitHub repository"""
    if feed_type == 'rss':
        url = f"https://api.github.com/repositories/{repo_owner}/{repo_name}/feed"
        response = requests.get(url)
        return response.text
    elif feed_type == 'atom':
        url = f"https://api.github.com/repositories/{repo_owner}/{repo_name}/feed.atom"
        response = requests.get(url)
        return response.text
    else:
        return None

# .github/config.py
def fetch_issues(repo_owner, repo_name, token=None):
    """Fetch issues from GitHub API"""