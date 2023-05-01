This is a repository by TEAM PANIC for the PA Raspberry Pi Competition 2023 - Accelerating the transition to green energy

All code in this repository is licensed under the MIT license. See LICENSE for more information.

> © 2023 TEAM PANIC - All Rights Reserved

# 📡 Radar

Radar is a tool for discovering devices on a local network. It scans the network for devices that respond to ICMP echo requests (ping). With this data, it attempts to identify devices by their MAC address.

**Devices must have `net.ipv4.icmp_echo_ignore_broadcasts` set to 0 in order to respond to ICMP echo requests.**

## 🚀 Usage
HTTP GET request to 127.0.0.1:5000/devices

```
curl -X GET http://127.0.0.1:5000/devices
```

### Response:
Returns and array of devices
```
[
    {
        "ip?": "0.0.0.0",
        "mac": "00:00:00:00:00:00",
        "name": "CAR-1",
        "type": "CAR" | "CONTROL",
        "net_status": "UNKNOWN" | "PERMANENT" | "NOARP" | "STALE" | "REACHABLE" | "NONE" | "INCOMPLETE" | "DELAY" | "PROBE" | "FAILED"
    }
]
```





