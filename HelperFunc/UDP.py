
import struct

class udp:
    def __init__(self,raw_data):
        self.src_port ,self.dest_port, self.size =struct.unpack('!HH2xH',raw_data[:8])
        self.data =raw_data[8:]
