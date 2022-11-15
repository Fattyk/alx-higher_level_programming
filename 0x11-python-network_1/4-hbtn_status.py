#!/usr/bin/python3
"""
Fetch URL using requests package:
This Python script fetches https://alx-intranet.hbtn.io/status using requests
"""
import requests


def fetch_url():
    """This method fetchs https://alx-intranet.hbtn.io/status using requests"""
    res = requests.get("https://alx-intranet.hbtn.io/status")
    return res.text


def main():
    """Main Entry - This is the main entry of the program"""
    body = fetch_url()
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")


if __name__ == "__main__":
    main()
