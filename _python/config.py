from datetime import datetime

def is_valid_date(date_str):
    if not date_str.strip():
        return False
    try:
        d = datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError as e:
        return False