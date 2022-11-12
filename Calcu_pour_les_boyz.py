# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 19:54:56 2022

@author: Utilisateur
"""
import numpy as np
import pandas as pd
import streamlit as st
import io
#!python -m streamlit run .py

Titre_calcu = st.sidebar.title("Calculatrice OG")
Instruction = st.sidebar.write("Veuillez entrer deux chiffres/nombres et sélectionner l'opérateur de votre choix")
NB = st.sidebar.write("NB: pour effectuer une racine carré, entrez la valeur '0' au 1er chiffre/nombre")

nbr1 = float(st.sidebar.text_input("1er chiffre/nombre",0))

operateur = st.sidebar.radio("Opérateur",["+","-","X","/","Exposant","Racine carré"])

nbr2 = float(st.sidebar.text_input("2e chiffre/nombre",0))

if operateur == "+":
    resultat = nbr1 + nbr2
elif operateur == "-":
    resultat = nbr1 - nbr2
elif operateur == "X":
    resultat = nbr1 * nbr2
elif operateur == "/":
    resultat = nbr1 / nbr2
elif operateur == "Exposant":
    resultat = nbr1**nbr2
elif operateur == "Racine carré":
    if nbr1 == 0:
        resultat = np.sqrt(nbr2)
    else:
        avertissement = st.warning("Erreur, veuillez entrer la valeur '0' au 1er chiffre/nombre")
        resultat = "Erreur"
        
Affichage = st.title("Résultat de l'opération math: {}".format(resultat))


