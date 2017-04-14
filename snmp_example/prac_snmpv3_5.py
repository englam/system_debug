'''
SNMPwalk

'''



#ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')))

from pysnmp.hlapi import *

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in nextCmd(SnmpEngine(),
                          CommunityData('public'),
                          #UsmUserData('test'),
                          UdpTransportTarget(('192.168.1.1', 161)),
                          ContextData(),
                          #ObjectType(ObjectIdentity('IF-MIB'))):
                          ObjectType(ObjectIdentity('SNMPv2-MIB', 'system',0))):

    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))