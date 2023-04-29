from scapy.all import * 
import socket

def mode3(): 
    print("you chose mode 3") 

    # ip1 = IP(src="50.106.175.86", dst ="131.229.72.13")
    # sy1 = TCP(dport=22, flags="F", seq=12345)
    # packet = ip1/sy1
    # packet =  IP(src="50.106.175.86", dst ="131.229.72.13"/TCP(dport=22, flags="F", seq=12345)
    # p = sr1(packet, timeout=5)
    # p.show()
    i= IP()
    t= TCP()
    i.dst='131.229.72.13'
    t.dport=22
    t.flags="F"
    packet=i/t
    answered,unanswered = sr(packet, timeout=2)
    #answered.summary(lfilter = lambda s,r: r.sprintf("%TCP.flags%") == "SA",prn=lambda s,r: r.sprintf("%TCP.sport% is open"))
    if isinstance(answered, type(None)):
        print('Port' + str(x) + ' is open!')
    # serviceName = socket.getservbyport(1, 'tcp') # this returns just the service name 
    # print(serviceName)
    # print("Name of the service running at port number %d : %s"%(portNumber, serviceName));
    # p = sr1(IP(dst="www.slashdot.org")/ICMP()/"XXXXXXXXXXX")
    # p.show()
mode3()
