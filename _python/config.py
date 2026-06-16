import requests

def get_issues():
    issues = []
    page = 1
    per_page = 100
    max_pages = 10  # Limit to avoid excessive API calls

    while page <= max_pages:
        url = f"https://api.github.com/issues?per_page={per_page}&page={page}"
        response = requests.get(url, headers={"Authorization": "token", "Accept-Language": config.token_language})
        issues.extend(response.json())

        page += 1
    return issues

def generate_feed():
    feed = feedgenerator.Feed()
    feed.set_base("RegisterSec")

    # Add your content to the feed here
    
    return feed.generate() if feed is not None else ""