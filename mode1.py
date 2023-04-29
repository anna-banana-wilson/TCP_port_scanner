from scapy.all import *

def mode1():
    print("you chose mode 1")

    target = '131.229.72.13'
    startport = 0
    endport = 1023

    for x in range(startport, endport):
        packet = IP(dst = target)/TCP(dport = x, flags = 'S')
        response = sr1(packet, timeout = 2, verbose = 0) # this sends and recieves one time

        # if actually have a valid response from the target and and we a get a SYN-ACK (0x12 means SYN-ACK)
        if not isinstance(response, type(None)):
            if response.haslayer(TCP) and response.getlayer(TCP).flags ==0x12:
                print('Port' + str(x) + ' is open!')
                # send the RST packet (reset packet, so we can get rid of the connection and move onto the next one):
                sr(IP(dst=target)/TCP(dport=response.sport, flags = 'R'), timeout = 0.5, verbose = 0)

    


mode1()
    