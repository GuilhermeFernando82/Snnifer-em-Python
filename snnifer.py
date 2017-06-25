from scapy.all import *

def imprimir(pacotes):
    print pacotes[TCP].payload

sniff(filter='port 80', store=0, prn=imprimir)