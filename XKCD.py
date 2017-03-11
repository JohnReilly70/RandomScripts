import re
import requests
import bs4
import urllib.request
import time


def xkcd_beautiful_soup():
    res = requests.get('http://xkcd.com')
    res.raise_for_status()
    regex = re.compile(r'https://xkcd.com/(\d+)/')
    page_total = re.findall(regex, res.text)
    skip_list = [404,1350,1416,1446,1608,1663]
    for page in range(1,int(page_total[0])+1):
        try:
            print(page)
            if page in skip_list:
                print(page," Skipped")
                continue
            res = requests.get('http://xkcd.com/{}/'.format(page))
            res.raise_for_status()
            soup = bs4.BeautifulSoup(res.text, "html.parser")
            image = (soup.find('div', attrs={'id': 'comic'}).img.get('src'))
            urllib.request.urlretrieve("http://xkcd.com/{}".format(image), "XKCD/beautiful_soup/{}.jpg".format(page))
            print("Complete: {}".format(page))
        except:
            print("Error on {}".format(page))
            continue

def xkcd_regex():
    res = requests.get('http://xkcd.com')
    res.raise_for_status()
    regex = re.compile(r'https://xkcd.com/(\d+)/')
    page_total = re.findall(regex, res.text)
    regex = re.compile(r'(https://imgs.xkcd.com/comics/.*)')
    for page in range(int(page_total[0]),0,-1):
        try:
            print("Starting: {}".format(page))
            res = requests.get('http://xkcd.com/{}/'.format(page))
            res.raise_for_status()
            re_image_link = re.findall(regex,res.text)
            urllib.request.urlretrieve(re_image_link[0], "XKCD/RE/{}.jpg".format(page))
            print("Complete: {}".format(page))
        except:
            print("Error on {}".format(page))
            continue
xkcd_regex()