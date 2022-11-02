#!/usr/bin/python3
"""Recursive function that queries the Reddit Api and
   return a list containing the titles of all hot
   articles foe a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    url = "https://www/reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "my-app.0.1",
            }
    payload = {
            "after": after,
            "count": count,
            "limit": 100
            }
    response = requests.get(url, headers=headers, params=payload)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for h in results.get("children"):
        hot_list.append(h.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
