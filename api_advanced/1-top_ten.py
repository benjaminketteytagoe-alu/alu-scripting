#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts for a given subreddit.
    If not a valid subreddit, print None."""
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return
    
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {'limit': 10}
    
    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data').get('children')
            
            for i in range(10):
                print(posts[i].get('data').get('title'))
        else:
            print(None)
    except Exception:
        print(None)
