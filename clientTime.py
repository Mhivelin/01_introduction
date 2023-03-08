from socket import AF_INET, SOCK_DGRAM
import sys
import socket
import struct, time


# Fonction pour faire une requête de type NTP
def get_ntp_time(host: str = "pool.ntp.org"):
    port = 123
    buf = 1024
    address = (host, port)

    # Message à envoyer
    msg = '\x1b' + 47 * '\0'

    # Time de reference (in seconds since 1900-01-01 00:00:00)
    TIME1970 = 2208988800  # 1970-01-01 00:00:00

    # Connexion au server
    client = socket.socket(AF_INET, SOCK_DGRAM)

    # Envoi de la request
    client.sendto(msg.encode('utf-8'), address)

    # Réception de la réponse
    msg, address = client.recvfrom(buf)

    # On doit interpréter la réponse qui a un format spécial
    t = struct.unpack("!12I", msg)[10]

    # Différence entre la réponse et le temps de référence
    t -= TIME1970
    return time.ctime(t).replace("  ", " ")


if __name__ == "__main__":
    print(get_ntp_time())
