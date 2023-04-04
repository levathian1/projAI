#!/usr/bin/python           # This is server.py file

import socket  # Import socket module
from threading import Thread 
from socketserver import ThreadingMixIn 
import random # pour le tirage au sort du joueur 1 
import sys, getopt

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

import re  # findall
import time  # sleep

class myThread(Thread): 
    def __init__(self,ip,port): 
        Thread.__init__(self) 
        self.ip = ip 
        self.port = port 
        print ("[+] Nouveau thread démarré pour " + ip + ":" + str(port))
 
    def run(self): 
        while True : 
            data = con.recv(2048) 
            print("Le serveur a reçu des données:", data) 
            msg = raw_input("Entrez la réponse du serveur ou exit pour sortir:")
            if msg == 'exit':
                break
            con.send(msg)
            
            
###############
### SERVEUR ###
###############
def serveur(port):
    
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # host = socket.gethostname() # Get local machine name
    host = '127.0.0.1'  # l'ip locale de l'ordinateur

    # port = 12346                # Reserve a port for your service.
    s.bind((host, port))  # Bind to the port
    
    s.listen(5) # Now wait for client connection.
    print("Serveur: en attente de connexions des joueurs...")  
    (c1, (ip1,port1)) = s.accept() # Establish connection with client.
    print('Serveur: connexion établie avec le premier client IP: ', ip1, ' port:',port1)
    print('Serveur: en attente de connexion du second joueur')
    (c2, (ip2,port2)) = s.accept() # Establish connection with client.
    print('Serveur: connexion établie avec le second client IP: ', ip2, ' port:',port2)
    
    print("Serveur: tirage au sort du joueur qui commencera la partie")
    player = random.randint(1, 2)
    print("Serveur: le joueur ",player," commence la partie")
    print("Serveur: envoie de l'information aux joueurs")
    msg1 = "Serveur: A vous de jouer"
    msg2 = "Serveur: A votre adversaire de jouer"
    if player == 1:
        c1.send(str(player).encode())
        c1.send(str(msg1).encode())
        c2.send(str(msg2).encode())
    else:
        c2.send(str(player).encode())
        c1.send(str(msg2).encode())
        c2.send(str(msg1).encode()) 

    while True:
        print("Serveur: en attente d'un coup ")
        if player == 1:
            msg = c1.recv(1024).decode()
            print("commande recue du joueur 1 : ", msg)
            c2.send(str(msg).encode())
            player = 2
        else: # player == 2
            msg = c2.recv(1024).decode()
            print("commande recue du joueur 2 : ", msg)
            c1.send(str(msg).encode())
            player = 1

        if msg[2:9] == "abandon":
            c1.send(str("Serveur: Merci de vous êtes connectés. Au revoir.").encode())
            c1.close()  # Close the connection
        # if not msg:  # si on ne recoit plus rien
            break  # on break la boucle (sinon les bips vont se repeter)
        
        print(msg)  # print msg,"\a" affiche les donnees envoyees, suivi d'un bip sonore.
        vals = re.findall('\d+', msg)
        key1 = (int(vals[0]), int(vals[1]))
        key2 = (int(vals[2]), int(vals[3]))
        print(key1, key2)
 

def main(argv):
    port = ''
    try:
        opts, args = getopt.getopt(argv, "hp:d:", ["port=", "d="])
    except getopt.GetoptError:
        print('awale-MultiserveurGFX3.py -p <port> -d <dimension du plateau>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('awale-MultiserveurGFX3.py -p <port> -d <dimension du plateau>')
            sys.exit()
        elif opt in ("-p", "--port"):
            port = int(arg)
            print('Serveur: numero de port à utiliser par les clients : ', port)
        elif opt in ("-d", "--dimension"):
            d = int(arg)
            print('Serveur: dimension du plateau : ', d)
    # createBoard(d)
    # plotBoard()
    serveur(port)    

if __name__ == "__main__":
    main(sys.argv[1:])
