from scapy.all import Ether, sendp

CUSTOM_TYPE = 0x1234

username = input("Enter username: ")
message = input("Enter message: ")

full_message = f"{username}: {message}"

packet = Ether(
    dst="ff:ff:ff:ff:ff:ff",
    type=CUSTOM_TYPE
) / full_message.encode()

sendp(packet)

print("Message sent.")