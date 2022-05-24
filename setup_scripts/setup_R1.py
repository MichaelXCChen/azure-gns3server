from telnetlib import Telnet
import time

HOST = '172.16.253.1'
PORT = 5000

tn = Telnet(HOST, PORT)

tn.write(b'\r\n')
tn.read_until(b'Router#')
time.sleep(0.5)
tn.write(b'conf t\r\n')
tn.read_until(b'Router(config)#')
time.sleep(0.5)
tn.write(b'int g0/0\r\n')
tn.read_until(b'Router(config-if)#')
time.sleep(0.5)
tn.write(b'ip address 10.0.0.2 255.255.255.0\r\n')
tn.read_until(b'Router(config-if)#')
time.sleep(0.5)
tn.write(b'no shut\r\n')
tn.read_until(b'Router(config-if)#')
tn.write(b'exit\r\n')
tn.read_until(b'Router(config)#')
time.sleep(0.5)
tn.write(b'ip route 0.0.0.0 0.0.0.0 10.0.0.1 250\r\n')
tn.read_until(b'Router(config)#')
time.sleep(0.5)
tn.write(b'exit\r\n')
tn.read_until(b'Router#')
time.sleep(0.5)
tn.write(b'exit\r\n')
tn.close()
