import subprocess as sub

interface = input('Enter Interface Name: ')
new_MAC = input('Enter New Mac Address: ')

if len(new_MAC) != 17:
    print('[+] Warning: Please Enter a Valid MAC Address')
    quit()


#Calling OS commands using call function in this way, then the program is vulnerable to OS Command Injection
# OS Command Injection is where an attacker can supply addtional OS commands in the user input and this can leak sensitive info or may even
# damage the system by deleting important library files or an entire file system and thus it results in Denial of Service (DoS)

# print("[+] Changing the MAC Address to", new_MAC)
# sub.call("ifconfig " + interface + " down", shell = True)
# sub.call("ifconfig " + interface + " hw ether " + new_MAC, shell = True)
# sub.call("ifconfig " + interface + " up", shell = True)
# sub.call("ifconfig", shell = True)
# print("[+] Observe the 'ether' field and its corresponding value in the captured output below")
# print("\n\nMAC Address Changed Successfully!")


#Instead of using the above solution we'll use the following method to eliminate the possibility of OS Commands Injection where the entire command 
#is provided in a list (python list) of elements where the Python understands that the first element in the list will always be the 
#command and the rest of the elements are considered as parameters/flags of the command

print("\n[+] Changing the MAC Address to", new_MAC)
sub.call(["ifconfig", interface, "down"])
sub.call(["ifconfig", interface, "hw", "ether", new_MAC])
sub.call(["ifconfig", interface, "up"])
print("\n[+] Observe the 'ether' field and its corresponding value in the captured output below")
print("\n[+] Captured Output\n")
sub.call(["ifconfig"])
print("\n[+] MAC Address Changed Successfully!")

