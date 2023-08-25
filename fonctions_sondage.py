# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:05:55 2020

Auteur: Aubry Gatien

Avancement: TP3
"""
from random import randint
import copy
import json

def SondageInit():
    """Initialisation des variables du sondage 
    \nPROPOSITIONS: liste des PROPOSITIONS 
    \nscore: liste des scores \npersonnes: liste des personnes"""
    #Initiation des PROPOSITIONS
    PROPOSITIONS=[""]*100
    maproposition = """Boy-cotter des produits trop néfastes pour le climat"""
    PROPOSITIONS[0]=maproposition
    PROPOSITIONS[1]="""Manger plus de patates pour sauver les bébés phoques"""
    PROPOSITIONS[2]="""Voter aux elections"""
    PROPOSITIONS[3]="""Brûler le pétrole pour éviter qu'il soit consommé"""
    PROPOSITIONS[4]="""Faire des tests nucléaires dans l'atmosphère"""
    #Initiation des scores
    score=[0]*100
    #Initiation des personnes qui répondent au sondage
    personnes=[]
    return PROPOSITIONS, score, personnes

def SondageChargement():
    """Chargement des variables à partir du document texte
    \nArgumenbts en entrée:
    \nArguments en Sortie:
    """
    PROPOSITIONS=[""]*100
    score=[0]*100
    
    txt = open("bug.txt", "r", encoding="utf8")
    nb = txt.readline()
    for i in range(int(nb)):
        temp = txt.readline()
        score[i] = int(temp[0:5])
        PROPOSITIONS[i] = str(temp[5:len(temp)-2])
    txt.close()
    personnes = []
    return PROPOSITIONS, score, personnes

def SondageUnitaire(PROPOSITIONS, score, personnes):
    """Réalisation des étapes nécéssaires pour le sondage d'une seule personne
    \nArgumenbts en entrée:
    \nArguments en Sortie:
    """
    #On compte le nombre de proposition
    temp=0
    for i in range(100):
        if PROPOSITIONS[i] != "":
            temp+=1
    Nb_PROPOSITIONS = temp
    Nb_PROPOSITIONS_Final = temp
    
    entree = 0
    while entree != 4:
        if Nb_PROPOSITIONS == 0:
            print("Merci")
            break
        
        #Tirage d'une proposition et changement à la dernière place
        tirage = randint(0, Nb_PROPOSITIONS-1)
        print(PROPOSITIONS[tirage])
        tem = PROPOSITIONS[Nb_PROPOSITIONS-1]
        PROPOSITIONS[Nb_PROPOSITIONS-1] = PROPOSITIONS[tirage]
        PROPOSITIONS[tirage] = tem
       
        
        temp = score[Nb_PROPOSITIONS-1]
        score[Nb_PROPOSITIONS-1] = score[tirage]
        score[tirage] = temp
        
        Nb_PROPOSITIONS = Nb_PROPOSITIONS-1
        
        #Réponse de l'utilisateur
        print("D’accord (1), Sans avis (2), Pas d’accord (3), Fin (4),Autre idée (5):")
        entree=int(input())
        while entree != 1 and entree != 2 and entree != 3 and entree != 4 and entree != 5:
            print("réponse valide nécéssaire:")
            entree=int(input())
        if entree == 1:
            score[Nb_PROPOSITIONS] += 1
        elif entree == 2:
            score[Nb_PROPOSITIONS] += 0
        elif entree == 3:
            score[Nb_PROPOSITIONS] += -1
        elif entree == 5:
            if Nb_PROPOSITIONS_Final == 99:
                print("Tableau de Proposition déjà rempli au maximal de sa capacité")
            else:
                print("entrez votre propre proposition")
                PROPOSITIONS[Nb_PROPOSITIONS_Final]=str(input())
                Nb_PROPOSITIONS_Final+=1
                #Intégrer le truc demandé, non intégré car ça ne marche pas trop
                """
                temp = str(input())
                if AcceptationNouvelleProposition(temp):
                    PROPOSITIONS[Nb_PROPOSITIONS_Final]=temp
                    Nb_PROPOSITIONS_Final+=1
                """
    #Fin boucle while
    
    #Récupération des informations
    infoperso={'age':-1,'sexe':'error','departement':-1,'profession':'error'}
    infoperso['age']=int(input("Ton age SVP: "))
    infoperso['sexe']=int(input("Ton sexe SVP (1 pour H, 2 pour F, autre pour autre): "))
    infoperso['departement']=int(input("Ton departement SVP: "))
    infoperso['profession']=input("Ta profession SVP: ")
    print("""age: {0}\nsexe: {1}\ndepartement: {2}\nprofession: {3}\n""".format(infoperso['age'],infoperso['sexe'],infoperso['departement'],infoperso['profession']))
    personnes.append(copy.deepcopy(infoperso))
    return Nb_PROPOSITIONS_Final,personnes,score

def SondageTri(C,T,Nb_PROPOSITIONS_Final):
    """Tri d la liste des propositions en fonction des scores selon un ordre décroissant.
    \nArgumenbts en entrée: La matrice des propositions, la matrice des scores, le nombre de proposition
    \nArguments en Sortie:
    """
    for i in range(Nb_PROPOSITIONS_Final):
        for j in range(i+1,Nb_PROPOSITIONS_Final):
            if T[j]>T[i]:
                temp=T[i]
                T[i]=T[j]
                T[j]=temp
                temp=C[i]
                C[i]=C[j]
                C[j]=temp
    return C,T
    
