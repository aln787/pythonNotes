
#!/usr/bin/env python3
"""Example request to free quote api's

TODO:
- add fetch_details docstring
"""
#https://www.python.org/dev/peps/pep-0008/#documentation-strings
#https://www.python.org/dev/peps/pep-0257/

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

urls = { #https://github.com/public-apis/public-apis/blob/master/README.md#public-apis-
    "quotes": {
        "programming": "https://programming-quotes-api.herokuapp.com/quotes/random",
        "general": "https://quote-garden.herokuapp.com/api/v2/quotes/random",
        "trump": "https://www.tronalddump.io/random/quote",
        "general2": "https://favqs.com/api/qotd"}}

def fetch_quote(url):
    with requests.Session() as s:
        r = s.get(url)
    return r.json()

def format_quote(quote, author = ""):
    """Format Quote String
    
    Args:
        quote (str): The quote string.
        author (str): The author of the quote if avalible.

    Returns:
        str: The return value. This string includes the author if avalible.
    """
    if None in [quote, author]:
        raise Exception("The API response for your selected category appears to me malformed.")
    a = " -{}".format(author) if author != "" else "" 
    return quote + a

def get_user_selection(urls):
    """Get User Selection
    
    Prompt the user for the type of quote they are interested in seeing from the supported API's.
    
    Args:
        urls (dict): This dict contains the list of URLs and URL types
    
    return:
        str: This string indicates which option the user has selected
    """
    options = list(urls['quotes'].keys())
    selection = input("Enter one of the following opitions - {}: ".format(", ".join(options))).lower()
    print()
    if selection in options:
        url = urls["quotes"][selection]
        return selection, url
    else:
        print("value entered invalid")
        return get_user_selection(urls)

def fetch_details(selection, rj):
    if selection == "programming":
        quote  = rj.get('en')
        author = rj.get('author')
        r = format_quote(quote, author)
    elif selection == "general":
        quote  = rj.get('quote', {}).get('quoteText')
        author = rj.get('quote', {}).get('quoteAuthor')
        r = format_quote(quote, author)
    elif selection == "general2":
        quote  = rj.get('quote', {}).get('body')
        author = rj.get('quote', {}).get('author')
        r =  format_quote(quote, author)
    elif selection == "trump":
        author = rj.get("value")
        r = format_quote(author)
    else:
        print("handler not found: " + current)
    return r

def main():
    if input("Would you like to fetch a quote - y, n:").lower() == "y":
        selection, url = get_user_selection(urls)
        print(fetch_details(selection, fetch_quote(url)))
        main()
    else:
        print("exiting")

if __name__ == "__main__":
    main()

"""
notes
#Aleternative yo using .get() is to use a try catch on KeyErrors
##try:
##    quote  = rj['quote']['bodys']
##    author = rj['quote']['author']
##    r =  format_quote(quote, author)
##except KeyError as e:
##    print(e)
# -*- coding: utf-8 -*-
Free iOS shell and iOS Jupyter Notebook
- https://apps.apple.com/us/app/a-shell/id1473805438
- https://apps.apple.com/us/app/carnets-jupyter/id1450994949
"""
