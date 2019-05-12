import paramiko
import os
import sys
import time
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# from conf import ssh_conf as conf_file
import socket
import json
import requests
import unicodedata


#killCommand = 'taskkill /IM "UiPath.Service.Host.exe" /F'
killCommand = 'net stop UiRobotSvc'
startCommand = 'net start UiRobotSvc'

# DATA WILL BE FETCHED FROM SECURED DB from hashed content. Credentials will not be exposed
mc1_host = "<host>"
mc1_userName = "<user name>"
mc1_pwd="<password>"
mc2_host = "<host>"
mc2_userName = "<user name>"
mc2_pwd="<password>"

args = sys.argv
cmd=None
host=None
userName=None
pwd=None

if args[1]=="start":
    cmd=startCommand
elif args[1]=="stop":
    cmd=killCommand

if args[2]=='1':
    host=mc1_host
    userName=mc1_userName
    pwd=mc1_pwd
elif args[2]=='2':
    host=mc2_host
    userName=mc2_userName
    pwd=mc2_pwd

def ssh(ip, port, username, password, cmd):
    try:
        print('Connecting to server .....')
        ssh = paramiko.SSHClient()  # ??ssh?? 
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=int(port),
                    username=username, password=password, )
        print('Machine '+ args[2] + ' '+args[1]+' success')
        stdin, stdout, stderr = ssh.exec_command(cmd, timeout=10)
        result = stdout.read()
        result1 = result.decode()
        error = stderr.read().decode('utf-8')

        if not error:
            ret = {"ip": ip, "data": result1}
            ssh.close()
            return ret
    except Exception as e:
        print ('Error in connecting to server')
        error = "???????,{}".format(e)
        ret = {"ip": ip, "data": error}
        return ret


ssh(host, 22, userName, pwd, cmd)






