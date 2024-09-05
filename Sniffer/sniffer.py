from scapy.all import *

iPkt = 0

def process_pocket(pkt):
    global iPkt
    iPkt += 1
    print("Ho letto un pacchetto sulla tua macchina" + str(iPkt))

sniff(iface = "enp4s0", filter = "tcp", prn = process_pocket)