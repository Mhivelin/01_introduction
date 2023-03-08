import random
import socket
import sys
import struct


HOST = '127.0.0.1'
PORT = 2001

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

while 1:
    print("serveur simple en attente sur "+HOST+":"+str(PORT))
    mySocket.listen(5)

    connexion, adresse = mySocket.accept()
    print("Un client est connecté depuis l'adresse IP %s et le port %s" % (adresse[0], adresse[1]))

    connexion.send(("Hello. Envoyer un nombre maximum\n").encode('UTF-8'))

    ##VERSION AVEC ENTIER BINAIRE (demande un client ad'hoc)
    #MAX = socket.ntohl(struct.unpack('I',connexion.recv(4))[0]);
    #print("Max reçu: " + str(MAX))
    #NUMBER = random.randint(0, MAX)
    #print("Nombre à deviner: " + str(NUMBER))
    #while 1:
    #    connexion.send("Votre proposition ?\n".encode('UTF-8'))
    #    propositionClient = socket.ntohl(struct.unpack('I',connexion.recv(4))[0]);
    #    if (propositionClient>NUMBER):
    #        connexion.send("Plus petit".encode('UTF-8'))
    #    elif (propositionClient<NUMBER):
    #        connexion.send("Plus grand".encode('UTF-8'))
    #    elif (propositionClient==NUMBER):
    #         connexion.send("Bravo !".encode('UTF-8'))
    #       break


    ##VERSION AVEC CHAINE DE CARACTERES (utilisable avec telnet)
    MAX = connexion.recv(1024).decode('UTF-8')
    print("Max reçu: " + MAX)
    NUMBER = random.randint(0, int(MAX));
    print("Nombre à deviner: " + str(NUMBER))
    while 1:
        connexion.send("Votre proposition ?\n".encode('UTF-8'))
        propositionClient = int(connexion.recv(1024).decode('UTF-8'))
        if (propositionClient>NUMBER):
            connexion.send("Plus petit\n".encode('UTF-8'))
        elif (propositionClient<NUMBER):
            connexion.send("Plus grand\n".encode('UTF-8'))
        elif (propositionClient==NUMBER):
           connexion.send("Bravo !".encode('UTF-8'))
           break

    connexion.send("Good Bye.".encode('UTF-8'))
    connexion.close()
    print("Connexion interrompue.\n")

    ch = input("Attendre un autre client ? <R>ecommencer <T>erminer ? ")
    if ch.upper() == 'T':
        break