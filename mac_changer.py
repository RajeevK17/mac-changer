from colorama import Fore
import subprocess
import random
import sys

def mac_changer():
    choice_input = int(input("1. For random mac address\n2. For mac address of your choice\n\nEnter value: "))
    interface = input("\nEnter your interface: ")

    if choice_input == 1:
        mac_digits = [random.choice("0123456789abcdef") for _ in range(12)]
        random_mac_address = ":".join(["".join(mac_digits[i:i+2]) for i in range(0, 12, 2)])

        # Capturing the standard error if interface name is invalid
        result1 = subprocess.run(["sudo", "ifconfig", interface, "down"], stderr=subprocess.PIPE, text=True)

        if "No such device" in result1.stderr:
            print(f'{Fore.RED}\n[-]Please check your interface name and try again!')
            sys.exit()
            
        else:
            # Capturing the standard error if system cannot assign randomized mac address
            result2 = subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", random_mac_address], stderr=subprocess.PIPE, text=True)
            
            if "Cannot assign requested address" in result2.stderr:
                print(f'{Fore.RED}[-]Please run the program again!')
                subprocess.run(["sudo", "ifconfig", interface, "up"])
                sys.exit()
        
            subprocess.run(["sudo", "ifconfig", interface, "up"])
            print(f'{Fore.GREEN}\n[+]Your new mac address for interface {interface} is {random_mac_address}')

    elif choice_input == 2:
        # Capturing the standard error if interface name is invalid
        result1 = subprocess.run(["sudo", "ifconfig", interface, "down"], stderr=subprocess.PIPE, text=True)

        if "No such device" in result1.stderr:
            print(f'{Fore.RED}\n[-]Please check your interface name and try again!')
            sys.exit()


        else:
            manual_mac_address = input("\nEnter your manual mac address(seperated by colons): ")

            # Capturing the standard error if system cannot assign manual mac address
            result2 = subprocess.run(["sudo", "ifconfig", interface, "hw", "ether", manual_mac_address], stderr=subprocess.PIPE, text=True)
            
            if "Cannot assign requested address" in result2.stderr:
                print(f'{Fore.RED}\n[-]Cannot assign requested mac address. Please run the program again!')
                subprocess.run(["sudo", "ifconfig", interface, "up"])
                sys.exit()

            subprocess.run(["sudo", "ifconfig", interface, "up"])
            print(f'\n{Fore.GREEN}[+]Your new mac address for interface {interface} is {manual_mac_address}')

if __name__ == '__main__':
    mac_changer()