# 5. Write a program anti_html.py that takes a URL as an argument, downloads the HTML from
# the web, and prints it after stripping HTML tags.

import sys
import requests
from bs4 import BeautifulSoup


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the HTTP response
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching HTML from {url}: {e}")
        sys.exit(1)


def strip_html_tags(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()


if len(sys.argv) != 2:
    print("Usage: python anti_html.py <URL>")
    sys.exit(1)

url = sys.argv[1]
html_content = get_html(url)
stripped_content = strip_html_tags(html_content)

print(stripped_content)
