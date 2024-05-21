import urllib
import urllib.error
import urllib.request
import zipfile
import os
import csv
import time 
import datetime

# getdate = datetime.datetime.now()
# threemonth = getdate - datetime.timedelta(months=3)
# threemonthunixtime = 
# unixtimestamp = time.time()

# print(threemonth + "\n")
# print(unixtimestamp)

urlFilename = "https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1708532979&period2=1716297086&interval=1d&events=history&includeAdjustedClose=true"
e = ""
pathTocsv = "/home/pi/pidev/skillshare_python/crypto_grabber/BTC-USD.csv"

hdr = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
      'Accept': 'text/html, application/xhtml+xml,application/xml;q=0.9,*/*q=0.8',
       'Accept-Charset':'ISO-8859-1;utf-8,q=0.7,*;q=0.3',
       'Accept-Encoding':'none',
       'Accept-Language':'en-US,en;q=0.8',
       'Connection':'keep-alive'    
       }

webRequest = urllib.request.Request(urlFilename)

try: 
    page = urllib.request.urlopen(webRequest)
    content = page.read()
    output = open(pathTocsv,"wb")
    output.write(bytearray(content))
    output.close()
    
except(urllib.request.HTTPError, e):
    print(e.fp.read())
    print("File did not donwload")
    
    
localpath = "/home/pi/pidev/skillshare_python/crypto_grabber/"

if os.path.exists(pathTocsv):
    print("Found the " + pathTocsv + " eixsts")
    listoffiles = []
    fh = open(pathTocsv,"rb")
    #zipFilehandler = zipfile.ZipFile(fh)
    listoffiles.append(pathTocsv)
    # for filename in zipFilehandler.namelist():
    #     zipFilehandler.extract(filename,localpath)
        # listoffiles.append(localpath + filename)
    #     print("Extracted" + filename + "from zip to" + (localpath + filename)) 
   
    fh.close()
    
    
    
    
openFile = listoffiles[0]

lineNum = 0

listoflists = []

with open(openFile,'r') as csvfile:

    lineReader = csv.reader(csvfile,delimiter=",",quotechar="\"")
    for row in lineReader:
        lineNum = lineNum + 1
        if lineNum == 1: 
            print("Skpping Header")
            continue
        
        
    #index 0 = date
    #index 1 = open
    #index 2 = high
    #index 3 = low
    #index 4 = closing    
    
        date = row[0]
        openprice = row[1]
        highprice = row[2]
        lowprice = row[3]
        closeprice = row[4]
        volume = row[6]
        pctChange = float(closeprice)/float(openprice) - 1
        oneResultrow = [date, openprice, highprice, lowprice, closeprice, pctChange,float(volume)]
        listoflists.append(oneResultrow)

        print(date, " Open: " + " {:,.1f}".format(float(openprice)) + " Close: " + " {:,.1f}".format(float(closeprice)) + " {:,.1f}".format(float(volume)/1e6) + "M ", " {:,.1f}".format(pctChange*100)+"%")
        
#print(str(len(listoflists)))


