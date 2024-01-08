from scapy.all import sniff, IP, TCP

def packet_callback(packet):
    if packet.haslayer(IP) and packet.haslayer(TCP):
        if packet[TCP].dport == 4000 or packet[TCP].sport == 4000:
            # This packet is associated with port 4000
            print(f"Packet: {packet.summary()}")

def sniff_packets(port=4000):
    print(f"Now listening for traffic on port {port}")
    sniff(prn=packet_callback, store=False, iface = "lo0")

if __name__ == "__main__":
    sniff_packets()
