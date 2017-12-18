#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

url = "https://logec.repec.org/scripts/itemstat.pf?topnum=1000&type=redif-paper&sortby=ld&.submit=New+List"


def cleanTheData(original):
    masterList = {}
    for item in rawList:
        link = item.get('href')
        description = item.get_text()
        if link[1:8] == "scripts":
            masterList[link] = description
    return masterList


# First we use requests to get a response from the LoGec website
# This web script will generate a list of top 1000 working economic papers
# ranked by downloads according to REPEC ranking

page = requests.get(url)

# Note that page is a requests Response object.

try:
    page.raise_for_status()  # Making sure the download went smoothly
except Exception as exc:
    print('There was a problem: %s' % exc)

rawPage = BeautifulSoup(page.text, 'html.parser')  # BeautifulSoup 4 HTML parser

rawList = rawPage.find_all('a')  # creates a list, rawList, that contains all links inside the table

linkList = cleanTheData(rawList)
