#!/usr/bin/python3
"""0-subs.py"""
import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns
    the number of subscribers for a given subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'custom'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json()['data']['subscribers']
