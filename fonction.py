#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import json
import timeout
import requests

#Fonction analyse retour écoute micro en JSON
def texte_json(js, niveauConfidence):
    if js['_text'] == None:
        #play("error.wav")
        #play("Je-ne-comprends-pas.wav")
        print "Je-ne-comprends-pas pas de texte"
        return False
    else:
        if js['entities'] == {}:
            #play("error.wav")
            #play("Je-ne-trouve-pas-de-correspondance.wav")
            #fonction.parole(js['_text'])
            print "Je-ne-trouve-pas-de-correspondance a " + js['_text']
            return False
        else:
            texte = js['_text']
            for key, value in  js['entities'].iteritems():
                pass
            entities = str(key)
            confidence = value[0]['confidence']
            intent = str(value[0]['value'])
            if confidence < niveauConfidence: #niveau de confidence pour va$
                #play("error.wav")
                #fonction.play("Je-ne-comprends-pas-la-commande.wav")
                #fonction.parole(texte)
                print "Je-ne-comprends-pas-la-commande confidence < a " + str(niveauConfidence)
                return False
            else:
                return texte, entities, confidence, intent

def parole(texte):
    cmd = "pico2wave -l=fr-FR -w=fichier.wav \"" + texte + "\" && play fichier.wav"
    timeout.run(cmd,shell = True)

def record():
    cmd = 'rec -V1 -r 16000 -c 1 -b 16 -e signed-integer --endian little jarvis-record.wav silence 1 2 12% 1 0:00:01 12% trim 0 10'
    retour, aa, bb = timeout.run(cmd,shell = True, timeout = 10)
    return retour

def play(fichier):
    cmd = "play les_sons/" + fichier
    timeout.run(cmd,shell = True)

def wit(token_wit, niveauConfidence):
    token_wit = "MWUCLNWIHPFPHEAKAN5OTJFMB2MLMRWX" #
    #token_wit = "OHQ3X34NGICRFIRLUIBXRIKYD3G72RQB"

    headers = {'content-type' : 'audio/wav',"Authorization":"Bearer " + token_wit }
    #audio = open('./jarvis-record.wav','rb').read()
    audio = open('./testSon/allume-lustre-chambre.wav','rb').read()

    r=requests.post('https://api.wit.ai/speech?v=20160526',data=audio,headers=headers)

    return texte_json(r.json(), niveauConfidence)

