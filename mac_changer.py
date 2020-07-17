import subprocess as sub
import argparse
import re

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument('-i', '--interface', dest = 'interface', help = 'Interface name whose MAC is to be changed')
  parser.add_argument('-m', '--mac', dest = 'new_mac', help = 'New MAC Address')
  options = parser.parse_args()
  
  #Check for errors i.e if the user does not specify the interface or new MAC
  #Quit the program if any one of the argument is missing
  #While quitting also display an error message
  
  if not options.interface:
    #Code to handle if interface is not specified
    parser.error('[-] Please specify an interface in the arguments, use --help for more info.')
    
  elif not options.new_mac:
      #Code to handle if new MAC Address is not specified
      parser.error('[-] Please specify a new MAC Address, use --help for more info.')
      
  return options

def change_mac(interface, new_mac):
  
  #Cecking if the new MAC Address has a length of 17 or not. If not print an error and quit, else change the MAC Address
  if len(new_mac) != 17:
    print('[-] Please enter a valid MAC Address')
    quit()
  
  print('\n[+] Changing the MAC Address to', new_mac)
  sub.call(['sudo', 'ifconfig', interface, 'down'])
  sub.call(['sudo', 'ifconfig', interface, 'hw', 'ether', new_mac])
  sub.call(['sudo', 'ifconfig', interface, 'up'])
  
def get_current_mac(interface):
  output = sub.check_output(['ifconfig', interface], universal_newlines = True)
  search_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", output)
  if search_mac:
    return search_mac.group(0)
  else:
    print('[-] Could not read the MAC Address')
    
    
command_args = get_args()

prev_mac = get_current_mac(command_args.interface)
print('\n[+] MAC Address before change -> {}'.format(prev_mac))

change_mac(command_args.interface, command_args.new_mac)

changed_mac = get_current_mac(command_args.interface)
print('\n[+] MAC Address after change -> {}'.format(changed_mac))

#Checking if the current MAC is same as the what the user intended to be
#If not then display an error
#Else display a message that says MAC Changed successfully
if changed_mac == command_args.new_mac:
  print('\n[+] MAC Adress was successfully changed from {} to {}'.format(prev_mac, changed_mac))
else:
  print('\n[-] Could not change the MAC Address')
