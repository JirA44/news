import os
from datetime import datetime
from urllib.parse import urljoin

def get_github_issues(repo_name, token=None):
    """Fetch GitHub issues for a specific repo"""
    base_url = "https://api.github.com/issues"
    page = 1
    max_page = 50  # Limit to prevent infinite loops
    
    while page <= max_page:
        url = f"{base_url}?per_page=100&page={page}&is_merged=false"
        response = requests.get(url, headers={"Authorization": f"token {token}"} if token else {})
        
        if not response.status_code == 200:
            raise Exception(f"Error fetching issues: {response.status_code}")
        
        # Process each issue
        for item in response.json().get("items", []):
            # Check if it's a real issue (not merged)
            if not item["merged"]:
                # Simulate a commit to track the bug
                os.system(f"git add src/RegisterSec.py && git commit -m 'Fix {item['title']}')"
                
        page += 1

# Example usage
if __name__ == "__main__":
    get_github_issues("RegisterSec", "303f06e3")  # Replace with actual token and repo name