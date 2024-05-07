#!/usr/bin/python3
'''Querying the Reddit API to return the top ten hot posts'''
import requests


def top_ten(subreddit):
    '''A function that queries the Reddit API and prints the titles of the
    first 10 hot posts for a given subreddit.

    Args:
        subreddit (str): subreddit to use for querying top ten hot posts
    Returns:
        Titles of top 10 hot posts
    '''
    url = 'https://api.reddit.com/r/'
    headers = {'User-Agent': 'my-custom-header/0.0.1'}

    response = requests.get(
        f'{url}{subreddit}/hot?limit=10', headers=headers,
        allow_redirects=False
        )
    if response.status_code != 200:
        print('None')
    else:
        dictionary = response.json()
        hot_10 = dictionary.get("data", {})
        hot_10_children = hot_10.get("children", [])
        if len(hot_10_children) == 0:
            print('None')
        for data in hot_10_children:
            top_ten_data = data.get("data")
            print(top_ten_data.get("title"))
