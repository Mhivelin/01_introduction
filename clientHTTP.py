# Un client HTTP très simple
import socket

# un exemple d'interrogation d'un serveur DNS
print("Interrogation du DNS: "+socket.gethostbyname("www.moodle-fnd.fr"))

# 1- Construire un objet qui représente la socket
#    vers laquelle le client veut se connecter
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2- ouvrir la connection vers la socket
s.connect(("www.moodle-fnd.fr",80))

# 3- construire le message à envoyer (ici une requête http).
request = "GET / HTTP/1.1\r\n"
request += "Host: www.moodle-fnd.fr\r\n"
request += "Connection: Close\r\n\r\n"

# 4- l'envoyer sur la socket
s.send(request.encode('UTF-8'))

# 5- lire 15 octet sur la socket (augmenter pour lire plus...)
data = s.recv(150)

# Convertir le tableau de 15 octets en une chaine de caractère
#    et l'afficher.
print(data.decode('utf-8'))

s.close()