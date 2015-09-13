#!/usr/bin/python


ott=0
orr=0

import sys,re,datetime

qual=(1,2)

def printtt(d,r,t):
	if(r<0 or t<0) : return
	print (('"%s";"%d";"%d"')%(d,r,t),)

def printT(d,r,t):
	if(r<0 or t<0) : return
	print (('{"date":%s,"rx":%d,"tx":%d,"link":%s,"level":%s},')%(d,r,t,qual[0],qual[1]))

def printQ(a,b):
	global qual
	qual=(a,b)




while 1:
	line = sys.stdin.readline()
	if not line : break
#for line in sys.stdin:
	m = re.search('(.*),(.*),(.*)', line)
	if(m):
		d=int(m.group(1))
		dd=datetime.datetime.fromtimestamp(d).strftime('%Y-%m-%d %H:%M:%S')
		r=int(m.group(2))
		t=int(m.group(3))
		printT (d,r-orr,t-ott)
		orr=r
		ott=t
	m = re.search('wlan0: 0000( *)([0-9]*). *(-[0-9]*). *(-[0-9]*).*([0-9]*) ',line)
	if(m):
		printQ(m.group(2),m.group(3))