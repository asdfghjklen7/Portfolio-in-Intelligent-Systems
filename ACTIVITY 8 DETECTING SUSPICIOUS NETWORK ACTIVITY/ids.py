from collections import Counter
from scapy.all import IP, Ether

# Simulated list of network packets
simulated_packets = [
    IP(src="192.168.1.10", dst="192.168.1.1"),
    IP(src="192.168.1.10", dst="192.168.1.1"),
    IP(src="192.168.1.20", dst="192.168.1.1"),
    IP(src="192.168.1.10", dst="192.168.1.1"),
    IP(src="192.168.1.20", dst="192.168.1.1"),
    IP(src="192.168.1.20", dst="192.168.1.1"),
    IP(src="192.168.1.10", dst="192.168.1.1"),
    IP(src="192.168.1.10", dst="192.168.1.1"),
    IP(src="192.168.1.10", dst="192.168.1.1"),
    IP(src="192.168.1.10", dst="192.168.1.1"),
    IP(src="192.168.1.10", dst="192.168.1.1"),
    IP(src="192.168.1.10", dst="192.168.1.1"),
] + [IP(src="192.168.1.150", dst="192.168.1.1") for _ in range(25)]

THRESHOLD = 20

print("Analyzing simulated network packets...")
print("Packet counts per source IP:")

# Count occurrences of each source IP
ip_counts = Counter(pkt[IP].src for pkt in simulated_packets if IP in pkt)

for ip, count in ip_counts.items():
    print(f"- {ip}: {count} packets")

print("\nChecking for suspicious activity....")
for ip, count in ip_counts.items():
    if count > THRESHOLD:
        print(f"!!! ALERT: Suspicious activity detected from {ip}. Packets sent: {count}")