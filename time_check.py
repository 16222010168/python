#!/usr/bin/env python

import paramiko
import datetime

def GetPasswd(path):      #This foundation is to generate a dictionary which contain host ip and password.


    f = open(path,'r')
    tmp = []

    for i in f.readlines():
        tmp.append(i.strip('\n').split(':'))

    host = []
    passwd = []
    for i in tmp:

        host.append(i[0])
        passwd.append(i[1])

    host_dict = dict(zip(host,passwd))
    return host_dict

def time_check(host_t):
        t1 = datetime.datetime.strptime(host_t, '%Y-%m-%d %H:%M:%S')
        tmp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        t2 = datetime.datetime.strptime(tmp, '%Y-%m-%d %H:%M:%S')
        if t1 > t2:
                delta =  t1 - t2
        else:
                delta = t2 -t1
        return delta.seconds

hostp = GetPasswd("/tmp/host.txt")
ipaddr = hostp.keys()
result_host = []
time_diff = []
for i in xrange(len(ipaddr)):
    hn = ipaddr[i]
    pw = hostp[ipaddr[i]]

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname = hn, port = 22, username = "yunwei", password = pw)
    stdin, stdout, stderr = client.exec_command('date "+%Y-%m-%d %H:%M:%S" ')
    host_time = stdout.read().strip()
    diff = time_check(host_time)
    if diff > 300:
        result_host.append(hn)
        time_diff.append(diff)
    else:
        pass

diff_dict = dict(zip(result_host, time_diff))

print diff_dict

ftmp = []
for i in diff_dict.keys():
    ftmp.append(i + '\n')
    ftmp.append(str(diff_dict[i]) + '\n')

f = open('timech.log', 'w')
f.writelines(ftmp)
f.close()


