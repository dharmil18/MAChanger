import subprocess as sub
import optparse
import re

def get_args():
    parser = optparse.OptionParser()
    parser.add_option('-i', '--interface', dest='interface', help='Interface name whose MAC is to be changed')
    parser.add_option('-m', '--mac', dest='new_mac', help='New MAC Address')
    options, arguments = parser.parse_args()

    #Check for errors i.e if the user does not specify the interface or new MAC
    #Quit the program if any one of the argument is missing
    #While quitting also display an error message
    if not options.interface:
        #Handling the code if interface is not specified
        parser.error("[-] Please specify an interface in the arguments, use --help for more info.")
    elif not options.new_mac:
        #Handling the code if new MAC Address is not specified
        parser.error("[-] Please specify a new MAC Address, use --help for more info.")
    return options

def get_current_mac(interface):
    ifconfig_op = sub.check_output(["ifconfig", options.interface], universal_newlines=True)
    mac_search = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_op)
    if mac_search:
        return mac_search.group(0)
    else:
        print("[-] Could not read the MAC Address")

def change_mac(interface, new_mac):

    if len(new_mac) != 17:
        print('[+] Warning: Please Enter a Valid MAC Address')
        quit()

    print("\n[+] Changing the MAC Address to", new_mac)
    sub.call(["ifconfig", interface, "down"])
    sub.call(["ifconfig", interface, "hw", "ether", new_mac])
    sub.call(["ifconfig", interface, "up"])


options = get_args()

prev_mac = get_current_mac(options.interface)
print("\n[+] MAC Address Before Change -> {}".format(prev_mac))

change_mac(options.interface, options.new_mac)

current_mac = get_current_mac(options.interface)
print("\n[+] MAC Address After Change -> {}".format(current_mac))

#Validating whether the MAC Address was changed to what the user had requested or not
if current_mac == options.new_mac:
    print("\n[+] MAC Adress was successfully changed from {} to {}".format(prev_mac, current_mac))
else:
    print("\n[-] Could not change the MAC Address")


