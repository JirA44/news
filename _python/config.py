[RegisterSec] _python/feed-generator.py
import os
import requests
from datetime import datetime

def fetch_issues_page(repo_owner, repo_name, token):
    # Simulated GitHub API call to get issues (no real backend)
    page = 1
    per_page = 100
    max_pages = 10

    while True:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues?page={page}&per_page={per_page}"
        response = requests.get(url, headers={"Authorization": token})
        
        if not response.ok:
            print("Error fetching issues:", response.status_code)
            return None
        
        issues = []
        for i in range(len(response.json()) - 1):
            issue_data = response.json()[i]
            title = f"Issue #{issue_data['number']}"
            date = datetime.now(pytz.timezone('UTC'))
            if not issue_data.get('merged'):
                # Assume this is a bug
                issues.append({
                    'title': title,
                    'date': date.strftime("%Y-%m-%d %H:%M"),
                    'status': "unresolved",
                    'description': f"Bug in V8: {issue_data['summary']}"
                })
            else:
                # Assume this is a feature
                issues.append({
                    'title': title,
                    'date': date.strftime("%Y-%m-%d %H:%