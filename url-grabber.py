import sys

import urllib.request

inputUrl = "http://www.google.com"

#dictionary 
crawledWebLink = {}

while inputUrl != '':
    try: 
        inputUrl = input("Please enter a url to parse\n")
        if inputUrl == "": 
            print("exiting loop")
            break
        
        
        urlName = input("Enter url name" + inputUrl + "\n")
        webfile = urllib.request.urlopen(inputUrl).read()  #don't think this is going to work
        
        
        crawledWebLink[urlName] = webfile
    except: 
        print("Error",sys.exc_info()[0])
        
        stopOrgo = ("Press 1 to exit or any key to continue")
        if stopOrgo ==1 : 
            print("stopping")
            break
        else: 
            print("Continuing")
            continue
        
        
print(crawledWebLink.keys())



    
    
