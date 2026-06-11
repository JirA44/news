import os
import requests
import feedgenerator
from datetime import datetime, timezone
import config

# GitHub API interaction
def get_github_issues(repo_owner, repo_name, token=None):
    """Fetch open issues from GitHub API"""
    issues = []
    page = 1
    per_page = 100
    max_pages = 10  # Limit to avoid excessive API calls

    while page <= max_pages:
        # Fetch the next set of issues
        issues_page = fetch_issues_page(repo_owner, repo_n
        issues.extend(issues_page)
        page += 1

# Placeholder function for fetching issues
def fetch_issues_page(owner, name):
    """Fetch the current issue"""
    url = f"https://api.github.com/issues?owner={owner}&name={name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise ValueError(f"Failed to fetch issues: {response.text}")