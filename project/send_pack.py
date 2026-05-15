from scapy.all import Ether, sendp, Raw, get_if_hwaddr

CUSTOM_TYPE = 0x1234
iface = "enp0s3"

username = input("Enter username: ")
message = input("Enter message: ")
full_message = f"{username}: {message}"

packet = Ether(

    # reveal senders MAC
    src=get_if_hwaddr (iface),

    # please insert your MAC here
    dst="00:00:00:00:00:00",

    type=CUSTOM_TYPE
) / Raw(load=full_message.encode())

sendp (packet, iface="enp0s3", verbose=False)

print ("Message sent.")