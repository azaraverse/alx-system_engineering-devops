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
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'User-Agent': 'MyUbuntu/1.0 (Linux; U; en-US; Python)'}

    response = requests.get(url, headers=header, allow_redirects=False)
    if response.status_code != 200:
        return 0
    try:
        dictionary = response.json()
    except ValueError:
        return 0
    data = dictionary.get("data")
    if data:
        subscribers = data.get("subscribers")
        if subscribers:
            return subscribers
    return 0
