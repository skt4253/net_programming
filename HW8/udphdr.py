import struct
import binascii

class Udphdr:
    # udp = Udphdr(5555, 80, 1000, 0xFFFF)
    def __init__(self, srcport, dstport, tot_len, checksum):
        self.srcport = srcport
        self.dstport = dstport
        self.tot_len = tot_len
        self.checksum = checksum
        
    def pack_Udphdr(self):
        packed = b''
        packed += struct.pack("!H", self.srcport)
        packed += struct.pack("!H", self.dstport)
        packed += struct.pack("!H", self.tot_len)
        packed += struct.pack("!H", self.checksum)
        return packed
    
def unpack_Udphdr(buffer):
    unpacked = struct.unpack("!HHHH", buffer[:8])
    return unpacked

def getSrcPort(unpacked_udpheader):
    return unpacked_udpheader[0]

def getDstPort(unpacked_udpheader):
    return unpacked_udpheader[1]

def getLength(unpacked_udpheader):
    return unpacked_udpheader[2]

def getChecksum(unpacked_udpheader):
    return unpacked_udpheader[3]

udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print("({}, {}, {}, {})".format(getSrcPort(unpacked_udphdr), getDstPort(unpacked_udphdr), getLength(unpacked_udphdr), getChecksum(unpacked_udphdr)))