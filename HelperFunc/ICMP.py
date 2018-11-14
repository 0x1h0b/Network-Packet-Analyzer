import struct

# Helper function for dealing with icmp data

class icmp:
    def __init__(self,raw_data):
        self.type,self.code,self.checksum = struct.unpack('!BBH',raw_data[:4])
        self.data = raw_data[4:]
