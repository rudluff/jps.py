#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys
import time

cookies = {'PHPSESSID':'01010101010replaceme010101'}

def scrape(arg):
    page = requests.get(arg, cookies=cookies)
    soup = BeautifulSoup(page.text, "lxml")

search_url = sys.argv[1]
page = requests.get(search_url, cookies=cookies)
soup = BeautifulSoup(page.text, "lxml")

pages = soup.find('div', class_="linkbox")
pages = [i for i in pages if i] 

# crufty way to locate maximum page number (i know it's stupid)
lastlink = pages[-1].attrs['href']
lastlink = lastlink[18:]
lastlink = lastlink.split("&")
lastlink = int(lastlink[0])

# go to page, grab urls to .torrent files, download those torrent files, go to next page, repeat
for pageno in range(1,lastlink):
    allthelinks = []
    arg = search_url + "page=" + str(pageno)
    scrape(arg)
    torrenttag = soup.find_all('a', {'title':'Download'})
    for link in torrenttag:
        allthelinks.append(link.attrs['href'])
    numberinpage = 0
    for link in allthelinks:
        filename = str(pageno) + "-" + str(numberinpage) + ".torrent"
        torrentfile = requests.get('https://jpopsuki.eu/' + link)
        file = open(filename, "wb")
        file.write(torrentfile.content)
        file.close()
        time.sleep(2.2)
        numberinpage = numberinpage+1
    print("Finished page " + str(pageno))
