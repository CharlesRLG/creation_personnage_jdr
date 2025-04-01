import tkinter as tk
from tkinter import ttk

def calcule_caracs():
    race = race_saisi.get()
    if race == "Humain":
        caracs_label.config(text = "CC : 20, CT : 20, Force : 20, Endurance : 20, Initiative : 20, Agilité : 20, Dextérité : 20, Intelligence : 20, Force_Mental : 20, Sociabilité : 20, Chance : 20")
    elif race == "Barbare":
        caracs_label.config(text = "CC : 30, CT : 20, Force : 25, Endurance : 25, Initiative : 20, Agilité : 20, Dextérité : 20, Intelligence : 0, Force_Mental : 20, Sociabilité : 20, Chance : 20")
    elif race == "Nain":
        caracs_label.config(text = "CC : 30, CT : 20, Force : 20, Endurance : 40, Initiative : 20, Agilité : 5, Dextérité : 5, Intelligence : 20, Force_Mental : 20, Sociabilité : 20, Chance : 20")

## Crée la fenetre principale
root = tk.Tk()
root.title("Création de Personnage")

## Saisie du nom
tk.Label(root, text="Nom du personnage :").pack()
nom_perso_saisi = tk.Entry(root)
nom_perso_saisi.pack()

## Choix de la race
tk.Label(root, text="Race :").pack()
race_saisi = tk.StringVar(value="Humain")
race_menu = ttk.Combobox(root, textvariable = race_saisi)
race_menu['values'] = ("Humain", "Barbare", "Nain")
race_menu.pack()

## Bouton pour calculer les statistiques
tk.Button(root, text = "Calculer les caractéristiques", command = calcule_caracs).pack()

## Afficher les caracs
caracs_label = tk.Label(root, text = "")
caracs_label.pack()

root.mainloop()