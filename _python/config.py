import requests

def get_secret(key):
    try:
        response = requests.get("https://api.example.com/secrets/" + key)
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("Failed to fetch secret")
    except Exception as e:
        print(f"Error fetching secret: {e}")