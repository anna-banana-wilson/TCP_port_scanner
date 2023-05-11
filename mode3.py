import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import * 
import socket


def grab_banner(ip_address, port):
    try:
        s = socket.socket()
        s.connect((ip_address, port))
        banner = s.recv(1024)
        s.close()
        return banner
    except:
        return ''

def fin(order, ports, target_ip): 

    num_open = 0

    if(ports == 'all'):
        endport = 65535
    elif(ports == 'known'):
        endport = 1023
    else:
        print("Invalid ports argument")
        exit() # im not sure if this is the right thing, but i want to stop if they type an invalid option
    

    ip1 = IP( dst = target_ip)

    # ORDER 
    if(order == 'order'):

        print('{:<10}'.format('PORT'), '{:^10}'.format('STATE'), '{:>10}'.format('SERVICE')) 

        # testing for individual ports 
        sy1 = TCP(dport=443, flags="F", seq=12345)
        packet = ip1/sy1
        response = sr1(packet, timeout = 2, verbose = 0)   
        if isinstance(response, type(None)):
            banner = str(grab_banner(target_ip, 443))
                    
            print('{:<10}'.format('443'), '{:^10}'.format('open'), '{:>10}'.format(banner)) 

        # for x in range(0, endport):
        #     sy1 = TCP(dport=x, flags="F", seq=12345)
        #     packet = ip1/sy1
        #     response = sr1(packet, timeout = 2, verbose = 0)   
        #     #answered.summary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA",prn=lambda s,r: r.sprintf("%TCP.sport% is open"))
        
        #     if isinstance(response, type(None)):
            
        #         num_open += 1
        #         # print(type(response))
        #         banner = str(grab_banner(target_ip, x))
                    
        #         print('{:<10}'.format(x), '{:^10}'.format('open'), '{:>10}'.format(banner)) 
    
        #     # serviceName = socket.getservbyport(1, 'tcp') # this returns just the service name 
        #     # print(serviceName)
        #     # print("Name of the service running at port number %d : %s"%(portNumber, serviceName));
        #     # p = sr1(IP(dst="www.slashdot.org")/ICMP()/"XXXXXXXXXXX")
        #     # p.show()

    # RANDOM 
    elif(order == 'random'):

        print('{:<10}'.format('PORT'), '{:^10}'.format('STATE'), '{:>10}'.format('SERVICE')) 

        port_list = []

        for i in range (0, endport + 1): # the plus 1 is because of how python range() works
            port_list.append(i)
            # print('item in port list: ', i) # This number is correct! 
        
        random.shuffle(port_list)

        for x in range(0, endport):
            
            sy1 = TCP(dport=x, flags="F", seq=12345)
            packet = ip1/sy1
            response = sr1(packet, timeout = 0.5, verbose = 0)   
            #answered.summary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA",prn=lambda s,r: r.sprintf("%TCP.sport% is open"))
        
            if isinstance(response, type(None)):
            
                num_open += 1
                # print(type(response))
                banner = str(grab_banner(target_ip, x))
                    
                print('{:<10}'.format(x), '{:^10}'.format('open'), '{:>10}'.format(banner)) 
    

    # INVALID 
    else: 
        print("Invalid order argument")
        exit() # im not sure if this is the right thing, but i want to stop if they type an invalid option

    return num_open

