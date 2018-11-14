import socket
import sys


from HelperFunc.Ethernet import EthernetFrame
from HelperFunc.IPv4 import ipv4
from HelperFunc.TCP import tcp
from HelperFunc.UDP import udp
from HelperFunc.ICMP import icmp



def main():
    try:
        con=socket.socket(socket.AF_PACKET , socket.SOCK_RAW, socket.ntohs(3))
        print('Socket Initialized !!................................')
    except socket.error as err_msg:
        print ('Socket Initialization failed !!...'+ str(err_msg))
        print('Run the program with superuser permission.')
        sys.exit()

    while True:
        raw_data, address =con.recvfrom(65536)
        s= EthernetFrame(raw_data)        # s is an ethernet frame instance
        print('\n ####################### Ethernet Frame ############################# \n')
        print('Destination Mac:{} , Source Mac:{} , Protocol: {} \n'.format(s.dest,s.src,s.proto))

        if s.proto==8:   # 8 is for IPv4 packets ..
            d=ipv4(s.data)                 # d is a ipv4 instance
            print('IPv4 Packet:')
            print('\t'+'- Version: {} ,Header Length : {} , TTL: {}'.format(d.version,d.header_length,d.ttl))
            print('\t'+'- Protocol:{}, Source IP: {} , Target IP:{}'.format(d.proto,d.src,d.target))

              # 6 tells us that its a tcp segment
            if d.proto == 6:
                t=tcp(d.data)            # t is a tcp instance
                print('\t'+'- TCP segment:')
                print('\t\t'+'- Destination Port: {} , Source Port : {}'.format(t.dest_port,t.src_port))
                print('\t\t'+'- Sequence:{} , Acknowledge:{}'.format(t.sequence,t.ack))
                print('\t\t'+'- Flags :')
                print('\t\t  '+' URG:{}, ACK:{}, PSH:{}'.format(t.urg,t.ack,t.psh))
                print('\t\t  '+' RST:{}, SYN:{}, FIN:{}'.format(t.rst,t.syn,t.fin))
             # 17 tells that its an udp segment
            elif d.proto ==17:
                u=udp(d.data)
                print('\t'+'- UDP Segment:')
                print('\t\t'+'- Source Port :{} , Destination Port:{}, Size:{}'.format(u.src_port,u.dest_port,u.size))

             # 1 tells us that its an icmp data
            elif d.proto==1:
                i=icmp(d.data)
                print('\t'+'- ICMP Segment:')
                print('\t\t'+'- ICMP type:{} , icmp code:{} ,checksum:{}'.format(i.type,i.code,i.checksum))

            else:
                print('Unknown segment Type:')
        else:
            print('Following is not an IPv4 Packet:')




if __name__=='__main__':
    main()
