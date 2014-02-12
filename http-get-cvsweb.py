#!/usr/bin/python
#
# A simple script that logs into a CVSweb interface and downloads archived device configurations
# In this script we need revision 1 - 18, the files are then downloaded and saved with the revision
# number appended to the file
#
#
# Start


import sys
import urllib3
import httplib
import requests


#httplib.HTTPConnection.debuglevel = 1

print '====================================='
print ' Downloading Data....................'
print '====================================='

for x in range (1,19):
    url = requests.get('http://url/path/device-name?rev=1.' + str(x) + ';cvsroot=name', auth=('user', 'pass'))

    if url.status_code == 200:
       	with open('rancid-v1.' + str(x), 'wb') as f:
             print 'Saved file to rancid-v1.' + str(x)
             for chunk in url.iter_content():
                  f.write(chunk)

# End
