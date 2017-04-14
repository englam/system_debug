'''
SNMPv3: auth MD5, no privacy

'''



from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           UsmUserData(userName='test1234', authKey='test1234'),
           UdpTransportTarget(('192.168.1.253', 161)),
           ContextData(),
           ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets', 1)))
)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))