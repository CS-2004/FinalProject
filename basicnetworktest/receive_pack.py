from scapy.all import sniff, Ether, Raw

CUSTOM_TYPE = 0x1234

def handle_packet(packet):

    if packet.haslayer(Ether):

        if packet.type == CUSTOM_TYPE:

            if packet.haslayer(Raw):

                message = packet[Raw].load.decode(errors="ignore")

                print("\n=== Ethernet Chat ===")
                print(f"From MAC: {packet.src}")
                print(message)

sniff(prn=handle_packet, store=False)