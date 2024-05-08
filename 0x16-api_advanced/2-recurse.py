#!/bin/usr/python3
'''Queries the Reddit API and returns a list containing the titles of all
hot articles for a given subreddit recursively
'''
import requests


def recurse(subreddit, hot_list=[], after=''):
    '''Recursively queries the Reddit API and returns a list containing
    the title of all hot articles for a given subreddit.

    Args:
        subreddit (str): Subreddit to query.
        hot_list (optional): List to store the titles.
        after (optional): The after param for pagination.
    Returns:
        list: List containing the titles of all hot articles or None
        of no results are found.
    '''
    url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-custom-header/0.0.1'}

    response = requests.get(
        f'{url}{subreddit}/hot?after={after}', headers=headers,
        allow_redirects=False
        )

    if response.status_code != 200:
        return None

    dictionary = response.json()
    data = dictionary.get("data")
    posts = data.get("children")
    after = data.get("after")

    for post in posts:
        store_in_hot_list = post.get("data")
        hot_list.append(store_in_hot_list.get("title"))

    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list if hot_list else None
