#!/usr/bin/python
#coding=utf-8
from dytt8.dytt8 import dytt8
from xunbo.xunbo import xunbo
from mythread    import mythread

dytt8 = dytt8(5)

#print "开始抓取迅播前三页的电影链接。。。"
#xunbo = xunbo(3)

print "begin print"

ftp_urls = mythread(dytt8)
file = open('test.txt','w+')
for ftp_url in ftp_urls:
	file.write((ftp_url + '/n').encode('utf-8'))
file.flush()
file.close()
