# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:46:11 2019

@author: alepe
"""
import random

def melangeCarte(paquet):
    nouveau_paquet = []
    longueur=len(paquet)
    for i in range(len(paquet)):
        nouveau_paquet.append(paquet[random.randint(0,longueur-i-1)])
        paquet.remove(nouveau_paquet[-1])
    return nouveau_paquet

    

