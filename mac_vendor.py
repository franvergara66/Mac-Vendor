#!/python33/python
#Python 3 Example of how to use https://macvendors.co to lookup vendor from mac address
print ("Content-Type: text/html\n")

import urllib.request as urllib2
import json
import codecs

#API base url,you can also use https if you need
url = "http://macvendors.co/api/"
#Mac address to lookup vendor from
mac_address = "BC:92:6B:A0:00:01"

request = urllib2.Request(url+mac_address, headers={'User-Agent' : "API Browser"}) 
response = urllib2.urlopen( request )
#Fix: json object must be str, not 'bytes'
reader = codecs.getreader("utf-8")
obj = json.load(reader(response))

#Print company name
print (obj['result']['company']+"<br/>");

#print company address
print (obj['result']['address']);
