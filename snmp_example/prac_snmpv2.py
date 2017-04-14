from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(
    getCmd(SnmpEngine(),
           CommunityData('public'),
           UdpTransportTarget(('192.168.1.1', 161)),
           ContextData(),
           #ObjectType(ObjectIdentity('1')))
           #ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')))
          #ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5')))
           ObjectType(ObjectIdentity('1.3.6.1.2.1.2.2.1.5')))
)

#print (varBinds)

if errorIndication:
    print(errorIndication)
elif errorStatus:
    print('%s at %s' % (errorStatus.prettyPrint(),
                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
else:
    for varBind in varBinds:
        print(' = '.join([x.prettyPrint() for x in varBind]))