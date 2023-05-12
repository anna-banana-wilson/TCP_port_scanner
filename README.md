# TCP_port_scanner

## Sources:
https://www.paessler.com/it-explained/ping
https://www.oreilly.com/library/view/python-penetration-testing/9781789138962/9f389f41-4489-4628-a61f-969eea3aae8c.xhtml
https://pythontic.com/modules/socket/getservbyport
https://www.youtube.com/watch?v=OKHqhYk198M&ab_channel=CristiVlad
https://docs.python.org/3/library/argparse.html#type\
https://docs.python.org/3/library/datetime.html
https://realpython.com/python-sockets/
https://www.geeksforgeeks.org/simple-port-scanner-using-sockets-in-python/
https://gist.github.com/jossef/16d2746565989bd7b7fc02eb794db3b5
http://pymotw.com/2/socket/tcp.html
https://0xbharath.github.io/art-of-packet-crafting-with-scapy/network_recon/service_discovery/index.html
https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
https://gist.github.com/jossef/16d2746565989bd7b7fc02eb794db3b5 

## Required Files: 
- port_scanner.py
- mode1.py
- mode2.py
- mode3.py

## How to Run the Port Scanner
- To run the project, n the terminal, run the following command:
```Python3 port_scanner.py [mode] [order] [ports] [target_ip]```

- The options for `[mode]` are: 
    - `normal` which involves a full TCP connect to scan
    - `syn ` which only sends initial SYN and RST packets to scan
    - `fin` which only sends FYN packets to scan
- The options for `[order] ` are:
    - `order` scans the ports in order starting at 0
    - `random` scans the ports in a random order
- The options for `[ports]` are:
    - `all` scans all 65535 ports
    - `known` scans only the well known ports, the first 1023
- The `target_ip` option is simply the IP of the host you wish to scan

The following example runs the project on normal mode, scanning the ports in order, only the first 1023 ports, targeting the host at the ip address 111.111.11.11

```Python3 port_scanner.py normal order known 111.111.11.11```

## Individual Contributions and Challenges 
Jade:
- figured out how to implement argparse, which was different from using regular sys 
- timing how long the port scanner took 
- formatting the end aesthetics of the port scanner
- research and finding resources that helped with the implementation process 
- fin scan mode 3 and figuring out the bug that wouldn't work with getservbyport; using other method 

Anna:
- finding out how to implement mode 2 (SYN scan), from there the rest of the modes 
- loops, options (random or order, etc), ping to ensure the host is alive 

The Challenges We Overcame Together:
- We largely pair-programmed this project. Most of the code was written collaboratively, so individual contributions don't apply as much as we physically met up seven or eight times to implement this together side by side. 
- The biggest challenge we overcame was definitely the logic of the port scanner, we took a while figuring out what the output should be, especially when it came to the fin scan and retrieving banners. 
- Another big challenge we faced was that at some point, Anna's computer could not run connect to the host at all and therefore could not run it. 
- Another challenge was using Git in order to practice collaborating! Using GitHub was always finnicky for the both of us, so this project gave us a chance to practice that skill. 

