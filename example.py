######################################################################
## Filename:      example.py
## Copyright:     2014, Zhicong Chen
## Version:       
## Author:        Zhicong Chen <zhicong.chen@changecong.com>
## Created at:    Wed Jul 30 22:06:54 2014
## Modified at:   Wed Jul 30 22:33:22 2014
## Modified by:   Zhicong Chen <zhicong.chen@changecong.com>
## Status:        Experimental, do not distribute.
## Description:   
##
#####################################################################

import urllib2
from bs4 import BeautifulSoup

url = "http://www.audible.com/search/ref=?advsearchKeywords=B0030EJV3U"
# url = "http://www.audible.com/search/ref=?advsearchKeywords=B002UUKMM4"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

print soup.find("img", class_='adbl-prod-image')['src']
