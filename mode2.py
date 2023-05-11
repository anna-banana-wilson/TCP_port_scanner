from scapy.all import *

def syn(order, ports, target_ip):

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

        print('{:<10}'.format('PORT'), '{:^10}'.format('STATE'), '{:>10}'.format('SERVICE')) 

        for x in range(0, endport):
            packet = IP(dst = target_ip)/TCP(dport = x, flags = 'S')
            
            response = sr1(packet, timeout = 1, verbose = 0) # this sends and recieves one time
            # print('port: ', x)

            # if actually have a valid response from the target and and we a get a SYN-ACK (0x12 means SYN-ACK)
            if not isinstance(response, type(None)):
                if response.haslayer(TCP) and response.getlayer(TCP).flags == 0x12:
                    num_open += 1
                    
                    banner = socket.getservbyport(x, "tcp")
                    
                    print('{:<10}'.format(x), '{:^10}'.format('open'), '{:>10}'.format(banner)) 
    
                    # send the RST packet (reset packet, so we can get rid of the connection and move onto the next one):
                    sr(IP(dst=target_ip)/TCP(dport=response.sport, flags = 'R'), timeout = 0.5, verbose = 0)

    # RANDOM 
    elif(order == 'random'):

        print('{:<10}'.format('PORT'), '{:^10}'.format('STATE'), '{:>10}'.format('SERVICE')) 

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
                    # print(x)
                    banner = socket.getservbyport(x, "tcp")
                    
                    print('{:<10}'.format(x), '{:^10}'.format('open'), '{:>10}'.format(banner)) 
    
                    # send the RST packet (reset packet, so we can get rid of the connection and move onto the next one):
                    sr(IP(dst=target_ip)/TCP(dport=response.sport, flags = 'R'), timeout = 0.5, verbose = 0)
    
    # INVALID 
    else: 
        print("Invalid order argument")
        exit() # im not sure if this is the right thing, but i want to stop if they type an invalid option

    return num_open

        
     
