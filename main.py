#!/usr/bin/python3
import sys
from scapy.all import *
from pythonping import ping
import os 
import argparse 
import datetime
import mode1
import mode2
import mode3
import time 
# import mode2
# import mode3 


def HostUp(hostname, waittime=1000):
    # Function returns True if host IP returns a ping, else False
    assert isinstance(hostname, str), \
        "IP/hostname must be provided as a string."
    if os.system("ping -c 1 -W " + str(waittime) + " " +
                 hostname + " > /dev/null 2>&1") == 0:
        HOST_UP = True
    else:
        HOST_UP = False
    return HOST_UP
    

def main():
    seconds = time.time() 
    # positional arguments and options 
    parser = argparse.ArgumentParser(description="Port Scanner") 
    parser.add_argument("mode", choices=['normal', 'syn', 'fin']) 
    parser.add_argument("order", choices=['order', 'random'])
    parser.add_argument("ports", choices=['all', 'known', 'testoption'])
    parser.add_argument("target_ip", help="list the target host's IP address")
    mode = parser.mode
    order = parser.order 
    ports = parser.ports 
    target_ip = parser.target_ip 

    args = parser.parse_args() 
    
    #I'M ASSUMING we also need to use action= somewhere to link to the different files. 
    
    is_alive = HostUp(target_ip, waittime=1000) 

    now = datetime.datetime.now()
    print("Starting port scan at            ", now)
    print("Interesting ports on ", target_ip, ":")
    print("Scanned in ", seconds, " seconds.")

    

if __name__ == "__main__":
    
    main()

# i hope this works i really do because wtf 
# okay trying this again 