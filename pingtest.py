#!/usr/bin/env python
import subprocess
ping = 'ping'
arg = '-c'
count ='5'
l= ['10.1.1.206','192.168.1.1','10.100.8.106','10.100.8.107']
for ipaddr in l:
        a = subprocess.call([ping,arg,count,ipaddr])
        if a == 0:
                print ("%s is ok!" %ipaddr)
        else:
                print ("%s error"%ipaddr)
