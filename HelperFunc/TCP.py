import struct


class tcp:
    def __init__(self,raw_data):
        self.src_port,self.dest_port,self.sequence, self.ack , offset_flags = struct.unpack('!HHLLH',raw_data[:14])
        offset =(offset_flags >>12)*4
        self.urg = (offset_flags & 32) >> 5
        self.ack = (offset_flags & 16) >> 4
        self.psh = (offset_flags & 8) >> 3
        self.rst = (offset_flags & 4) >> 2
        self.syn = (offset_flags & 2) >> 1
        self.fin = (offset_flags & 1)
        self.data = raw_data[offset:]
