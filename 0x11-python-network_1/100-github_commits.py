#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve following challenge

Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""
import sys
import requests


def main():
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    res = requests.get(url)
    results = res.json()
    try:
        for item in range(10):
            print("{}: {}".format(
                results[item].get("sha"),
                results[item].get("commit").get("author").get("name")))
    except IndexError:
        pass


if __name__ == "__main__":
    main()
