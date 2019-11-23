import requests


def get_ip():
    """Get my current external IP."""
    return str(requests.get("https://icanhazip.com").content.strip())
