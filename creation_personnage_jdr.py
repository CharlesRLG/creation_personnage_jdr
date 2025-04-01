import tkinter as tk
from tkinter import ttk

def points_carac_repartition():
    total_reparti = int(cC_saisi.get()) + int(cT_saisi.get()) + int(force_saisi.get()) + int(endu_saisi.get()) + int(init_saisi.get()) + int(agi_saisi.get()) + int(dex_saisi.get()) + int(intel_saisi.get()) + int(force_ment_saisi.get()) + int(socia_saisi.get())
    if total_reparti > 120:
        warning_label.config(text="Vous avez dépassez la limite de 120 points !", fg="red")
    else:
        warning_label.config(text="")
    points_restants.set(f"Points restants : {120 - total_reparti}")

def calcule_caracs():
    race = race_saisi.get()
    if race == "Humain":
        message = f"Nom : {nom_perso_saisi} \n Race : Humain"
        message += f" CC : {cC_saisi.get() + 20} \n CT : {cT_saisi.get() + 20} \n Force : {force_saisi.get() + 20} \n Endurance : {endu_saisi.get() + 20} \n Initiative : {init_saisi.get() + 20} \n Agilité : {agi_saisi.get() + 20} \n Dextérité : {dex_saisi.get() + 20} \n Intelligence : {intel_saisi.get() + 20} \n Force Mental : {force_ment_saisi.get() + 20} \n Sociabilité : {socia_saisi.get() + 20} \n Chance : 20"
    
    elif race == "Humain":
        message = f"Nom : {nom_perso_saisi} \n Race : Humain"
        message += f" CC : {cC_saisi.get() + 30} \n CT : {cT_saisi.get() + 20} \n Force : {force_saisi.get() + 25} \n Endurance : {endu_saisi.get() + 25} \n Initiative : {init_saisi.get() + 20} \n Agilité : {agi_saisi.get() + 20} \n Dextérité : {dex_saisi.get() + 20} \n Intelligence : {intel_saisi.get() + 0} \n Force Mental : {force_ment_saisi.get() + 20} \n Sociabilité : {socia_saisi.get() + 20} \n Chance : 20"
      
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
race_menu['values'] = ("Humain", "Barbare")
race_menu.pack()

## Répartition des caractéristiques
tk.Label(root, text = "Répartition des points de caractéristiques :").pack()

cC_saisi = tk.IntVar(value=0)
cT_saisi = tk.IntVar(value=0)
force_saisi = tk.IntVar(value=0)
endu_saisi = tk.IntVar(value=0)
init_saisi = tk.IntVar(value=0)
agi_saisi = tk.IntVar(value=0)
dex_saisi = tk.IntVar(value=0)
intel_saisi = tk.IntVar(value=0)
force_ment_saisi = tk.IntVar(value=0)
socia_saisi = tk.IntVar(value=0)

tk.Label(root, text = "CC :").pack()
tk.Scale(root, from_ = 0, to = 40, orient = "horizontal", variable = cC_saisi, command = lambda x: points_carac_repartition()).pack()

tk.Label(root, text = "CT :").pack()
tk.Scale(root, from_ = 0, to = 40, orient = "horizontal", variable = cT_saisi, command = lambda x: points_carac_repartition()).pack()

tk.Label(root, text = "Force :").pack()
tk.Scale(root, from_ = 0, to = 40, orient = "horizontal", variable = force_saisi, command = lambda x: points_carac_repartition()).pack()

tk.Label(root, text = "Endurance :").pack()
tk.Scale(root, from_ = 0, to = 40, orient = "horizontal", variable = endu_saisi, command = lambda x: points_carac_repartition()).pack()

tk.Label(root, text = "Initiative :").pack()
tk.Scale(root, from_ = 0, to = 40, orient = "horizontal", variable = init_saisi, command = lambda x: points_carac_repartition()).pack()

tk.Label(root, text = "Agilité :").pack()
tk.Scale(root, from_ = 0, to = 40, orient = "horizontal", variable = agi_saisi, command = lambda x: points_carac_repartition()).pack()

tk.Label(root, text = "Dextérité :").pack()
tk.Scale(root, from_ = 0, to = 40, orient = "horizontal", variable = dex_saisi, command = lambda x: points_carac_repartition()).pack()

tk.Label(root, text = "Intelligence :").pack()
tk.Scale(root, from_ = 0, to = 40, orient = "horizontal", variable = intel_saisi, command = lambda x: points_carac_repartition()).pack()

tk.Label(root, text = "Force Mentale :").pack()
tk.Scale(root, from_ = 0, to = 40, orient = "horizontal", variable = force_ment_saisi, command = lambda x: points_carac_repartition()).pack()

tk.Label(root, text = "Sociabilité :").pack()
tk.Scale(root, from_ = 0, to = 40, orient = "horizontal", variable = socia_saisi, command = lambda x: points_carac_repartition()).pack()

points_restants = tk.StringVar(value = "Points restants : 120")
tk.Label(root, textvariable=points_restants).pack()

## Avertissement en cas de dépassement
warning_label = tk.Label(root, text="")
warning_label.pack()

## Bouton pour calculer les statistiques
tk.Button(root, text = "Calculer les caractéristiques", command = calcule_caracs).pack()

## Afficher les caracs
caracs_label = tk.Label(root, text = "")
caracs_label.pack()

root.mainloop()