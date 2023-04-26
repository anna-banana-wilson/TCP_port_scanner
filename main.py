#!/usr/bin/python3
import sys
from scapy.all import *
from pythonping import ping

def main():
    ping_return = ping('131.229.72.13', verbose=True, count = 1)
    for i in ping_return:
        print(i)
    


if __name__ == "__main__":


    main()

# i hope this works i really do because wtf 
# okay trying this again 