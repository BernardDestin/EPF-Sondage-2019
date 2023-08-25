# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:07:55 2020

Auteur: Aubry Gatien

Avancement: TP5
"""
import os
import json

from fonctions_sondage import SondageInit
from fonctions_sondage import SondageChargement
from fonctions_sondage import SondageUnitaire
from fonctions_sondage import SondageAffichage
from fonctions_sondage import SondageResume
from fonctions_sondage import SondageSauvegarde

#Variables=SondageInit()
VARIABLES = SondageChargement()
PROPOSITIONS = VARIABLES[0]
score = VARIABLES[1]
personnes = VARIABLES[2]

print("Veuillez entrer le nombre de participants:")
N = int(input("Nombre de particpants:"))

for i in range(N):
    temp = SondageUnitaire(PROPOSITIONS, score, personnes)
    Nb_Propositions_Final = temp[0]
    personnes = temp[1]
    score = temp[2]

SondageAffichage(PROPOSITIONS, score, Nb_Propositions_Final)

SondageResume(personnes)


#===================================================================================================
SondageSauvegarde(PROPOSITIONS, score, Nb_Propositions_Final, personnes)
#===================================================================================================
#Première ligne = 1 characteres
#Une ligne = 105 characteres
