from scapy.all import *
import socket
import time
import sys 

def mode1():
    print("you chose mode 1")

    target = '131.229.72.13'
    startport = 0
    endport = 24

    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # # here we asking for the target website
    # # or host
    # target = sys.argv[]     # edit to the argument it is 
    
    # # next line gives us the ip address
    # # of the target
    # target_ip = sys.argv[]  # edit to the argument it is 
    
    # try:
    #     s.connect((target_ip, port))
    #     return True
    # except:
    #     return False
    
    
    # start = time.time()
    
    # # here we are scanning port 0 to 4
    # for port in range(5):
    #     if port_scan(port):
    #         print(f'port {port} is open')
    #     else:
    #         print(f'port {port} is closed')
    
    # end = time.time()
    # print(f'Time taken {end-start:.2f} seconds')

    for x in range(startport, endport):
        packet = IP(dst = target)/TCP(dport = x, flags = 'S')
        response = sr1(packet, timeout = 1, verbose = 0) # this sends and recieves one time

        # if actually have a valid response from the target and and we a get a SYN-ACK (0x12 means SYN-ACK)
        if not isinstance(response, type(None)):
            if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                print(x)
                socket.getservbyport(x, "tcp")
                # send the RST packet (reset packet, so we can get rid of the connection and move onto the next one):
                sr(IP(dst=target)/TCP(dport=response.sport, flags = 'R'), timeout = 0.5, verbose = 0)

mode1()
    