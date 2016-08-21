#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import json
import requests

import sys 

#Fonction analyse retour écoute micro en JSON
def texte_json(js):
    if js['_text'] == None:
        #play("error.wav")
        #play("Je-ne-comprends-pas.wav")
        return 0, 0, 0, 0
    else:
        if js['entities'] == {}:
            texte = js['_text']
            entities = 0
            confidence = 0
            intent = 0
            #play("error.wav")
            #play("Je-ne-trouve-pas-de-correspondance.wav")
            return texte, entities, confidence, intent
        else:
            texte = js['_text']
            for key, value in  js['entities'].iteritems():
                pass
            entities = str(key)
            confidence = value[0]['confidence']
            intent = str(value[0]['value'])
            return texte, entities, confidence, intent

def wit():
    token_wit = "MWUCLNWIHPFPHEAKAN5OTJFMB2MLMRWX" #
    #token_wit = "OHQ3X34NGICRFIRLUIBXRIKYD3G72RQB"

    headers = {'content-type' : 'audio/wav',"Authorization":"Bearer " + token_wit }
    audio = open('./testSon/termineauto.wav','rb').read()
    r=requests.post('https://api.wit.ai/speech?v=20160526',data=audio,headers=headers)
    
    return texte_json(r.json())

texte, entities, confidence, intent = wit()

print texte
print entities
print confidence
print intent
