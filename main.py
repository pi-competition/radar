# get the current wlan0 local ip address and netmask to get the broadcast address
# python 3.9

import socket
import fcntl
import struct
import os
import server
import threading
import datetime

devices = [
    {
        "ip": None,
        "mac": "e4:5f:01:ef:da:6b",
        "name": "CONTROL-1",
        "type": "CONTROL",
        "net_status": "UNKNOWN"
    },
    {
        "ip": None,
        "mac": "b8:27:eb:56:c3:07",
        "name": "test",
        "type": "CAR",
        "net_status": "UNKNOWN"
    },
    {
        "ip": None,
        "mac": "b8:27:eb:56:c3:08",
        "name": "test2",
        "type": "CAR",
        "net_status": "UNKNOWN"
    }

]

last_run = None
last_ping = None

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15].encode())
    )[20:24])

def get_netmask(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x891b,  # SIOCGIFNETMASK
        struct.pack('256s', ifname[:15].encode())
    )[20:24])

def get_broadcast_address(ifname):
    ip = get_ip_address(ifname)
    netmask = get_netmask(ifname)
    ipaddr = ip.split('.')
    netmask = netmask.split('.')
    broadcast = []
    for i in range(4):
        broadcast.append(str(int(ipaddr[i]) | int(netmask[i]) ^ 255))
    return '.'.join(broadcast)

BROADCAST = get_broadcast_address('wlan0')


def main():
    global last_run
    # send broadcast message to discover devices
    ping = os.popen(f"ping -b -c1 {BROADCAST}").read()
    print(ping)
    # use arpreq to get the mac address of the device

    for device in devices:
        mac = device['mac']
        if device["ip"]:
            os.popen(f"ping -c1 {device['ip']}")
        res = os.popen(f'ip neigh | grep {mac}').read()
        if res:
            device['ip'] = res.split()[0]
            device['net_status'] = res.split()[5]
    last_run = datetime.datetime.now().isoformat()
    print(last_run)


    threading.Timer(60, main).start()
main()



def ping():
    global last_ping
    for device in devices:
        if device["ip"]:
            os.popen(f"ping -c1 {device['ip']}")
    last_ping = datetime.datetime.now().isoformat()
    threading.Timer(20, ping).start()
ping()
