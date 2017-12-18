import requests
import bs4

# First we use requests to geta Reponse from the LoGec website
# This web script will generate a list of top 1000 working economic papers
# ranked by downloads according to REPEC ranking

page = requests.get("https://logec.repec.org/scripts/itemstat.pf?topnum=1000&type=redif-paper&sortby=ld&.submit=New+List")

# Note that page is a requests Response object.

try:
    page.raise_for_status() # Making sure the download went smoothly
except Exception as exc:
    print('There was a problem: %s' % (exc))


rawPage = bs4.BeautifulSoup(page.text, "html.parser") # BeautifulSoup 4 HTML parser

rawList=rawPage.select(".rightmost a") # creates a list, rawList, that contains all links inside the table

def cleanTheData(original): 
    masterList=[]
    for item in rawList:
        a=item.get('href')
        b=item.get_text()
        if a[1:8] == unicode("scripts"):
            masterList.append((a,b))
    return masterList

linkList=cleanTheData(rawList)



