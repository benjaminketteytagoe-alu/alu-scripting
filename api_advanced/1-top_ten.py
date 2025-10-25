#!/usr/bin/python3
"""
Module that queries the Reddit API and prints the titles
of the first 10 hot posts for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query
        
    Returns:
        None: Prints titles or None if subreddit is invalid
    """
    if not subreddit or not isinstance(subreddit, str):
        print(None)
        return
    
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        'User-Agent': 'python:reddit.api.advanced:v1.0.0 (by /u/yourname)'
    }
    params = {
        'limit': 10
    }
    
    try:
        response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False,
            timeout=10
        )
        
        # Check if the request was successful and not redirected
        if response.status_code == 200:
            data = response.json()
            
            # Check if it's valid Reddit data structure
            if 'data' not in data or 'children' not in data.get('data', {}):
                print(None)
                return
                
            posts = data.get('data', {}).get('children', [])
            
            # Print each post title
            for post in posts:
                post_data = post.get('data', {})
                title = post_data.get('title')
                if title:
                    print(title)
        else:
            # Invalid subreddit or redirect
            print(None)
            
    except Exception:
        print(None))
