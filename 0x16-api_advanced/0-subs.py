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
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'MyUbuntu/1.0 (Linux; U; en-US; Python)'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Raise an exception for HTTP errors

        data = response.json().get('data', {})
        subscribers = data.get('subscribers', 0)
        return subscribers
    except requests.RequestException as e:
        print(f'Error making request: {e}')
        return 0
    except ValueError as e:
        print(f'Error parsing JSON: {e}')
        return 0
    except KeyError as e:
        print(f'Error accessing data: {e}')
        return 0
