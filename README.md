# MAChanger

A python script to change the MAC Address.

MAChange.py = This file is a simpler version of the script. It asks the user for the interface_name and the new_mac_address.

mac_changer.py = This file has more features such as command line arguments, error handling and validating that the goal was truly achieved.

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
