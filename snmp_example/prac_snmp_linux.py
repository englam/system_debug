import os

a = os.system('snmpwalk -v 2c 192.168.1.1 -c public')
print (a)