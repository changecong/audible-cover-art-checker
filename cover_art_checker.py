######################################################################
## Filename:      cover_art_checker.py
## Copyright:     2014, Zhicong Chen
## Version:       
## Author:        Zhicong Chen <zhicong.chen@changecong.com>
## Created at:    Wed Jul 30 20:31:45 2014
## Modified at:   Thu Jul 31 11:00:00 2014
## Modified by:   Zhicong Chen <zhicongc@audible.com>
## Status:        Experimental, do not distribute.
## Description:   This is a small tool that used to check if cover arts
##                of Audible audio books exist
##
#####################################################################

import sys
import urllib2
from bs4 import BeautifulSoup 
import threading

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

    def book_file_name_checker(self, sys_argvs):

        if not sys_argvs:
            return INVALID_ARGV
    
        if len(sys_argvs) != 2:
            return INVALID_ARGV_NUM

        file_name = sys_argvs[1]

        # check if the file exist
        import os
        file_exists = os.path.isfile(file_name)
        if file_exists:
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


    def check_cover_art(self):
        
        
        len_asins = 30
        total_asins = 0
        thread_num = 0


        all_asins = []


        file = open(self.__filename);

        while 1:
            line = file.readline()
            all_asins.append(line)
            if not line:
                break
        # create a new thread
        
        total_asins = len(all_asins)
        
        thread_num = total_asins / len_asins
        #print thread_num
        #sys.exit(0)
        print str(total_asins) + " asins in Total"
        print str(len_asins) + " asins in each group"
        
        if total_asins % len_asins != 0:
            thread_num = thread_num + 1

        print str(thread_num) + " groups"
        
        for thread_id in range(thread_num):

            if len(all_asins) < len_asins:
                asins = all_asins
            else:
                asins = all_asins[0: len_asins]
                all_asins = all_asins[len_asins : ]

            thread = AudibleThread(thread_id, asins)
            thread.start()

        
class AudibleThread(threading.Thread):

    '''
    threadID - the id of the current thread
    asins    - a list of asins

    '''
    def __init__(self, threadID, asins):
        threading.Thread.__init__(self)
        self.__threadID = threadID
        self.__asins = asins
        self.__url_base = "http://www.audible.com/search/ref=?advsearchKeywords="

    def run(self):
        # run the task
        print "Thread-" + str(self.__threadID) + " start."
        self.check_cover_art()
        print "Thread-" + str(self.__threadID) + " end."
        # print self.__asins

    def check_cover_art(self):
        
        for asin in self.__asins:

            # assemble the url
            url = self.__url_base + asin

            # load the page
            page = urllib2.urlopen(url)
            soup = BeautifulSoup(page)

            image_url = ''

            try:
                search_result = soup.find("ul", class_='adbl-search-results')
                search_result_soup = BeautifulSoup(str(search_result))
                image_url = search_result_soup.find("img", class_='adbl-prod-image')['src']
                # print image_url
            except:
                print "Exception: " + asin + "may be an invalid ASIN"
            
            # <img alt="The Hobbit, Part 1 | J. R. R. Tolkien" class="adbl-prod-image" src="http://ecx.images-amazon.com/images/I/51Xek6+7QwL._SL150_.jpg"/>
        
            # a fast way to verify is to check if there is "audilb" in the image src
            # print asin + " : " + image
            

            key_word = "Audible"

            no_image = image_url.find(key_word)

            # if the keyword is found
            if no_image != -1:
                print asin + " <--- Yes!!! Find it"
                print image_url


if __name__ == '__main__':

    # check the validity of the book list file then return the vilad file name 
    book_util = BookUtil()

    booklist = book_util.book_file_name_checker(sys.argv);

    print booklist
    app_util = Utility()

    if booklist is INVALID_ARGV:
        app_util.display_help()
        sys.exit(0)
    elif booklist is INVALID_FILE_NAME:
        app_util.display_invalid_name()
        sys.exit(0)

    # check if the book has a cover art
    app_util = AudibleUtil(booklist)
    app_util.check_cover_art()
