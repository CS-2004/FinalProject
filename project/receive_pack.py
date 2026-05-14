from scapy.all import sniff, Ether

def handle_packet(packet):

    if packet.haslayer(Ether):

        if packet.type == 0x1234:

            print("Custom Ethernet Message:")
            print(bytes(packet.payload).decode(errors="ignore"))

sniff(prn=handle_packet)