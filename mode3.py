from scapy.all import * 
#from pythonping import ping 

def mode3(): 
    print("you chose mode 3") 

    # ip1 = IP(src="50.106.175.86", dst ="131.229.72.13")
    # sy1 = TCP(dport=22, flags="F", seq=12345)
    # packet = ip1/sy1
    packet =  IP(src="50.106.175.86", dst ="131.229.72.13")/TCP(dport=22, flags="F", seq=12345)
    p = sr1(packet, timeout=2)
    p.show()

mode3()
