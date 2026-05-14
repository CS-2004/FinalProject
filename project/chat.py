from scapy.all import sniff, Ether, Raw, sendp, get_if_hwaddr
import threading

CUSTOM_TYPE = 0x1234
INTERFACE = "eth0"

username = input("Enter username: ")

my_mac = get_if_hwaddr(INTERFACE)

def receive_packets(packet):

    if packet.haslayer(Ether):

        if packet.type == CUSTOM_TYPE:

            # Ignore packets sent by ourselves
            if packet.src == my_mac:
                return

            if packet.haslayer(Raw):

                message = packet[Raw].load.decode(errors="ignore")

                print(f"\n{message}")

def start_sniffing():

    sniff(
        iface=INTERFACE,
        prn=receive_packets,
        store=False
    )

sniffer_thread = threading.Thread(target=start_sniffing)

sniffer_thread.daemon = True

sniffer_thread.start()

while True:

    message = input()

    full_message = f"{username}: {message}"

    packet = Ether(
        dst="ff:ff:ff:ff:ff:ff",
        type=CUSTOM_TYPE
    ) / full_message.encode()

    sendp(packet, iface=INTERFACE)