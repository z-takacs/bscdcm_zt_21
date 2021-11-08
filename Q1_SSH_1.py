"""

#
# File      :Q1_SSH_1.py
# Created   : 08/11/2021 18:21
# Author    : Zoltan Takacs
# Version   : v1.0.0
# Licensing : (C) 2021 Zoltan Takacs, LYIT
#             Available under GNU Public License (GPL)
# Desription:   Using Python Script to SSH into VM and checking which user logged in.
#
"""
if __name__ == '__main__':

    '''
  Main method of application:

  Parameters: None

  Returns: Logged in user on VM.
  '''

import paramiko

host = "192.168.136.128"
port = 22
username = "l00169723"
password = "Zozik@11!"
command = "whoami"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)
stdin, stdout, stderr = ssh.exec_command(command)
lines = stdout.readlines()

print(lines)
