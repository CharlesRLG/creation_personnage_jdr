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
    statut_social = statut_social_saisi.get()
    total_reparti = int(cC_saisi.get()) + int(cT_saisi.get()) + int(force_saisi.get()) + \
                    int(endu_saisi.get()) + int(init_saisi.get()) + int(agi_saisi.get()) + \
                    int(dex_saisi.get()) + int(intel_saisi.get()) + int(force_ment_saisi.get()) + \
                    int(socia_saisi.get())
    
    if total_reparti > 120:
        result_label.config(text="La répartition des points est incorrecte !")
    else:
        caracs = {
            "CC": int(cC_saisi.get()),
            "CT": int(cT_saisi.get()),
            "Force": int(force_saisi.get()),
            "Endurance": int(endu_saisi.get()),
            "Initiative": int(init_saisi.get()),
            "Agilité": int(agi_saisi.get()),
            "Dextérité": int(dex_saisi.get()),
            "Intelligence": int(intel_saisi.get()),
            "Force Mentale": int(force_ment_saisi.get()),
            "Sociabilité": int(socia_saisi.get())
        }

        bonuses = {
            "Humain": {"CC": 20, "CT": 20, "Force": 20, "Endurance": 20, "Initiative": 20,
                        "Agilité": 20, "Dextérité": 20, "Intelligence": 20, "Force Mentale": 20, "Sociabilité": 20},
            "Barbare": {"CC": 30, "CT": 20, "Force": 25, "Endurance": 25, "Initiative": 20,
                        "Agilité": 20, "Dextérité": 20, "Intelligence": 0, "Force Mentale": 20, "Sociabilité": 20}
        }

        # Appliquer les bonus
        message = f"Nom : {nom_perso_saisi.get()}\nRace : {race}\n\nCaractéristiques avec bonus :\n"
        for key, value in caracs.items():
            bonus = bonuses[race].get(key, 0)
            final_value = value + bonus
            message += f"{key}: {final_value}\n"

            # Vérification des limites de caractéristiques
            if final_value < 10 or final_value > 60:
                result_label.config(text=f"Erreur : la caractéristique {key} ({final_value}) est hors limites !")
                return

        result_label.config(text=message)
    
        # Validation pour chaque caractéristique
        for key, value in caracs.items():
            final_value = value + (bonuses["Humain"] if race == "Humain" else bonuses["Barbare"].get(key, 20))
            if final_value < 10 or final_value > 60:
                result_label.config(text=f"Erreur : la caractéristique {key} ({final_value}) est hors limites ! Doit être compris entre 10 et 60")
                return

        # Génération du message final
        message = f"Nom : {nom_perso_saisi.get()} \n Statut Social : {statut_social} \n Race : {race}\n"
        for key, value in caracs.items():
            bonus = bonuses["Humain"] if race == "Humain" else bonuses["Barbare"].get(key, 20)
            message += f"{key} : {value + bonus}\n"   

        result_label.config(text=message)
    
def designation_talent_race():
    listTalentRace.delete(0, tk.END)
    race = race_saisi.get()
    if race == "Humain":
        talent_race = ["Perspicace", "Destinée", "3 compétences aléatoires"]
    elif race == "Barbare":
        talent_race = ["Dure à cuire", "Destinée", "Ambidextre", "Orientation"]

    for talent in talent_race:
        listTalentRace.insert(tk.END, talent)

def designation_talent_statut():
    listTalentStatut.delete(0, tk.END)
    statut_social = statut_social_saisi.get()
    if statut_social == "Citadin":
        talent_statut_social = ["Lire/Ecrire", "Sociable", "faire la manche", "négociateur", "baratin"]
    elif statut_social == "Courtisan":
        talent_statut_social = ["Lire/Ecrire", "savoir vivre (noble)", "discret", "sociable", "résistance (maladie)"]
    elif statut_social == "Guerrier":
        talent_statut_social = ["Maitrise des dés", "guerrier-nés", "costaud", "déterminé", "infatigable"]

    for talentStatut in talent_statut_social:
        listTalentStatut.insert(tk.END, talentStatut)

def afficher_competences_double_clic(event):
    competences_selectionnees = [listCompetenceRace.get(i) for i in listCompetenceRace.curselection()]
    if len(competences_selectionnees) > 4:
        warning_label_comp.config(text="Veuillez sélectionner seulement 4 compétences ! (Double clic pour sélectionner)", fg="red")
    else:
        warning_label_comp.config(text="")
        message_competences = "Compétences raciales sélectionnées avec bonus:\n"
        for comp in competences_selectionnees:
            message_competences += f"{comp} +5\n"
        # Réinitialiser l'affichage des compétences avant d'ajouter les nouvelles
        result_text = result_label.cget("text").split("\nCompétences sélectionnées avec bonus:\n")[0]
        result_label.config(text=result_text + "\n" + message_competences)


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

