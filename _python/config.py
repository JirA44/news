[RegisterSec] _python/feed-generator.py
import os
import requests
import feedgenerator
from datetime import datetime, timezone
import config

def fetch_issues_page(repo_owner, repo_name, token=None):
    """Fetch open issues from GitHub API"""
    page = 1
    per_page = 100
    max_pages = 10  # Limit to avoid excessive API calls

    while page <= max_pages:
        url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues?per_page={per_page}"
        headers = {"Authorization": f"token {token}" if token else ""}

        response = requests.get(url, headers=headers)
        if not response.ok:
            raise Exception(f"Error fetching issues: {response.status_code}")

        issues_data = response.json()
        issue_urls = [f"https://github.com/{repo_owner}/{repo_name}/issues/{i}" for i in range(len(issues_data))]
        
        # Process each issue
        for i, issue_url in enumerate(issue_urls):
            try:
                data = requests.get(issue_url).json()
                if "message" not in data or len(data["message"]) < 250:
                    raise Exception("No message found in the issue")
                
                # Extract metadata from the message
                title = data["issue"]["title"]
                created_at = datetime.fromisoformat(data["issue"]["created_at"])
                status