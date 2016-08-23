#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import timeout #fichier pour le lancement des commandes shell avec temps maxi
import fonction #l'ensemble des fonctions de l'appli
from snowboy.Snowboy import Snowboy

token_wit = "K3RY7CDERSUFT5KJTYJH6IVKKDBSI2WH" # 
#token_wit = "OHQ3X34NGICRFIRLUIBXRIKYD3G72RQB"

sensibiliteSnowboy = 0.4
niveauConfidence = 0.6


fonction.play("Bonjour-je-suis-Optimus.wav") #message au lancement de l'appli 

fin = False #si fin = True arret de l'appli
while (not fin):
    #attente mot magique
    snow = Snowboy('snowboy/resources/optimus.pmdl', sensibiliteSnowboy)
    snow.detection()

    """enregistrement des commandes
       trois temps d'enregistrement maxi avec un timeout de 10 secondes
    """	
    i = 0 #nombre d'enregistrement 
    retourRecord= -1 #retour 0 si enregistrement ok ou autre si pas OK
    while  retourRecord != 0 and i < 3: 
        retourRecord = fonction.record()
        i = i + 1
        #retourRecord = 0

    if retourRecord != 0: #si enregistrement HS
    	fonction.play("error.wav")
        fonction.play("Je-n-ai-pas-entendu-de-commande.wav")
    else: #si enregistrement OK envoie à WIT retour du texte, de niveau de réussite et du dossier
        retour = fonction.wit(token_wit, niveauConfidence)
        if retour:   
            print "commande validée"
            print retour[0], retour[1], retour[2], retour[3]        
    
    fin = True
