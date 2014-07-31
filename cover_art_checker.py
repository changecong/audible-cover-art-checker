######################################################################
## Filename:      cover_art_checker.py
## Copyright:     2014, Zhicong Chen
## Version:       
## Author:        Zhicong Chen <zhicong.chen@changecong.com>
## Created at:    Wed Jul 30 20:31:45 2014
## Modified at:   Wed Jul 30 23:00:03 2014
## Modified by:   Zhicong Chen <zhicong.chen@changecong.com>
## Status:        Experimental, do not distribute.
## Description:   This is a small tool that used to check if cover arts
##                of Audible audio books exist
##
#####################################################################

import sys
import urllib2
from bs4 import BeautifulSoup 


# a list of error code
INVALID_ARGV = "invalid_argv"
INVALID_ARGV_NUM = "invalid_number_of_argv"
INVALID_FILE_NAME = "invalid_file_name"

class Utility:

    def __init__(self):
        self.__app_name = sys.argv[0]
        self.__file_name = ""
        if len(sys.argv) < 2:
            self.__file_name = "No file name provided."            
        elif len(sys.argv) > 2:
            self.__file_name = "Too many file names provided. One file only."
        else:
            self.__file_name = sys.argv[1] + " - File does not exist."

    '''
    Display help message
    '''
    def display_help(self):

        print "USAGE:"
        print self.__app_name + " <filename>"


    def display_file_name(self):
        print "Invalid file name : " + self.__file_name



'''

'''

class BookUtil:

    def book_file_name_checker(sys_argvs):

        if not sys_argvs:
            return INVALID_ARGV
    
        if len(sys_argvs) != 2:
            return INVALID_ARGV_NUM

        file_name = sys_argvs[1]

        # check if the file exist
        import os
        file_exits = os.path.isfile(file_name)
        if file_exist:
            return file_name
        else:
            return INVALID_FILE_NAME


class AudibleUtil:

    '''
    A sample of search url
    http://www.audible.com/search/ref=?advsearchKeywords=<ASIN>
    '''

    def __init__(self, filename):
        
        self.__filename = filename
        

        # construct a url

        # page = urllib2.urlopen('http://www.leeon.me');


    def check_cover_art():
        
        # create a new thread
        


        
class AudibleThread(threading.Thread):

    def __init__(self, threadID, asin):
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__asin = asin
        self.__url_base = "http://www.audible.com/search/ref=?advsearchKeywords="

    def run(self):
        # run the task
        check_cover_art()
        

    def check_cover_art():
        
        # assemble the url
        url = self.__url_base + self.__asin

        # load the page
        page = urllib2.urlopen(url)
        soup = BeautifulSoup(page)

        image = soup.find("img", class_='adbl-prod-image')['src']
        
        # <img alt="The Hobbit, Part 1 | J. R. R. Tolkien" class="adbl-prod-image" src="http://ecx.images-amazon.com/images/I/51Xek6+7QwL._SL150_.jpg"/>
        
        # a fast way to verify is to check if there is "audilb" in the image src

        key_word = "Aubible"

        no_image = image.find(key_word)

        if no_image != -1:
            print self.__asin


if __name__ == '__main__':

    # check the validity of the book list file then return the vilad file name 
    booklist = BookUtil.book_file_name_checker(sys.argv);
    app_util = AppUtil()

    if booklist is INVALID_ARGV:
        app_util.display_help()
        sys.exit(0)
    elif booklist is INVALID_FILE_NAME:
        app_util.display_invalid_name()
        sys.exit(0)

    # check if the book has a cover art
    app_util = AudibleUtil(booklist)
    app_util.check_cover_art()
