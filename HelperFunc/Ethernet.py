import struct
import socket

# Helper class for extracting information about Ethernet frame

class EthernetFrame:
    def __init__(self,raw_data):
        dest,src,proto= struct.unpack('!6s6sH',raw_data[:14])
        self.dest = self.get_mac_addr(dest)
        self.src = self.get_mac_addr(src)
        self.proto = socket.htons(proto)
        self.data = raw_data[14:]

    def get_mac_addr(self,byte_add):
        b_str=map('{:02x}'.format, byte_add)
        return ':'.join(b_str).upper()
