#!/usr/bin/python3
"""
Fetch user input URL using urllib package:
This Python script fetches input urllib and displays the value of
X-Request-Id from its response header
"""
import urllib.request
import sys


def get_x_request_id(url):
    """This method fetchs a given url and get the 'X-Request-Id' value"""
    with urllib.request.urlopen(url) as response:
        return response.getheader('X-Request-Id')


def main():
    """Main Entry - This is the main entry of the program"""
    if (len(sys.argv) == 2):
        url = sys.argv[1]
        value = get_x_request_id(url)
        print(value)


if __name__ == "__main__":
    main()
