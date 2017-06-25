from scapy.all import *

def imprimir(pacotes):
    hd = str(pacotes[TCP].payload)[0:4]
    if hd == 'POST':
        print pacotes[TCP].payload

sniff(filter='port 80', store=0, prn=imprimir)
