---

// FILE: .github/ISSUE_TEMPLATE/user_feedback.md
---
name: User feedback
about: Provide your opinion about the project or the repository
title: ''
labels: ''
assignees: ''

---
**Describe what you think**
A clear and concise description of your thoughts.

**Additional context**
Add any other context here that might help explain your idea. For example, if there's a specific feature you're interested in, describe it briefly. If there's a problem with the project, provide feedback on how to fix it. If there's an issue with user experience, describe what users are facing and how it can be improved.

---
// FILE: .github/ISSUE_TEMPLATE/pull_request.md
---
name: Pull request
about: Describe your changes
title: ''
labels: ''
assignees: ''

---
**Your summary**
A clear and concise description of your changes.

**Changes you made**
- [ ] Added a function to fetch issues from GitHub
- [ ] Fixed the issue with the registry

# File: _python/config.py
import os
import requests
import pytz
from datetime import datetime, timezone
from .feed_generator import get_github_issues

def check_registry():
    """Check if there are any registry-related issues"""
    repo_owner = "secopsnews"
    repo_name = "RegisterSec"
    
    try:
        # Fetch all issues for the repository owner and its branch
        issues = get_g