# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 15:27:10 2019

@author: alepe
"""
from Regle import regle

def cartesJouables(cartesIA, cartes_pli, couleur_atout, carte_meneuse):
    cartes_possibles=[] #va nous donner les cartes que peut jouer l'IA
    for i in range(len(cartesIA)):
        if regle(cartesIA, cartes_pli, cartesIA[i], couleur_atout, carte_meneuse):
            cartes_possibles.append(i)
    return cartes_possibles