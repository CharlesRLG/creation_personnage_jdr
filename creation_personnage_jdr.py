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
    total_reparti = int(cC_saisi.get()) + int(cT_saisi.get()) + int(force_saisi.get()) + int(endu_saisi.get()) + int(init_saisi.get()) + int(agi_saisi.get()) + int(dex_saisi.get()) + int(intel_saisi.get()) + int(force_ment_saisi.get()) + int(socia_saisi.get())
    if total_reparti > 120:
        result_label.config(text="La répartirion des points est incorrecte !")
    else:
        if race == "Humain":
            message = f"Nom : {nom_perso_saisi.get()} \n Race : Humain"
            message += f" CC : {cC_saisi.get() + 20} \n CT : {cT_saisi.get() + 20} \n Force : {force_saisi.get() + 20} \n Endurance : {endu_saisi.get() + 20} \n Initiative : {init_saisi.get() + 20} \n Agilité : {agi_saisi.get() + 20} \n Dextérité : {dex_saisi.get() + 20} \n Intelligence : {intel_saisi.get() + 20} \n Force Mental : {force_ment_saisi.get() + 20} \n Sociabilité : {socia_saisi.get() + 20} \n Chance : 20"

        elif race == "Barbare":
            message = f"Nom : {nom_perso_saisi.get()} \n Race : Barbare"
            message += f" CC : {cC_saisi.get() + 30} \n CT : {cT_saisi.get() + 20} \n Force : {force_saisi.get() + 25} \n Endurance : {endu_saisi.get() + 25} \n Initiative : {init_saisi.get() + 20} \n Agilité : {agi_saisi.get() + 20} \n Dextérité : {dex_saisi.get() + 20} \n Intelligence : {intel_saisi.get() + 0} \n Force Mental : {force_ment_saisi.get() + 20} \n Sociabilité : {socia_saisi.get() + 20} \n Chance : 20"
        result_label.config(text=message )
    
def designation_talent_race():
    listTalentRace.delete(0, tk.END)
    race = race_saisi.get()
    if race == "Humain":
        talent_race = ["Perspicace ou Sociale", "Destinée", "3 compétences aléatoires"]
    elif race == "Barbare":
        talent_race = ["Dure à cuire", "Destinée", "Ambidextre", "Orientation"]
    else:
        talent_race = ["Aucun talent associé"]

    for talent in talent_race:
        listTalentRace.insert(tk.END, talent)


def afficher_competences():
    # Récupérer les compétences sélectionnées
    competences_selectionnees = [listCompetenceRace.get(i) for i in listCompetenceRace.curselection()]
    if len(competences_selectionnees) > 4:
        warning_label_comp.config(text="Veuillez sélectionner seulement 4 compétences !", fg="red")
    else:
        warning_label_comp.config(text="")
        message_competences = "Compétences sélectionnées avec bonus:\n"
        for comp in competences_selectionnees:
            message_competences += f"{comp} +5\n"
        result_label.config(text=result_label.cget("text") + "\n" + message_competences)

def designation_competence_race():
    listCompetenceRace.delete(0, tk.END)
    race = race_saisi.get()
    if race == "Humain":
        competence_race = ["calme", "charme", "commandement", "corp à corp (base)", "Evaluation",
                           "Langue (aux choix)", "Marchandage", "Projectiles (arc)", "Ragot",
                           "Savoir (guilde marchande)", "soin des animaux"]
    elif race == "Barbare":
        competence_race = ["corp à corp (base)", "Evaluation", "Intimidation", "Projectiles (arc)",
                           "Ragot", "savoir (guerre)", "soin des animaux", "dressage",
                           "projectile (improvisé)", "corp à corp (improvisé)"]

    for competence in competence_race:
        listCompetenceRace.insert(tk.END, competence)

## Crée la fenetre principale
root = tk.Tk()
root.title("Création de Personnage")

## Canvas et scrollbar
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

canvas = tk.Canvas(main_frame)
scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill = tk.Y)

scrollable_frame = tk.Frame(canvas)
scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0,0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)
canvas.pack(side=tk.LEFT, fill= tk.BOTH, expand=True)

## Saisie du nom
tk.Label(scrollable_frame, text="Nom du personnage :").pack()
nom_perso_saisi = tk.Entry(scrollable_frame)
nom_perso_saisi.pack()

## Choix de la race
tk.Label(scrollable_frame, text="Race :").pack()
race_saisi = tk.StringVar(value="Humain")
race_menu = ttk.Combobox(scrollable_frame, textvariable = race_saisi)
race_menu['values'] = ("Humain", "Barbare")
race_menu.pack()

## variables


## Répartition des caractéristiques
tk.Label(scrollable_frame, text = "Répartition des points de caractéristiques :").pack()

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

carac_frame = tk.Frame(scrollable_frame)
carac_frame.pack()

# Ajout des caractéristiques sous forme de ligne
for text, var in [("CC", cC_saisi), ("CT", cT_saisi), ("Force", force_saisi), 
                  ("Endurance", endu_saisi), ("Initiative", init_saisi), 
                  ("Agilité", agi_saisi), ("Dextérité", dex_saisi), 
                  ("Intelligence", intel_saisi), ("Force Mentale", force_ment_saisi), 
                  ("Sociabilité", socia_saisi)]:
    tk.Label(carac_frame, text=text + " :").pack(side=tk.LEFT)
    tk.Scale(carac_frame, from_=0, to=40, orient="vertical", variable=var,
             command=lambda x: points_carac_repartition()).pack(side=tk.LEFT)

points_restants = tk.StringVar(value = "Points restants : 120")
tk.Label(scrollable_frame, textvariable=points_restants).pack()

## Avertissement en cas de dépassement
warning_label = tk.Label(scrollable_frame, text="")
warning_label.pack()

# Boîte pour afficher et sélectionner les compétences
tk.Label(scrollable_frame, text="Sélectionnez 4 compétences :").pack()
listCompetenceRace = tk.Listbox(scrollable_frame, selectmode=tk.MULTIPLE)
listCompetenceRace.pack()
designation_competence_race()

# Avertissement pour la sélection
warning_label_comp = tk.Label(scrollable_frame, text="")
warning_label_comp.pack()

## Bouton pour calculer les statistiques

tk.Button(scrollable_frame, text="Afficher les détails", command=lambda: [calcule_caracs(), designation_talent_race()]).pack()

# Bouton pour afficher les compétences sélectionnées avec bonus
tk.Button(scrollable_frame, text="Afficher les compétences sélectionnées", command=afficher_competences).pack()

## Afficher les caracs
result_label = tk.Label(scrollable_frame, text = "")
result_label.pack()

listTalentRace = tk.Listbox(scrollable_frame)
listTalentRace.pack()


root.mainloop()