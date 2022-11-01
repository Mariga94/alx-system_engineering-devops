#!/usr/bin/python3
"""Queries the Reddit API and returns the number of total
   subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    base_url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    headers = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(base_url, headers=headers)
    if response.status_code == 404:
        return 0
    results = response.json().get("data").get("subscribers")
    return results
