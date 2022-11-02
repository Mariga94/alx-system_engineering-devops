#!/usr/bin/python3
""""Query the reddit apu and print the titles of the first
    10 hot posts"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "my-app.0.1"
            }
    payload = {
            "limit": 10
            }
    res = requests.get(url, headers=headers, params=payload)
    if res.status_code == 404:
        print("None")
        return
    results = response.json().get("data")
    [print(h.get("data").get("title")) for h in results.get("children")]
