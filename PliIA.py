# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:40:22 2019

@author: telmar
"""
from Regle import regle
from CompareCarteJeu import compareCarteJeu
import random as rd
def pliIA(jeu1, jeu2, jeu3, jeu4, gagnant_prec, belote,rebelote, couleur_atout,joueur,num_pli):
    joues = 0
    cartes_pli = []
    carte_meneuse = 0
    gagnant = 4
    while joues < 4:
        autorise=False
        if joueur[(gagnant_prec + joues) % 4][1] != "IA":
            print("c\'est au tour de: "+ joueur[(gagnant_prec + joues) % 4])
            if (gagnant_prec + joues) % 4 == 0:
                while not autorise:
                    print("Cartes jouées :", cartes_pli)
                    print("atout: " + couleur_atout)
                    print("Mon jeu :")
                    for i in range(len(jeu1)):
                        print(i + 1, ":", jeu1[i], "\n")
                    choix = input("Quelle carte jouer ?")
                    choix = int(choix)
                    if choix > 8-num_pli: 
                        print("ce numéro n\'est pas autorisé")
                    elif regle(jeu1,cartes_pli,jeu1[choix-1],couleur_atout,carte_meneuse):
                        autorise = True
                    else :
                        print("vous n'etes pas autorisé à jouer cette carte")
                if jeu1[choix-1][1]==couleur_atout and jeu1[choix-1][0] in ["Dame","Roi"] and belote==4:
                    belote = input("Belote ? (y/n)")
                    while belote != "y" and belote != "n" :
                        print("argument non valide")
                        belote = input("Belote ? (y/n)")
                elif jeu1[choix-1][1]==couleur_atout and jeu1[choix-1][0] in ["Dame","Roi"] and belote==0:
                    rebelote = input("Rebelote ? (y/n)")
                    while rebelote != "y" and rebelote != "n" :
                        print("argument non valide")
                        rebelote = input("Rebelote ? (y/n)")
                cartes_pli.append(jeu1[choix - 1])
                if belote == "y":
            	    belote = 0
                if rebelote == "y":
            	    rebelote = 0
                jeu1.pop(choix-1)
            elif (gagnant_prec + joues) % 4 == 1:
                while not autorise:
                    print("Cartes jouées :", cartes_pli)
                    print("atout: " + couleur_atout)
                    print("Mon jeu :")
                    for i in range(len(jeu2)):
                        print(i + 1, ":", jeu2[i], "\n")
                    choix = input("Quelle carte jouer ?")
                    choix = int(choix)
                    if choix > 8-num_pli: 
                        print("ce numéro n\'est pas autorisé")
                    elif regle(jeu2,cartes_pli,jeu2[choix-1],couleur_atout,carte_meneuse):
                        autorise = True
                    else :
                        print("vous n'etes pas autorisé à jouer cette carte")
                if jeu2[choix-1][1]==couleur_atout and jeu2[choix-1][0] in ["Dame","Roi"] and belote==4:
                    belote = input("Belote ? (y/n)")
                    while belote != "y" and belote != "n" :
                        print("argument non valide")
                        belote = input("Belote ? (y/n)")
                elif jeu2[choix-1][1]==couleur_atout and jeu2[choix-1][0] in ["Dame","Roi"] and belote==1:
                    rebelote = input("Rebelote ? (y/n)")
                    while rebelote != "y" and rebelote != "n" :
                        print("argument non valide")
                        rebelote = input("Rebelote ? (y/n)")
                cartes_pli.append(jeu2[choix - 1])
                if belote == "y":
            	    belote = 1
                if rebelote == "y":
            	    rebelote = 1
                jeu2.pop(choix-1)
            elif (gagnant_prec + joues) % 4 == 2:
                while not autorise:
                    print("Cartes jouées :", cartes_pli)
                    print("atout: " + couleur_atout)
                    print("Mon jeu :")
                    for i in range(len(jeu3)):
                        print(i + 1, ":", jeu3[i], "\n")
                    choix = input("Quelle carte jouer ?")
                    choix = int(choix)
                    if choix > 8-num_pli: 
                        print("ce numéro n\'est pas autorisé")
                    elif regle(jeu3,cartes_pli,jeu3[choix-1],couleur_atout,carte_meneuse):
                        autorise = True
                    else :
                        print("vous n'etes pas autorisé à jouer cette carte")
                if jeu3[choix-1][1]==couleur_atout and jeu3[choix-1][0] in ["Dame","Roi"] and belote==4:
                    belote = input("Belote ? (y/n)")
                    while belote != "y" and belote != "n" :
                        print("argument non valide")
                        belote = input("Belote ? (y/n)")
                elif jeu3[choix-1][1]==couleur_atout and jeu3[choix-1][0] in ["Dame","Roi"] and belote==2:
                    rebelote = input("Rebelote ? (y/n)")
                    while rebelote != "y" and rebelote != "n" :
                        print("argument non valide")
                        rebelote = input("Rebelote ? (y/n)")
                cartes_pli.append(jeu3[choix - 1])
                if belote == "y":
            	    belote = 2
                if rebelote == "y":
            	    rebelote = 2
                jeu3.pop(choix-1)
            elif (gagnant_prec + joues) % 4 == 3:
                while not autorise:
                    print("Cartes jouées :", cartes_pli)
                    print("atout: " + couleur_atout)
                    print("Mon jeu :")
                    for i in range(len(jeu4)):
                        print(i + 1, ":", jeu4[i], "\n")
                    choix = input("Quelle carte jouer ?")
                    choix = int(choix)
                    if choix > 8-num_pli: 
                        print("ce numéro n\'est pas autorisé")
                    elif regle(jeu4,cartes_pli,jeu4[choix-1],couleur_atout,carte_meneuse):
                        autorise = True
                    else :
                        print("vous n'etes pas autorisé à jouer cette carte")
                if jeu4[choix-1][1]==couleur_atout and jeu4[choix-1][0] in ["Dame","Roi"] and belote==4:
                    belote = input("Belote ? (y/n)")
                    while belote != "y" and belote != "n" :
                        print("argument non valide")
                        belote = input("Belote ? (y/n)")
                elif jeu4[choix-1][1]==couleur_atout and jeu4[choix-1][0] in ["Dame","Roi"] and belote==3:
                    rebelote = input("Rebelote ? (y/n)")
                    while rebelote != "y" and rebelote != "n" :
                        print("argument non valide")
                        rebelote = input("Rebelote ? (y/n)")
                cartes_pli.append(jeu4[choix - 1])
                if belote == "y":
            	    belote = 3
                if rebelote == "y":
            	    rebelote = 3
                jeu4.pop(choix-1)

        else:
            cartes_possibles = []
            if (gagnant_prec + joues) % 4 == 0:
                for i in range(len(jeu1)):
                    if regle(jeu1, cartes_pli, jeu1[i], couleur_atout, carte_meneuse):
                        cartes_possibles.append(i)
                jouer = rd.randint(1, len(cartes_possibles))
                card = cartes_possibles[jouer-1]
                cartes_pli.append(jeu1[card])
                if jeu1[card][1] == couleur_atout and jeu1[card][0] in ["Dame", "Roi"] and belote == 4:
                    belote = 0
                elif jeu1[card][1] == couleur_atout and jeu1[card][0] in ["Dame", "Roi"] and belote == 0:
                    rebelote = 0
                jeu1.pop(card)
            elif (gagnant_prec + joues) % 4 == 1:
                for i in range(len(jeu2)):
                    if regle(jeu2, cartes_pli, jeu2[i], couleur_atout, carte_meneuse):
                        cartes_possibles.append(i)
                jouer = rd.randint(1, len(cartes_possibles))
                card = cartes_possibles[jouer-1]
                cartes_pli.append(jeu2[card])
                if jeu2[card][1] == couleur_atout and jeu2[card][0] in ["Dame", "Roi"] and belote == 4:
                    belote = 1
                elif jeu2[card][1] == couleur_atout and jeu2[card][0] in ["Dame", "Roi"] and belote == 0:
                    rebelote = 1
                jeu2.pop(card)
            elif (gagnant_prec + joues) % 4 == 2:
                for i in range(len(jeu3)):
                    if regle(jeu3, cartes_pli, jeu3[i], couleur_atout, carte_meneuse):
                        cartes_possibles.append(i)
                jouer = rd.randint(1, len(cartes_possibles))
                card = cartes_possibles[jouer-1]
                cartes_pli.append(jeu3[card])
                if jeu3[card][1] == couleur_atout and jeu3[card][0] in ["Dame", "Roi"] and belote == 4:
                    belote = 2
                elif jeu3[card][1] == couleur_atout and jeu3[card][0] in ["Dame", "Roi"] and belote == 0:
                    rebelote = 2
                jeu3.pop(card)
            elif (gagnant_prec + joues) % 4 == 3:
                for i in range(len(jeu4)):
                    if regle(jeu4, cartes_pli, jeu4[i], couleur_atout, carte_meneuse):
                        cartes_possibles.append(i)
                jouer = rd.randint(1, len(cartes_possibles))
                card = cartes_possibles[jouer-1]
                cartes_pli.append(jeu4[card])
                if jeu4[card][1] == couleur_atout and jeu4[card][0] in ["Dame", "Roi"] and belote == 4:
                    belote = 3
                elif jeu4[card][1] == couleur_atout and jeu4[card][0] in ["Dame", "Roi"] and belote == 0:
                    rebelote = 3
                jeu4.pop(card)
        
        if carte_meneuse == 0:
            carte_meneuse = cartes_pli[-1]
            gagnant=(gagnant_prec + joues) % 4
        else:
            gain = compareCarteJeu(carte_meneuse, cartes_pli[-1], couleur_atout)
            if gain == -1:
                carte_meneuse = cartes_pli[-1]
                gagnant = (gagnant_prec + joues) % 4
            elif gain == 1:
                carte_meneuse = carte_meneuse
        
        joues += 1

 
    return jeu1, jeu2, jeu3, jeu4, gagnant, cartes_pli, belote,rebelote
