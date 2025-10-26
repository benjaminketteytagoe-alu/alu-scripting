#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, print None."""
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data.get('data', {}).get('children', [])

        for post in children:
            title = post.get('data', {}).get('title')
            print(title)
    else:
        print(None)
