# MAChanger

A python script to change the MAC Address.

### Read the entire article [here](https://medium.com/@dharmilch18/changing-mac-address-using-python-8a16fc4a3563)

MAChange.py = This file is a simpler version of the script. It asks the user for the interface_name and the new_mac_address.

mac_changer.py = This file has more features such as command line arguments, error handling and validating that the goal was truly achieved. Validating means the script actually checks the new MAC Address that's returned by the command 'ifconfig' with the MAC Address the user wanted to change to. 

## Setup

Download this repository and run it locally,

```bash
python3 MAChanger.py
```
**OR**
```bash
python3 mac_changer.py -i interface_name -m new_mac_address
or
python3 mac_changer.py --interface interface_name --mac new_mac_address
```
where interface_name is the name of the interface whose MAC Address you want to change and
new_mac_address is the new MAC Address that you want to replace in place of the old one.

## Output

#### Before Executing the Script

Note: Look at the **'ether'** field for the MAC Address
```bash
root@kali:~/Desktop/MAChanger# ifconfig

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500

        inet 10.0.2.10  netmask 255.255.255.0  broadcast 10.0.2.255

        ether 08:00:27:35:21:ff  txqueuelen 1000  (Ethernet)

        RX packets 7  bytes 1640 (1.6 KiB)

        RX errors 0  dropped 0  overruns 0  frame 0

        TX packets 28  bytes 2645 (2.5 KiB)

        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
#### Output of the Script

```bash
root@kali:~/Desktop/MAChanger# python3 mac_changer.py -i eth0 -m 0a:01:33:55:21:9a 

[+] MAC Address Before Change -> 08:00:27:35:21:ff

[+] Changing the MAC Address to 0a:01:33:55:21:9a

[+] MAC Address After Change -> 0a:01:33:55:21:9a

[+] MAC Adress was successfully changed from 08:00:27:35:21:ff to 0a:01:33:55:21:9a
```


#### After Executing the Script

Note: Look at the **'ether'** field for the MAC Address

```bash
root@kali:~/Desktop/MAChanger# ifconfig

eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500

        inet 10.0.2.10  netmask 255.255.255.0  broadcast 10.0.2.255

        ether 0a:01:33:55:21:9a  txqueuelen 1000  (Ethernet)

        RX packets 8  bytes 2230 (2.1 KiB)

        RX errors 0  dropped 0  overruns 0  frame 0

        TX packets 29  bytes 2976 (2.9 KiB)

        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
