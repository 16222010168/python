#!/usr/bin/env python
import pexpect

def GetPasswd(path):

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

account = GetPasswd('ipaddr.txt')
source = raw_input('Source Path:')
destination = raw_input('Destination Path:')
file_name = raw_input('File Name:')

for host_ip in account.keys():

    child = pexpect.spawn('ftp ' + host_ip)
    fout = file('ftplog.log','a')
    child.logfile = fout
    child.expect('(?i)name .*: ')
    child.sendline('yunwei')
    child.expect('(?i)password:')
    child.sendline(account[host_ip])

    print ("Host: %s login successful"%host_ip)

    child.expect('ftp>')
    child.sendline('cd ' + destination)
    child.expect('ftp>')
    child.sendline('lcd ' + source)
    child.expect('ftp>')
    child.sendline('bin')
    child.expect('ftp>')
    child.sendline('put ' + file_name)
    child.expect('ftp>')
    child.sendline('by')
