#!/usr/bin/env python3
"""Retrieve and print words fro any URL

Usage:
    python3 words.py <URL>


"""

import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list of words from a URL

    Args:
        URL which can be passed via command line

    Returns:
        Return a list of words from given URL
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('UTF-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_items(items):
    for item in items:
        print(item)


def main(url):
    word = fetch_words(url)
    print_items(word)


if __name__ == '__main__':
    main(sys.argv[1]) # 0th argument is the module filename




