import urllib2

#proxy = "61.233.25.166:80"
proxy = "YOUR_PROXY_GOES_HERE"

proxies = {"http":"http://%s" % proxy}
url = "http://www.google.com/search?q=test"
headers={'User-agent' : 'Mozilla/5.0'}

proxy_support = urllib2.ProxyHandler(proxies)
opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
urllib2.install_opener(opener)

req = urllib2.Request(url, None, headers)
html = urllib2.urlopen(req).read()
print html


###### 2 #####
import requests
s = requests.Session()
s.proxies = {"http": "http://61.233.25.166:80"}

r = s.get("http://www.google.com")
print(r.text)


