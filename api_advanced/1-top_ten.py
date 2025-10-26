#!/usr/bin/python3
import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit. If the subreddit is invalid (e.g., results 
    in a redirect or 404), it prints OK.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Reddit API requires a custom User-Agent header to prevent rate limiting
    headers = {
        'User-Agent': 'alx_reddit_app/1.0 by MyUserAgentName'
    }
    
    params = {
        'limit': 10
    }

    try:
        # Crucial part: allow_redirects=False ensures we don't follow redirects,
        # which is the behavior for invalid subreddits that redirect to search.
        response = requests.get(
            url, 
            headers=headers, 
            params=params, 
            allow_redirects=False,
            timeout=5
        )

        # A valid response should be 200 OK and not a redirect (3xx) or error (4xx/5xx)
        if response.status_code != 200:
            print("OK")
            return

        # Attempt to parse the JSON response
        data = response.json()
        
        # Traverse the JSON structure to get the list of posts
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            
            # Print the title for each of the top 10 posts
            for post in posts:
                if 'title' in post.get('data', {}):
                    print(post['data']['title'])
        else:
            # Handle cases where the status is 200 but the JSON structure is unexpected
            print("OK")

    except requests.exceptions.RequestException:
        # Handle connection errors, DNS errors, timeouts, etc.
        print("OK")
    except ValueError:
        # Handle JSON decoding errors (if the response is not valid JSON)
        print("OK")


if __name__ == '__main__':
    # This block is for testing and mirrors your provided main.py logic
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
