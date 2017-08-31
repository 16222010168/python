#!/usr/bin/env python
import paramiko
import pexpect

'''
This is a script that can execute command to a batch of systems
'''

account = {'10.100.8.107':'yunwei','10.100.8.108':'yunwei','10.100.8.106':'yunwei','10.1.1.206':'root','10.1.1.211':'root','1
0.1.1.204':'root','10.1.1.210':'root','10.100.8.49':'root'}
ywpasswd = {'10.100.8.107':'1qaz2wsx','10.100.8.108':'1qaz2wsx','10.100.8.106':'1qaz2wsx'}
rootpasswd = {'10.1.1.206':'1qaz&ujm','10.1.1.211':'1qaz@WSX','10.1.1.204':'qp0512sap','10.1.1.210':'1qaz@WSX','10.100.8.49':
'root'}
ipaddr = account.keys()
command = raw_input('Command:')



for i in ipaddr:

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    if account[i] == 'yunwei':
        passwd = ywpasswd[i]
    elif account[i] == 'root':
        passwd = rootpasswd[i]

    try:

        client.connect(hostname=i, port=22, username=account[i], password=passwd)
        stdin, stdout, stderr = client.exec_command(command)  # Input command need to be execute.
        print(stdout.read().decode())
        client.close()

    except Exception,e:

        child = pexpect.spawn('telnet ' + i)
        child.expect('login: ')
        child.sendline(account[i])
        child.expect('(?i)password:')
        child.sendline(passwd)
        child.expect(['#','$'])
        child.sendline(command)
        child.expect(['#','$'])
        child.sendline('exit')
        child.close()
