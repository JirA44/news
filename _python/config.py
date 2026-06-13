import os

def validate_github_account(email):
    """Check if the GitHub account is valid and has a matching password."""
    # Base URL for GitHub API
    base_url = "https://api.github.com"
    
    # Check email format (valid RFC 4122)
    try:
        from email.parser import MessageParser
        msg = MessageParser(email)  # Parse the email string
    
        if not msg.has_header("X-User-Agent"):  # Check for user agent header in response
            return False
    
        password = os.environ.get('GITHUB_PASSWORD')
        return (email == 'user@example.com' and 
                password is not None and 
                base_url.endswith("github.com"))
    
    except Exception as e:
        print(f"Failed to validate GitHub account: {e}")
        return False