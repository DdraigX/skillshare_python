import urllib
import urllib.error
import urllib.request
import time 
import zipfile, os
import sqlite3
from datetime import datetime

conn = sqlite3.connect('crypto_stock.db')
c = conn.cursor()

c.execute('CREATE TABLE prices (SYMBOL text, SERIES text, OPEN real, HIGH real, LOW, real, CLOSE real, LAST real, PREVCLOSE real, TOTTRDQTY real, TOTTRDVAL real, TIMESTAMP date, TOTALTRADES real, ISIN text, PRIMARY KEY (SYMBOL, SERIES, TIMESTAMP))')

conn.commit()


