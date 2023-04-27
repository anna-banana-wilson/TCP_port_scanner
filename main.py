#!/usr/bin/python3
import sys
from scapy.all import *
from pythonping import ping
import os 


def HostUp(hostname, waittime=1000):
    '''Function returns True if host IP returns a ping, else False'''
    assert isinstance(hostname, str), \
        "IP/hostname must be provided as a string."
    if os.system("ping -c 1 -W " + str(waittime) + " " +
                 hostname + " > /dev/null 2>&1") is 0:
        HOST_UP = True
    else:
        HOST_UP = False
    return HOST_UP
    

def main():
    is_alive = HostUp("131.229.72.13", waittime=1000) 
    

if __name__ == "__main__":

    main()

# i hope this works i really do because wtf 
# okay trying this again 