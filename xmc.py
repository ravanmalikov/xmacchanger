
####################################################################################
# xmc - this script will change the mac address which you want to change           #
# Requirements: macchanger and ethtool needs to be installed                                  #
# Written by: Ravan Malikov                                                        #
# Github: https://github.com/ravanmalikov/XMacChanger/                             #
####################################################################################


import subprocess
import optparse
import re
from generate_mac import generate_mac

#Created by ravanmalikov
def get_user_input():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--interface",dest="interface",help="interface to change!!")
    parse_object.add_option("-m","--mac",dest="mac_address",help="new mac address")
    parse_object.add_option("-p","--permanent ",dest="reset",action='store_true',help="change your mac address to permanent")
    parse_object.add_option("-r","--random ",dest="random",action='store_true',help="changing you mac address to random")

    return parse_object.parse_args()

#Created by ravanmalikov
def change_mac_address(interface,mac_address):
    subprocess.call(["ifconfig",interface,"down"]);
    subprocess.call(["ifconfig",interface,"hw","ether",mac_address]);
    subprocess.call(["ifconfig",interface,"up"])
#Created by ravanmalikov
def mac_control(interface,mac_address):
    ifconfig=subprocess.check_output(["ifconfig",interface])
    new_mac = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w",str(ifconfig))
    if new_mac.group(0) == mac_address:
        return True
    else:
        return False
def get_old_mac(interface):
    operation = subprocess.check_output(["ethtool", "-P", interface])
    old_mac_group = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(operation))
    old_mac = old_mac_group.group(0)
    return old_mac

subprocess.call(["figlet","-w 120 -c","X M A CC H A N G E R v 1"])

(user_input,arguments)=get_user_input()
if user_input.random and user_input.reset or user_input.random and user_input.mac_address or user_input.reset and user_input.mac_address:
    print("You can't select 2 mac changing options in the same  time!")
elif user_input.reset:
    old_mac=get_old_mac(user_input.interface)
    change_mac_address(user_input.interface,old_mac)
    if mac_control(user_input.interface,old_mac)==True:
        print(f"YOUR MAC HAS BEEN RESET!\nYour permanent mac is {old_mac}")
    else:
        print("ERROR:Can't change mac adress to permanent!!")

elif  user_input.random:
    random_mac=generate_mac.total_random()
    change_mac_address(user_input.interface,random_mac)
    if mac_control(user_input.interface,random_mac.lower())==True:
        print(f"Your mac adress changed to {random_mac} ")
    else:
        print("ERROR:Can't change mac address to random")
else:
    change_mac_address(user_input.interface, user_input.mac_address)
    if mac_control(user_input.interface,user_input.mac_address)==True:
        print(f"Your MAC ADDRESS CHANGED TO {user_input.mac_address}")
    else:
        print("ERROR:Can't change mac !!")