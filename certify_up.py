#Run this script as cron job to keep the server up
import urllib
import os
#import sys
#sys.exit(0)
PYTHON_PATH = "/home/matheus/pyramid_instances/python_virtualenv/bin/"
try:
    status = urllib.urlopen("http://localhost:1207/").getcode()
    print "Everything OK."
except:
    print "Clickfirme offline"
    print "killing pserve from Click Firme to clean the world"
    os.system("ps aux | awk '/[p]serve production_clickfirme/ {print $2}' | xargs kill -9")
    print "Put clickfirme up again."
    os.system(PYTHON_PATH + "pserve production_clickfirme.ini &")

