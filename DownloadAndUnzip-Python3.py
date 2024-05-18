
# coding: utf-8

# In[1]:

########################################################
# Step 1: Download
#######################################################

#import some standard modules we can use to download URLs


import urllib.request



# initialize a variable with the URL to download, from the website
# of the National Stock Exchange of India, which publishes each day a 
# bunch of interesting market data
urlOfFileName = "http://www.nseindia.com/content/historical/EQUITIES/2015/JUL/cm17JUL2015bhav.csv.zip"

urlOfFileName


# In[2]:

# initialize a variable with the local file in which to store the URL
# (this is a path on my local desktop)
localZipFilePath = "/Users/swethakolalapudi/Desktop/cm17JUL2015bhav2.csv.zip"

localZipFilePath

# Now a bit of boilerplate code to actually download the file. The website
# of the NSE does not like bots (automated scripts) that attempt to scrape
# data from it, so it will block scripts unless they have something called
# the user-agent property set in their HTTP headers. Don't worry too much
# about what this boilerplate code means, just go along with it:)

hdr = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*q=0.8',
       'Accept-Charset':'ISO-8859-1;utf-8,q=0.7,*;q=0.3',
       'Accept-Encoding':'none',
       'Accept-Language':'en-US,en;q=0.8',
       'Connection':'keep-alive'
      }


hdr


# In[6]:

# Now for the code that actually downloads the page and stores to file

# Make the web request - just use a web browser like Mozilla or Chrome would
# This is where the strange boilerplate code that we just typed out comes in handy
webRequest = urllib.request.Request(urlOfFileName,headers=hdr)

# Doing stuff with files is quite error-prone, so let's be careful and 
# use try/except as safety nets
try:
    # note that we are now inside the try loop, as the indentation shows
    page = urllib.request.urlopen(webRequest)
    # save the contents of this page into a variable called 'content'
    # These contents are literally the zip file from the URL (i.e. what 
    # we got when we just downloaded the file manually
    content = page.read()
    # Now save the contents of the zip file to disk locally
    # 1. Open the file (barrel)
    output = open(localZipFilePath,"wb")
    # the 'w' indicates that we intend to write, i.e. put stuff into the 
    # barrel. the 'b' indicates that this is a binary (not a text) file
    output.write(bytearray(content))
    # 2. In the line above, we actually write contents to the file. 
    # Note how the function bytearray - from python's libraries - 
    # knows how to convert this binary file into a bytearray that can
    # be written to file.
    output.close()
    # 3. The barrel (i.e. the file) is closed, sealed shut
except(urllib.request.HTTPError, e):
    # we are now in the 'except' portion of the try/except block. This
    # code will be executed only if an exception is thrown in the try block
    # i.e. if something goes wrong. 
    # Note how we specifically 'handle' exceptions of the type HTTPError
    print(e.fp.read())
    print("Looks like the file download did not go through, for url = ",urlOfFileName)


# In[8]:

####################################################################
# Step 2: Unzip the downloaded file and extract
####################################################################

import zipfile, os
#initialize a variable with the local directory in which to extract
# the zip file above
localExtractFilePath = "/Users/swethakolalapudi/Desktop/"



# check if the zip file above was downloaded successfully..if
# not, there is little point in trying to extract!
if os.path.exists(localZipFilePath):
    # we are inside the conditional, i.e. this code is indented
    # because it will only be executed if the condition is true,
    # i.e. if 'os.path.exists(localZipFilePath)' returns True
    print("Cool!" + localZipFilePath + " exists..proceeding")
    # A zip file can contain any number of files, we don't know
    # how many upfront - so initialize an empty array in which to save
    # the names of the files
    listOfFiles = []
    # Open the barrel, i.e. the zip file.
    fh = open(localZipFilePath,'rb')
    # Note the 'rb' above .. the 'r' signifies that we will read,
    # and the 'b' that this is a binary file.
    # Recall that binary files - unlike text files - need handlers
    # that know what to do with them - that is exactly what we will
    # use the zipfile library for.
    zipFileHandler = zipfile.ZipFile(fh)
    # zipFileHandler knows how to read the list of zipped up files 
    # Iterate over that list in a for-loop. 
    for filename in zipFileHandler.namelist():
        # the indentation has changed again - we are inside the for
        # loop, and the iterator variable is 'filename'
        zipFileHandler.extract(filename,localExtractFilePath)
        # let's add this to the list of files we have extracted
        listOfFiles.append(localExtractFilePath + filename)
        print("Extracted " + filename + " from the zip file to " + (localExtractFilePath + filename))
    # we are outside the for-loop now, hence the unindent
    print("In total, we extracted ", str(len(listOfFiles)), " files")
    fh.close()
    # Don't forget to close the file, ie to seal the barrel!
        


# In[10]:

###################################################################
# Step 3: Parse the extracted CSV and create a table of stock info
###################################################################

