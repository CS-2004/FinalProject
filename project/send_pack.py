from scapy.all import Ether, sendp

packet = Ether(
    dst="ff:ff:ff:ff:ff:ff",
    type=0x1234
) / b"hello ethernet"

sendp(packet)