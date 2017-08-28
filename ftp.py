#!/usr/bin/env python
import pexpect

account = {'10.100.8.107':'yunwei','10.100.8.108':'yunwei','10.100.8.106':'yunwei','10.1.1.206':'root','10.1.1.211':'root','10.1.1.204':'root','10.1.1.210':'root','10.100.8.49':'root'}
ywpasswd = {'10.100.8.107':'1qaz2wsx','10.100.8.108':'1qaz2wsx','10.100.8.106':'1qaz2wsx'}
rootpasswd = {'10.1.1.206':'1qaz&ujm','10.1.1.211':'1qaz@WSX','10.1.1.204':'qp0512sap','10.1.1.210':'1qaz@WSX','10.100.8.49':
'root'}
ipaddr = account.keys()
source = raw_input('Source Path:')
destination = raw_input('destination path:')
fn = raw_input('file name:')

for i in ipaddr:
    child = pexpect.spawn('ftp ' + i)
    fout = file('ftplog.log','a')
    child.logfile = fout
    child.expect('(?i)name .*: ')
    child.sendline(account[i])

    if account[i] == 'yunwei':
        passwd = ywpasswd[i]
    elif account[i] == 'root':
        passwd = rootpasswd[i]

    child.expect('(?i)password:')
    child.sendline(passwd)
    child.expect('ftp>')
    child.sendline('cd ' + source)
    child.expect('ftp>')
    child.sendline('lcd ' + destination)
    child.expect('ftp>')
    child.sendline('bin')
    child.expect('ftp>')
    child.sendline('put ' + fn)
    child.expect('ftp>')
    child.sendline('by')
