from scapy.all import sniff, Ether, Raw

CUSTOM_TYPE = 0x1234

def handle_packet(packet):
    try:
        if packet.haslayer(Ether) and packet.type == CUSTOM_TYPE and packet.haslayer(Raw):
            payload = packet[Raw].load.decode(errors="ignore")

            print("\n=== Ethernet Chat ===")
            print(f"From MAC: {packet.src}")
            print(payload)

    except Exception as e:
        print(f"Error: {e}")

sniff(prn=handle_packet, store=False, iface="enp0s3")