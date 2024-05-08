#!/usr/bin/python3
'''Querying the Reddit API to return the total number of subscribers'''
import requests


def number_of_subscribers(subreddit):
    '''A function that queries the Reddit API and returns the number of
    subscribers for a given subreddit

    Args:
        subreddit (str): subreddit to use for querying total subscribers
    Returns:
        (int) total number of subscribers to the subreddit
        (int) 0 if not a valid subreddit
    '''
    # GET /r/subreddit/about
    # Return information about the subreddit.
    # Data includes the subscriber count, description, and header image.
    url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-custom-header/0.0.1'}

    response = requests.get(
        f'{url}{subreddit}/about', headers=headers, allow_redirects=False
        )
    if response.status_code != 200:
        return 0
    dictionary = response.json()
    data = dictionary.get("data")
    return data.get("subscribers")
