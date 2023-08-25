def Word(phrase, caractere):
    debut = caractere
    if caractere == None: #<========================================================================1 erreur
        return None, None
    while phrase[caractere] != " " and phrase[caractere] != "\n":
        caractere += 1
        if caractere == len(phrase):
            return phrase[debut:caractere], None
    if phrase[caractere] == "\n":
        if debut != caractere:
            return phrase[debut:caractere], caractere
        else:
            return None, None #<====================================================================1 erreur
    else:
        return phrase[debut:caractere], caractere + 1

def ChercherMotPhrase(phrase, MotCherche):
    mot, cara = Word(phrase, 0)
    while mot != None:
        if mot == MotCherche:
            return True #<==========================================================================1 erreur
        mot, cara = Word(phrase, cara)
    return False #<=================================================================================1 erreur


def VerificationProposition(phrase):
    listeprop = open("liste_propositions.txt", "r", encoding = "utf8") #<===========================1 erreur
    mot, next_cara = Word(phrase, 0) #<=============================================================1 erreur
    prop = listeprop.readline()
    while mot != None:
        while prop != "":
            if len(mot) > 5 and ChercherMotPhrase(prop, mot):# Pourquoi teste t'on si len(mot)>5 ?
                return True, prop
            prop = listeprop.readline()
        listeprop.close()
        listeprop = open("liste_propositions.txt", "r", encoding = "utf8") #<=======================1 erreur
        prop = listeprop.readline()
        mot, next_cara = Word(phrase, next_cara)
    listeprop.close() #<============================================================================1 erreur
    return False, None


def GarderPropositionUtilisateur(PropositionUtilisateur):
    bool, PhraseExistante = VerificationProposition(PropositionUtilisateur)
    if bool:
        print()
        print("Un autre sondé avait suggéré la proposition :")
        print()
        print(PhraseExistante)
        print()
        avis = input("Votre proposition est-elle similaire ? (O/N)")
        if avis == "O" and avis == "o":
            return False, PhraseExistante
        else:
            return True, PropositionUtilisateur
    else:
        return True, PropositionUtilisateur