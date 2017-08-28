#!/usr/bin/env python
"""
This is a ping test script, it helps to check the connetion of the multiple remote system!
"""

import subprocess
ping = 'ping'
arg = '-c'
count ='5'
l= ['10.1.1.206','192.168.1.1','10.100.8.106','10.100.8.107']   #Input ip address of the system you want to check to the list.
for ipaddr in l:
        a = subprocess.call([ping,arg,count,ipaddr])
        if a == 0:
                print ("%s is ok!" %ipaddr)
        else:
                print ("%s error"%ipaddr)
