from scapy.all import * 
import socket

def mode3(ports, mode, target_ip): 
    print("you chose mode 3") 

    # ip1 = IP(src="50.106.175.86", dst ="131.229.72.13")
    # sy1 = TCP(dport=22, flags="F", seq=12345)
    # packet = ip1/sy1
    # packet =  IP(src="50.106.175.86", dst ="131.229.72.13"/TCP(dport=22, flags="F", seq=12345)
    # p = sr1(packet, timeout=5)
    # p.show()
    # i= IP()
    # t= TCP()
    # i.dst='131.229.72.13'
    # t.dport=22
    # t.flags="F"
    # packet=i/t
    # print(packet)
    # answered,unanswered = sr(packet)
    # print(type(answered))

    if(ports == 'all'):
        endport = 65535
    elif(ports == 'known'):
        endport = 1023
    elif(ports == 'testoption'):
        endport = 23
    else:
        print("Invalid ports argument")
        exit() # im not sure if this is the right thing, but i want to stop if they type an invalid option
    
    startport = 0
    endport = 25

    ip1 = IP( dst ="131.229.72.13")

    # ORDER 
    if(order == 'order'):
        for x in range(startport, endport):
            sy1 = TCP(dport=x, flags="F", seq=12345)
            packet = ip1/sy1
            response = sr1(packet, timeout = 2)   
            #answered.summary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA",prn=lambda s,r: r.sprintf("%TCP.sport% is open"))
            if isinstance(response, type(None)):
                # print(type(response))
                serviceName = socket.getservbyport(x, 'tcp') # this returns just the service name 
                print(serviceName)

            # serviceName = socket.getservbyport(1, 'tcp') # this returns just the service name 
            # print(serviceName)
            # print("Name of the service running at port number %d : %s"%(portNumber, serviceName));
            # p = sr1(IP(dst="www.slashdot.org")/ICMP()/"XXXXXXXXXXX")
            # p.show()

    # RANDOM 
    elif(order == 'random'):
        port_list = []

        for i in range (0, endport + 1): # the plus 1 is because of how python range() works
            port_list.append(i)
            # print('item in port list: ', i) # This number is correct! 
        
        random.shuffle(port_list)

        for x in range(startport, endport):
            sy1 = TCP(dport=x, flags="F", seq=12345)
            packet = ip1/sy1
            response = sr1(packet, timeout = 2)   
            #answered.summary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA",prn=lambda s,r: r.sprintf("%TCP.sport% is open"))
            if isinstance(response, type(None)):
                # print(type(response))
                serviceName = socket.getservbyport(x, 'tcp') # this returns just the service name 
                print(serviceName)

    # INVALID 
    else: 
        print("Invalid order argument")
        exit() # im not sure if this is the right thing, but i want to stop if they type an invalid option

mode3()