def SondageAffichage(PROPOSITIONS,score,Nb_PROPOSITIONS_Final):
    """Affiche les résultats du sondage
    \nArgumenbts en entrée: La matrice des propositions, la matrice des scores, le nombre de proposition
    \nArguments en Sortie:
    """
    PROPOSITIONS, score = SondageTri(PROPOSITIONS,score,Nb_PROPOSITIONS_Final)
    tempp=0
    for i in range(100):
        if PROPOSITIONS[i] != "":
            tempp+=1
    print("-"*80)
    print("{: ^80s}".format("RESULTATS"))
    print("-"*80)
    
    for i in range(tempp):
        print("{: ^10d} Il Faut {:70}".format(score[i],PROPOSITIONS[i]))
    print('')

def SondageResume(personnes):
    """Affichages d'informations complémentaires sur les personnes ayant répondues au sondage
    \nArgumenbts en entrée: La matrice des informations sur les personnes
    \nArguments en Sortie: ceci est une procédure
    """
    #Partie Age
    TotalAge=0
    for i in range(len(personnes)):
        TotalAge+=personnes[i]['age']
    MoyenneAge=TotalAge/len(personnes)
    print("La moyenne d'age est:",MoyenneAge)
    print('')
    
    #Partie ListeDépartements
    ListeDepartements=[]
    print("Les gens viennent de:")
    for i in range(len(personnes)):
        ListeDepartements.append(personnes[i]['departement'])
        print(ListeDepartements[i])
    print('')
    
    #Partie Sexe
    H=0
    F=0
    N=0
    for i in range(len(personnes)):
        temp=personnes[i]['sexe']
        if temp == 1:
            H+=1
        elif temp == 2:
            F+=1
        else:
            N+=1
    print('Il y a '+str(H)+' Hommes soit '+str(int(100*H/(H+F+N)))+'% de la Population')
    print('Il y a '+str(F)+' Femmes soit '+str(int(100*F/(H+F+N)))+'% de la Population')
    print('Il y a '+str(N)+' Non Binaires soit '+str(int(100*N/(H+F+N)))+'% de la Population')
    print('')
    
    #partie professions
    Listeprofessions = []
    print("Les profession des gens sont: ")
    for i in range(len(personnes)):
        Listeprofessions.append(personnes[i]['profession'])
        print(Listeprofessions[i])


def SondageSauvegarde(PROPOSITIONS,score,Nb_PROPOSITIONS_Final,personnes):
    """sauvegarde des fichiers du sondage
    \nArgumenbts en entrée: La matrice des propositions, la matrice des scores, le nombre de proposition, la matrice des informations sur les personnes
    \nArguments en Sortie: Affichage imformatif informant la fin du processus de sauvegarde
    """
    txt = open("bug.txt", "w", encoding="utf8")
    txt.write(str(Nb_PROPOSITIONS_Final))
    
    for i in range(Nb_PROPOSITIONS_Final):
        txt.write("\n"+'%%0%dd' % (4,) % (score[i],)+" "+str(PROPOSITIONS[i])+" "*(100-len(PROPOSITIONS[i])))
    
    txt.close()
    infopersotot = dict()
    for i in range(len(personnes)):
        infopersotot["sonde #"+'%%0%dd' % (3,) % (i+1,)]=personnes[i]
    doc = open("info_perso.json", "a", encoding="utf8")
    for i in range(len(infopersotot)):
        json.dump(infopersotot["sonde #"+'%%0%dd' % (3,) % (i+1,)], doc, sort_keys=True, indent=4)
    doc.close()
    return print("sauvegarde terminée")

#=============================================================================
#=============================================================================
#=============================================================================

def Word(phrase,caractere):
    """Fonction qui renvoie un mot trouvé dans une phrase"""
    debut = caractere
    if caractere == None:
        return None, None
    while phrase[caractere]!=" " and phrase[caractere]!="\n":
        caractere += 1
        if caractere == len(phrase):
            return phrase[debut:caractere], None
    if phrase[caractere]=="\n":
        if debut!=caractere:
            return phrase[debut:caractere], caractere
        else:
            return None, None
    else:
        return phrase[debut:caractere], caractere + 1

def ChercherMotPhrase(phrase, MotCherche):
    """fonction qui cherche un mot dans une phrase"""
    mot, cara = Word(phrase, 0)
    while mot!=None:
        if mot == MotCherche:
            return True
        mot, cara = Word(phrase, cara)
    return False

def VerificationProposition(phrase):
    """Fonction principale qui vérifie si la proposition est dans le doc txt"""
    listeprop = open("liste_propositions.txt","r", encoding = "utf8")
    mot, next_cara = Word(phrase,0)
    prop = listeprop.readline()
    while mot!=None:
        while prop!="":
            if len(mot)>5 and ChercherMotPhrase(prop, mot):# Pourquoi teste t'on si len(mot)>5 ?
                return True, prop
            prop = listeprop.readline()
        listeprop.close()
        listeprop = open("liste_propositions.txt","r", encoding = "utf8")
        prop = listeprop.readline()
        mot, next_cara = Word(phrase,next_cara)
    return False, None


def AcceptationNouvelleProposition(PropositionUtilisateur):
    """demande à l'utilisateur"""
    bool, PhraseExistante = VerificationProposition(PropositionUtilisateur)
    if bool:
        print()
        print("Un autre sondé avait suggéré la proposition :")
        print()
        print(PhraseExistante)
        print()
        avis = input("Votre proposition est-elle similaire ? (O/N)")
        if avis == "O" or avis == "o":
            return False, PropositionUtilisateur
        else:
            return True, PhraseExistante
    else:
        return True, PhraseExistante