def afficher_competences_statut_double_clic(event):
    competences_statut_selectionnees = [listCompetenceStatut.get(i) for i in listCompetenceStatut.curselection()]
    if len(competences_statut_selectionnees) > 3:
        warning_label_comp_statut.config(text="Veuillez sélectionner seulement 3 compétences ! (Double clic pour sélectionner)", fg="red")
    else:
        warning_label_comp_statut.config(text="")
        
        # Récupérer le texte actuel affiché
        texte_actuel = result_label.cget("text")
        
        # Si les compétences de statut sont déjà affichées, les supprimer
        if "\nCompétences de statut avec bonus:\n" in texte_actuel:
            texte_actuel = texte_actuel.split("\nCompétences de statut avec bonus:\n")[0]
        
        # Ajouter les nouvelles compétences de statut sélectionnées
        message_competences_statut = "\nCompétences de statut avec bonus:\n"
        for comp_statut in competences_statut_selectionnees:
            message_competences_statut += f"{comp_statut} +5\n"

        # Réinitialiser l'affichage des compétences avant d'ajouter les nouvelles
        
        result_label.config(text=texte_actuel + message_competences_statut)


def designation_competence_statut():
    listCompetenceStatut.delete(0, tk.END)
    statut_social = statut_social_saisi.get()
    if statut_social == "Citadin":
        competence_statut = ["Art (aux choix)","charme","marchandage","métier (aux choix)","résistance à l'alcool","esquive","escalade","ragot","pari"]
    elif statut_social == "Courtisan":
        competence_statut = ["calme", "art (aux choix)", "discrétion urbaine", "évaluation","corp à corp (base)", "dressage (chien)", "guérison", "savoir (politique)", "esquive", "chevaucher (chevale)"]
    elif statut_social == "Guerrier":
        competence_statut = ["corps à corps (base)", "esquive", "chevaucher (cheval)", "parie", "résistance", "intuition", "métier (aux choix)", "commandement", "intimidation", "athlétisme"]

    for competence_soc in competence_statut:
        listCompetenceStatut.insert(tk.END, competence_soc)

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
race_menu = ttk.Combobox(scrollable_frame, textvariable=race_saisi)
race_menu.bind("<<ComboboxSelected>>", lambda e: [designation_competence_race(), designation_talent_race()])
race_menu['values'] = ("Humain", "Barbare")
race_menu.pack()

# Choix du statut social
tk.Label(scrollable_frame, text="Statut Social :").pack()
statut_social_saisi = tk.StringVar(value="Citadin")
statut_menu = ttk.Combobox(scrollable_frame, textvariable=statut_social_saisi)
statut_menu.bind("<<ComboboxSelected>>", lambda e: [designation_talent_statut(), designation_competence_statut()])
statut_menu['values'] = ("Citadin", "Courtisan", "Guerrier")
statut_menu.pack()

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

# Boîte pour afficher et sélectionner les compétences socials
tk.Label(scrollable_frame, text="Sélectionnez 3 compétences :").pack()
listCompetenceStatut = tk.Listbox(scrollable_frame, selectmode=tk.MULTIPLE)
listCompetenceStatut.pack()
designation_competence_statut()

# Avertissement pour la sélection
warning_label_comp = tk.Label(scrollable_frame, text="")
warning_label_comp.pack()

# Avertissement pour la sélection
warning_label_comp_statut = tk.Label(scrollable_frame, text="")
warning_label_comp_statut.pack()

## Bouton pour calculer les statistiques

tk.Button(scrollable_frame, text="Afficher les caractéristiques", command=lambda: [calcule_caracs(), designation_talent_race(), designation_talent_statut]).pack()

#  liaison d'événement compétence
listCompetenceRace.bind("<Double-Button-1>", afficher_competences_double_clic)

#  liaison d'événement compétence statut
listCompetenceStatut.bind("<Double-Button-1>", afficher_competences_statut_double_clic)

## Afficher les caracs
tk.Label(scrollable_frame, text = "Caractéristiques :\n").pack()
result_label = tk.Label(scrollable_frame, text = "")
result_label.pack()

tk.Label(scrollable_frame, text = "Talents Race :\n").pack()
listTalentRace = tk.Listbox(scrollable_frame)
listTalentRace.pack()

tk.Label(scrollable_frame, text = "Talents Statut Social :\n").pack()
listTalentStatut = tk.Listbox(scrollable_frame)
listTalentStatut.pack()

root.mainloop()