import urllib
import urllib.error
import urllib.request
import zipfile
import os
import csv



urlFilename = "https://query1.finance.yahoo.com/v7/finance/download/BTC-USD?period1=1684506073&period2=1716128473&interval=1d&events=history&includeAdjustedClose=true"
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

# if os.path.exists(localpath):
#     print("Found the file" + localpath + "eixsts")
#     listoffiles = []
#     fh = open(localpath,"rb")
    

