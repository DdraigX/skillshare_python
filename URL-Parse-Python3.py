
# coding: utf-8

# In[2]:

import urllib.request
import sys
# these import statements allow us to use 'modules' aka 'libraries' ....
# code written by others that we can use


# In[3]:

urlToRead = 'http://www.google.com'
# This value won't actually get used, because of the way the while loop 
# below is set up. But while loops often need a dummy value like this to 
# work right the first time


# In[4]:

crawledWebLinks = {}
# Initialize an empty dictionary, in which (key,value) pairs will 
# correspond to (shortname, url) eg ("Google" , "http://www.google.com")


# In[7]:

# OK, there's a while loop coming up now
while urlToRead !='':
    try:
        urlToRead = input("Please enter the next URL to crawl")
        if urlToRead == "":
            print("OK, exiting loop")
            break 
        shortName = input("Please enter a short name for that URL "+ urlToRead)
        webFile = urllib.request.urlopen(urlToRead).read()
        # This line above uses a readymade function in the urllib2 module to
        # do something super - cool: 
        # IT takes a url, goes to the website for that url, downloads the 
        # contents (which are in the form of HTML) and returns them to be 
        # stored in a string variable (here called webFile)
        crawledWebLinks[shortName] = webFile
        # this line above places a key value pair (shortname, HTML for that url)
        # in the dictionary
    except:
        # this bit of code - the indented lines following 'except:' will be 
        # executed if the code in the try block (the indented lines following)
        # the 'try:' above) throw and error
        # this is an example of something known as exception-handling, on which 
        # much more later
        print("********************\nUnexpected Error****",sys.exc_info()[0])
        # The snip 'sys.exc_info()[0]' returns information about the last 
        # error that occurred - 
        # this code is made available through the sys library that we imported above. 
        # Quite Magical :) 
        stopOrProceed = input("Hmm..stop or proceed? Enter 1 to stop, enter anything else to continue")
        if stopOrProceed =="1" : 
            print("Okey-dokey....stopping\n")
            break
            # this break will break out of the nearest loop - in this case, 
            # the while loop
        else: 
            print("Cool! Let's continue\n")
            continue
            # this continue will skip out of the current iteration of this 
            # loop and move to the next i.e. the loop will reset to the start
    print("Note this indentation - this line is inside the while loop, but outside the try/catch block")
print(" Note this indentation - this line is entirely outside the loop ")
print(crawledWebLinks.keys())

# Okey - dokey.... wow that was a lot of code. Now let's hit shift enter
# and hope this code executes the way we expect it to


# In[ ]:



