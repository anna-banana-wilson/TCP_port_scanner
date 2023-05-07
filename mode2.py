from scapy.all import *

def mode2(order, ports, target_ip):
    
    if(ports == 'all'):
        endport = 65535
    elif(ports == 'known'):
        endport = 1023
    elif(ports == 'testoption'):
        endport = 23
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
                    print(x)
                    print(socket.getservbyport(x, "tcp"))
                    # send the RST packet (reset packet, so we can get rid of the connection and move onto the next one):
                    sr(IP(dst=target_ip)/TCP(dport=response.sport, flags = 'R'), timeout = 0.5, verbose = 0)

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
                    # print(x)
                    print(socket.getservbyport(x, "tcp"))
                    # send the RST packet (reset packet, so we can get rid of the connection and move onto the next one):
                    sr(IP(dst=target_ip)/TCP(dport=response.sport, flags = 'R'), timeout = 0.5, verbose = 0)
    
    # INVALID 
    else: 
        print("Invalid order argument")
        exit() # im not sure if this is the right thing, but i want to stop if they type an invalid option

        
     
