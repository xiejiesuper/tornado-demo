# -*- coding: cp936 -*-


import urllib2,urllib,cookielib
'''
baiduMainLoginUrl = 'http://127.0.0.1:8000/signup'
postDict ={
    "userID": "15616825117",
    "password": "sbvgdebfb",
    "username": "fgn",
    '_xsrf':'3e78be3a80604ffaa04271347f6b645290'#从cookie中获取
}
postData = urllib.urlencode(postDict);
req = urllib2.Request(baiduMainLoginUrl, postData);
req.add_header("Cookie","_xsrf=3e78be3a80604ffaa04271347f6b645290;user=cnRoZnJ0aHRy|1426251342|daa90b681812dfd998d2140ff0a0ce74a22e9fa9;");
resp = urllib2.urlopen(req);
print resp.read()

'''
url = 'http://127.0.0.1:8000/index'
req = urllib2.Request(url, None);
req.add_header("Cookie","user=118024498|ddf056d4628bac467d8bc7c4f6221d07578c9894");
a = urllib2.urlopen(req);
print a.read()
