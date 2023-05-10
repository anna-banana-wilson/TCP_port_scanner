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


def HostUp(hostname, waittime=1000): # this function is from a github user to check ping status 
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
    # positional arguments and options 
    parser = argparse.ArgumentParser(description="Port Scanner") # initialize ArgumentParser 
    parser.add_argument("mode", choices=['normal', 'syn', 'fin']) 
    parser.add_argument("order", choices=['order', 'random'])
    parser.add_argument("ports", choices=['all', 'known'])
    parser.add_argument("target_ip", help="list the target host's IP address")
    args = parser.parse_args() # grab arguments from command line 

    # storing various arguments into variables 
    mode = args.mode
    order = args.order 
    ports = args.ports 
    target_ip = args.target_ip 

    # using ping to check if target host is up and running 
    is_alive = HostUp(target_ip, waittime=1000) 
    
    if is_alive == True: # if so, then run the port scanner 

        start_time = time.time() 
        now = datetime.datetime.now()
        print("Starting port scan at            ", now)
        print("Interesting ports on ", target_ip, ":")
        
        if(mode == 'normal'):
            num_open = mode1.normal(order = order, ports = ports, target_ip = target_ip)
        if(mode == 'syn'):
            num_open = mode2.syn(order = order, ports = ports, target_ip = target_ip)
        if(mode == 'fin'): 
            num_open = mode3.fin(order = order, ports = ports, target_ip = target_ip)
        
        print("IP address (1 host up) scanned in %s seconds" % (time.time() - start_time))

        if(ports == 'all'):
            num_closed = 65535 - num_open
        elif(ports == 'known'):
            num_closed = 1023 - num_open
            
        print("Not shown: %s closed ports" % (num_closed))

    else:
        print("The target host is down.")
        exit() 
    

    

if __name__ == "__main__":
    
    main()

