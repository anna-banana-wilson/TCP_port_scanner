from scapy.all import *
import socket
import time
import sys 
import random

def normal(order, ports, target_ip):
    print("MODE 1 RUNNING")

    num_open = 0

    if(ports == 'all'):
        endport = 65535
    elif(ports == 'known'):
        endport = 1023
    else:
        print("Invalid ports argument")
        exit() # im not sure if this is the right thing, but i want to stop if they type an invalid option
    
    # ORDER 
    if(order == 'order'):
        for x in range(0, endport):
            packet = IP(dst = target_ip)/TCP(dport = x, flags = 'S')
            
            response = sr1(packet, timeout = 1, verbose = 0) # this sends and recieves one time
            # print('port: ', x)

            # if actually have a valid response from the target and and we a get a SYN-ACK (0x12 means SYN-ACK)
            if not isinstance(response, type(None)):
                if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                    num_open += 1
                    # grab the sequence number of the server and increment by 1
                    my_ack = response.seq+1 
                    # create ack packet 
                    ack_packet = IP(dst = target_ip)/TCP(dport=response.sport, flags = 'A', seq=101, ack=my_ack)
                    # send the ACK packet to complete the 3 way handshake: 
                    sr(ack_packet, timeout = 1, verbose = 0)
                    # grab the banner 
                    print(socket.getservbyport(x, "tcp"))
    
    # RANDOM 
    elif(order == 'random'):
        port_list = []

        for i in range (0, endport + 1): # the plus 1 is because of how python range() works
            port_list.append(i)
            # print('item in port list: ', i) # This number is correct! 
        
        random.shuffle(port_list)

        for x in port_list:
            packet = IP(dst = target_ip)/TCP(dport = x, flags = 'S')
            response = sr1(packet, timeout = 1, verbose = 0) # this sends and recieves one time
            
            # if actually have a valid response from the target and and we a get a SYN-ACK (0x12 means SYN-ACK)
            if not isinstance(response, type(None)):
                if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                    num_open += 1
                    # grab the sequence number of the server and increment by 1
                    my_ack = response.seq+1 
                    # create ack packet 
                    ack_packet = IP(dst = target_ip)/TCP(dport=response.sport, flags = 'A', seq=101, ack=my_ack)
                    # send the ACK packet to complete the 3 way handshake: 
                    sr(ack_packet, timeout = 1, verbose = 0)
                    # grab the banner 
                    print(socket.getservbyport(x, "tcp"))
    
    # INVALID 
    else: 
        print("Invalid order argument")
        exit() # im not sure if this is the right thing, but i want to stop if they type an invalid option

    return num_open
    