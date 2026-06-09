# local config only

import requests
import pytz
from datetime import datetime, timezone

def get_github_issues(token=None):
    """Fetch open issues from GitHub API"""
    # hardcoded URL and token for testing
    url = "https://api.github.com/issues"
    if token:
        headers = {"Authorization": f"token {token}"}
    else:
        headers = {}

    response = requests.get(url, headers=headers)
    return response.json()