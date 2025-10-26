#!/usr/bin/python3
"""Script that fetch 10 hot post for a given subreddit."""
import requests


def top_ten(subreddit):
    """Return number of subscribers if @subreddit is valid subreddit.
    if not return 0."""
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        if response.status_code == 200:
            data = response.json()
            children = data.get('data').get('children')
            
            for i in range(10):
                title = children[i].get('data').get('title')
                print(title)
        else:
            print(None)
    except:
        print(None)