import csv
# import the CSV module, which knows how to do stuff with CSV files
# (Aside: CSV = Comma-Separated-Values, a file format in which each
# line is a list of values separated by commas). We need a handler 
# because there are edge cases (for instance cell values themselves
# containing commas) that the module knows how to handle.
oneFileName = listOfFiles[0]
# we know that the zip file downloaded has only file that we care about
# so access it using the indexing operator. Remember of course that
# arrays are indexed from zero.
lineNum = 0
# Keep a list of lists in which to store the output. For each stock,
# we care about a. how much that stock moved today (% change versus
# yesterday) and b. how heavily the stock was traded (the value that
# changed hands today)
listOfLists = []
# THis variable above will track the 3 columns we care about:
# ticker, % change and value traded
with open(oneFileName,'r') as csvfile:
    # note that the indent changed because of the 'with' operator
    # 'with' is a super-powerful construct that allows us to open a 
    # file and do stuff with it, and not worry about explicitly 
    # opening and closing the file. When the with block opens,
    # the file is explicitly opened, and when the with block ends,
    # the file is implicitly closed. BTW, note that the 'rb' indicates
    # that we only plan to read the file, and that we will use a handler
    # (which in this case is the csv library we imported above)
    lineReader = csv.reader(csvfile,delimiter=",",quotechar="\"")
    # The CSV handler (the csv.reader function) knows how to read
    # a csv file, 1 line at a time. This handler needs 2 bits of info
    # from us: (a) what delimiters are used to separate cell values (in
    # our case, and with all csvs, it is the ',' character) and (b) how
    # cell values that contain the separator will be special-cased. 
    # this is done in most csv files using quotes. Thus, if a cell inside
    # the file itself contains a comma, the entire cell value will be in
    # quotes.
    for row in lineReader:
        # the linereader can be iterated over, one line at a time
        lineNum = lineNum + 1
        # what line are we on? keep track so we can skip the header
        if lineNum == 1:
            print("Skipping the header row")
            continue
            # remember that continue will skip to the next line
            # in the for loop
        # Ok! Everything in life is a list. The CSV file is a list of 
        # lines, and each line is a list of words. We know from the 
        # header that:
        # column 1 (index = 0) is the stock ticker
        # column 6 (index = 5) is the last closing price
        # column 8 (index = 7) has yesterday's last closing price
        # column 10 (index = 9) has the traded value in India Rupees
        symbol = row[0]
        close = row[5]
        prevClose = row[7]
        tradedQty = row[9]
        pctChange = float(close)/float(prevClose) - 1
        oneResultRow = [symbol,pctChange,float(tradedQty)]
        # oneResulRow will look like this: ['SBI',0.034,100000.0]        
        listOfLists.append(oneResultRow)
        # listOfLists will look like this:
        # [ ['SBI',0.034,100000.0]  , ['AXISBANK',0.056,800900.0]   ]
        # we got hold of all the quantities that we care about for 
        # each stock, and created one row that we added into our
        # running result
        print(symbol, "{:,.1f}".format(float(tradedQty)/1e6) + "M INR", "{:,.1f}".format(pctChange*100)+"%")
    # the indent has changed, we are out of the for loop, but the 
    # last line of the for loop prints out a nicely formatted message.
    # Note that the "{:,.1f}".format helps to print nice comma-separated
    # numbers
    # btw, note that when we exit the with block, the file is automatically
    # closed
    print("Done iterating over the file contents - the file is closed now!")
    print("We have stock info for " + str(len(listOfLists)) + " stocks")


# In[11]:

####################################################################
# Step 4: Sort the list of lists!
####################################################################

# we have spent a lot of time talking about the power of for loops
# but Python has something even more powerful that is actually the 
# 'idiomatic' Python way of doing stuff: lambda functions.

# For now, let's just use a lambda function to sort our list of lists
# we won't go into a whole lot of detail about what lambda functions are,
# beyond saying that they are a way of saying 'Dear list, here is a function,
# please apply this function to each element of yourself'

# In general, in pure and true Python, the use of for loops is 
# minimized, and that of lambda functions is preferred. But our 
# objective in this class is to understand the basics of programming 
# via python, so we will continue with our way of doing stuff using 
# for loops

# After that long segue, back to the task at hand of sorting a list 
# of lists. 
listOfListsSortedByQty = sorted(listOfLists, key=lambda x:x[2], reverse=True)
# Here we sort the list of lists by column 3 (index = 2). The 
# reverse = True means that sort will be descending
listOfListsSortedByQty = sorted(listOfLists, key=lambda x: x[1], reverse=True)


listOfListsSortedByQty


# In[12]:

########################################################################
# Step 5: Write out an excel file with the summary of the top movers,
# and most heavily traded files
########################################################################

import xlsxwriter
# import the xlsxwriter library which does all the magic

excelFileName = "/Users/swethakolalapudi/cm17JUL2015bhav.xlsx"
# Initialize a variable with the name of the excel file we will create

workbook = xlsxwriter.Workbook(excelFileName)
# create a workbook. THis is analogous to opening the barrel
worksheet = workbook.add_worksheet("Summary")
# create a worksheet (empty) named 'Summary'

worksheet.write_row("A1",["Top Traded Stocks"])
worksheet.write_row("A2",["Stock","% Change","Value Traded (INR)"])
# the way to write stuff into the excel is by specifying
# a. the cell address eg "A1", in the standard excel format
# b. the list of values to be written, 1 per cell starting from that address


# Let's write out the 5 most heavily traded stocks
# we already have the stocks sorted by how much they were traded
# in the list of the first 5 numbers, starting from 0
# Do this using the range function. range(5) is python shorthand
# for a list of the first 5 numbers, starting from 0
# Thus, range(5) == [0,1,2,3,4]
# Set up a for loop over this list - the iterator variable is 
# called rowNum
for rowNum in range(5):
    # get the corresponding row from our sorted result
    oneRowToWrite = listOfListsSortedByQty[rowNum]
    # write this out to the excel spreadsheet
    # while doing this, remember to add 1 to the row number
    # why? because Excel arrays are indexed from 1 while python
    # arrays are indexed from 0
    worksheet.write_row("A" + str(rowNum + 3), oneRowToWrite)
# as the changed indentation tells us, we are done with the for loop
# Close the file (ie seal the barrel!)
workbook.close()


# In[ ]:



