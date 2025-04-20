import tkinter as tk
from tkinter import ttk
import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as pdf_canvas

PA_citadin = random.randint(1,16)
PC_citadin = random.randint(1,10)
PO_courtisan = random.randint(1,10)
PA_courtisan = random.randint(1,15)
PC_courtisan = random.randint(1,12)
PA_guerrier = random.randint(1,8)
PC_guerrier = random.randint(1,10)

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

def afficher_talent_statut_social(event):
    # Récupérer les compétences sélectionnées dans le Listbox
    talent_selectionnees = [listTalentStatut.get(i) for i in listTalentStatut.curselection()]
    
    # Vérifier si l'utilisateur dépasse la limite de 1 talent social sélectionné
    if len(talent_selectionnees) > 1:
        warning_label_tal.config(text="Veuillez sélectionner seulement 1 talent social !", fg="red")
    else:
        warning_label_tal.config(text="")
        
        # Reconstruire uniquement l'affichage nécessaire
        message_talent = "Talent social sélectionnées :\n"
        for tal in talent_selectionnees:
            message_talent += f"{tal}\n"
        
        # Mettre à jour le label avec seulement le message des compétences
        texte_base = result_label.cget("text").split("\nTalent social sélectionnées :\n")[0]
        result_label.config(text=f"{texte_base}\n{message_talent}")

def afficher_competences_double_clic(event):
    # Récupérer les compétences sélectionnées dans le Listbox
    competences_selectionnees = [listCompetenceRace.get(i) for i in listCompetenceRace.curselection()]
    
    # Vérifier si l'utilisateur dépasse la limite de 4 compétences sélectionnées
    if len(competences_selectionnees) > 4:
        warning_label_comp.config(text="Veuillez sélectionner seulement 4 compétences !", fg="red")
    else:
        warning_label_comp.config(text="")
        
        # Reconstruire uniquement l'affichage nécessaire
        message_competences = "Compétences raciales sélectionnées avec bonus:\n"
        for comp in competences_selectionnees:
            message_competences += f"{comp} +5\n"
        
        # Mettre à jour le label avec seulement le message des compétences
        texte_base = result_label.cget("text").split("\nCompétences raciales sélectionnées avec bonus:\n")[0]
        result_label.config(text=f"{texte_base}\n{message_competences}")



def designation_competence_race():
    # Vider le contenu du Listbox avant d'ajouter les nouvelles compétences
    listCompetenceRace.delete(0, tk.END)
    
    race = race_saisi.get()  # Récupérer la race sélectionnée
    if race == "Humain":
        competence_race = ["calme", "charme", "commandement", "corp à corp (base)", "Evaluation",
                           "Langue (aux choix)", "Marchandage", "Projectiles (arc)", "Ragot",
                           "Savoir (guilde marchande)", "soin des animaux"]
    elif race == "Barbare":
        competence_race = ["corp à corp (base)", "Evaluation", "Intimidation", "Projectiles (arc)",
                           "Ragot", "savoir (guerre)", "soin des animaux", "dressage",
                           "projectile (improvisé)", "corp à corp (improvisé)"]

    # Ajouter les nouvelles compétences dans le Listbox
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

def designation_equipement_statut():
    listEquipementStatut.delete(0, tk.END)
    statut_social = statut_social_saisi.get()
    if statut_social == "Citadin":
        equipement_statut = ["Cape","Vêtements de base","Dague","chapeau","1 ration","bourse :", f"{PA_citadin} PA", f"{PC_citadin} PC", "besace"]
    elif statut_social == "Courtisan":
        equipement_statut = ["Costume luxueux","Dague","Bourse de luxe :","une pince à épiler","un cure oreilles","un peigne",f"{PO_courtisan} PO",f"{PA_courtisan} PA",f"{PC_courtisan} PC"]
    elif statut_social == "Guerrier":
        equipement_statut = ["Vêtements délabré","Arme 1 main + bouclier"," ou arme 2 mains","dague",f"{PA_guerrier} PA",f"{PC_guerrier} PC"]

    for equipement_soc in equipement_statut:
        listEquipementStatut.insert(tk.END, equipement_soc)
        
## \\\\\\\\\\\\\\\\\\\\\ sauvegarde du perso /////////////////////

def sauvegarder_pdf():
    nom_personnage = nom_perso_saisi.get()
    race_personnage = race_saisi.get()
    statut_social_personnage = statut_social_saisi.get()
    texte_caracteristiques = result_label.cget("text")  # Récupère le texte des caractéristiques affichées

    # Utiliser un nom par défaut si le champ du nom est vide
    if not nom_personnage.strip():
        nom_personnage = "Personnage_sans_nom"

    # Nettoyer le nom pour éviter les caractères invalides dans les noms de fichiers
    nom_personnage = "".join(c if c.isalnum() or c in ("_", "-") else "_" for c in nom_personnage)

    # Chemin et nom du fichier PDF
    fichier_pdf = f"{nom_personnage}_fiche_personnage.pdf"
    
    # Création du PDF
    c = pdf_canvas.Canvas(fichier_pdf, pagesize=A4)
    c.setFont("Helvetica", 12)
    
    # Titre
    c.drawString(100, 800, f"Fiche de Personnage : {nom_personnage}")
    c.drawString(100, 780, f"Race : {race_personnage}")
    c.drawString(100, 760, f"Statut Social : {statut_social_personnage}")
    
    # Ajout des caractéristiques
    c.drawString(100, 740, "Caractéristiques :")
    lignes = texte_caracteristiques.split("\n")
    hauteur = 720
    for ligne in lignes:
        c.drawString(100, hauteur, ligne)
        hauteur -= 20
    
    # Finalisation et sauvegarde
    c.save()
    print(f"PDF sauvegardé sous le nom {fichier_pdf}")


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
statut_menu.bind("<<ComboboxSelected>>", lambda e: [designation_talent_statut(), designation_competence_statut(), designation_equipement_statut()])
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

# Boîte pour afficher et séectionner le statut social
tk.Label(scrollable_frame, text="Sélectionnez 1 Talent social :").pack()
listTalentStatut = tk.Listbox(scrollable_frame, selectmode=tk.MULTIPLE)
listTalentStatut.pack()
designation_talent_statut()

# Avertissement pour la sélection
warning_label_comp = tk.Label(scrollable_frame, text="")
warning_label_comp.pack()

# Avertissement pour la sélection
warning_label_comp_statut = tk.Label(scrollable_frame, text="")
warning_label_comp_statut.pack()

# Avertissement pour la selection talent statut
warning_label_tal = tk.Label(scrollable_frame, text="")
warning_label_tal.pack()

## Bouton pour calculer les statistiques

tk.Button(scrollable_frame, text="Afficher les caractéristiques", command=lambda: [calcule_caracs(), designation_talent_race()]).pack()

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

## Afficher les equipements
tk.Label(scrollable_frame, text = "Equipement statut social : \n").pack()
listEquipementStatut = tk.Listbox(scrollable_frame)
listEquipementStatut.pack()

# liason d'événement statut social
listTalentStatut.bind("<Double-Button-1>", afficher_talent_statut_social)

# Sauvegrder un pdf du perso
tk.Button(scrollable_frame, text="Sauvegarder en PDF", command=sauvegarder_pdf).pack()


root.mainloop()