import struct
# helper class for deaing with ipv4 data
class ipv4:

    def __init__(self, raw_data):
        version_header_length = raw_data[0]
        self.version = version_header_length >> 4
        self.header_length = (version_header_length & 15) * 4
        self.ttl, self.proto, src, target = struct.unpack('!8xBB2x4s4s', raw_data[:20])
        self.src = self.final(src)
        self.target = self.final(target)
        self.data = raw_data[self.header_length:]

    # Returns properly formatted IPv4 address
    def final(self, addr):
        return '.'.join(map(str, addr))
