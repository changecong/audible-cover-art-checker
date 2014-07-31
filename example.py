######################################################################
## Filename:      example.py
## Copyright:     2014, Zhicong Chen
## Version:       
## Author:        Zhicong Chen <zhicong.chen@changecong.com>
## Created at:    Wed Jul 30 22:06:54 2014
## Modified at:   Thu Jul 31 10:39:42 2014
## Modified by:   Zhicong Chen <zhicongc@audible.com>
## Status:        Experimental, do not distribute.
## Description:   
##
#####################################################################

import urllib2
from bs4 import BeautifulSoup

# url = "http://www.audible.com/search/ref=?advsearchKeywords=B0030EJV3U"
url = "http://www.audible.com/search/ref=?advsearchKeywords=B002UUKMM4"
# url = "http://www.audible.com/search/ref=?advsearchKeywords=B007IKJYT8"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page)

#image = soup.find("img", class_='adbl-prod-image')['src']
#print image

search_result = soup.find("ul", class_='adbl-search-results')
print search_result
search_result_soup = BeautifulSoup(str(search_result))
image = search_result_soup.find("img", class_='adbl-prod-image')['src']


key_word = "Audible"
no_image = image.find(key_word)
# if the keyword is found                                                                                                                                                                            
if no_image != -1:
    print image
