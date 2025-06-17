import tkinter as tk
from tkinter import ttk
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as pdf_canvas
import random

root = tk.Tk()
root.title("Création de Personnage")

# --- Données de base
races = {
    "Humain": {
        "caracs": {"CC": 20, "CT": 20, "Force": 20, "Endurance": 20, "Initiative": 20,
                    "Agilité": 20, "Dextérité": 20, "Intelligence": 20, "Force Mentale": 20, "Sociabilité": 20, "Chance": 20},
        "talents": ["Ambidextre", "Rapide"],
        "competences": ["Athlétisme", "Discrétion", "Équitation", "Intuition", "Langage", "piscine", ]
    },
    "Barbare": {
        "caracs": {"CC": 30, "CT": 20, "Force": 25, "Endurance": 25, "Initiative": 20,
                    "Agilité": 20, "Dextérité": 20, "Intelligence": 0, "Force Mentale": 20, "Sociabilité": 20, "Chance": 20},
        "talents": ["Furie", "Résistance"],
        "competences": ["Intimidation", "Survie", "Escalade", "Endurance", "Tactique"]
    }
}

statuts = {
    "Citadin": {
        "equipement": ["Habit simple", "Petite bourse"],
        "talents": ["Marchandage", "Réseau"],
        "competences": ["Commerce", "Langage", "Discrétion", "Savoir local"]
    },
    "Courtisan": {
        "equipement": ["Tenue élégante", "Lettre de noblesse"],
        "talents": ["Éloquence", "Manipulation"],
        "competences": ["Étiquette", "Charme", "Langage", "Persuasion"]
    },
    "Guerrier": {
        "equipement": ["Armure légère", "Épée rouillée"],
        "talents": ["Combat", "Endurance"],
        "competences": ["Armes", "Parade", "Commandement", "Intimidation"]
    }
}

# --- Variables
nom_var = tk.StringVar()
race_var = tk.StringVar(value="Humain")
statut_var = tk.StringVar(value="Citadin")
talent_statut_var = tk.StringVar()
pnj_var = tk.BooleanVar(value=False)
caracs = {key: tk.IntVar(value=0) for key in races["Humain"]["caracs"]}
caracs["Chance"].set(0)  # Fixé à 0 côté interface, mais additionné avec 20 dans résumé
points_restants = tk.StringVar(value="Points restants : 120")
pv_var = tk.StringVar(value="PV : 0")
competence_race_vars = {}
competence_statut_vars = {}

race_var.trace_add("write", lambda *_, v=race_var: maj_race_related())
statut_var.trace_add("write", lambda *_, v=statut_var: maj_statut_related())


# --- Interface principale
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

# --- Colonne Gauche
left_frame = tk.Frame(main_frame)
left_frame.grid(row=0, column=0, sticky="nw")

tk.Label(left_frame, text="Nom").pack()
tk.Entry(left_frame, textvariable=nom_var).pack()

def generer_nom():
    prefixes = ["Al", "Bel", "Cor", "Dra", "El", "Fa", "Gal", "Har", "Is", "Jon", "Ka", "Li"]
    suffixes = ["dor", "wen", "rak", "thor", "mir", "lith", "nas", "grim", "vald", "eth"]
    nom_genere = random.choice(prefixes) + random.choice(suffixes)
    nom_var.set(nom_genere)

tk.Button(left_frame, text="Générer un nom", command=generer_nom).pack(pady=(0, 5))

tk.Checkbutton(left_frame, text="PNJ", variable=pnj_var, command=lambda: maj_pnj()).pack()

tk.Label(left_frame, text="Race").pack()
race_menu = ttk.Combobox(left_frame, textvariable=race_var, values=list(races.keys()), state="readonly")
race_menu.pack()

tk.Label(left_frame, text="Statut Social").pack()
statut_menu = ttk.Combobox(left_frame, textvariable=statut_var, values=list(statuts.keys()), state="readonly")
statut_menu.pack()

# --- Caractéristiques
carac_frame = tk.LabelFrame(left_frame, text="Caractéristiques (max 120 pts, max 60 par stat)")
carac_frame.pack(pady=5)
carac_widgets = []

for key, var in caracs.items():
    row = tk.Frame(carac_frame)
    tk.Label(row, text=key, width=15, anchor="w").pack(side="left")
    if key == "Chance":
        tk.Label(row, text="20").pack(side="left")
    else:
        spin = tk.Spinbox(row, from_=0, to=40, textvariable=var, width=5, command=lambda: maj_points())
        spin.pack(side="left")
        carac_widgets.append(spin)
    row.pack(anchor="w")

tk.Label(left_frame, textvariable=points_restants).pack()
tk.Label(left_frame, textvariable=pv_var).pack()

# --- Colonne Centre
center_frame = tk.Frame(main_frame)
center_frame.grid(row=0, column=1, padx=10, sticky="nw")

tk.Label(center_frame, text="Talents raciaux :").pack(anchor="w")
talents_race_label = tk.Label(center_frame, text="")
talents_race_label.pack(anchor="w")

tk.Label(center_frame, text="Choisir 4 compétences raciales :").pack(anchor="w")
competence_race_frame = tk.Frame(center_frame)
competence_race_frame.pack(anchor="w")

tk.Label(center_frame, text="Choisir un talent de statut :").pack(anchor="w")
talent_statut_menu = ttk.Combobox(center_frame, textvariable=talent_statut_var, state="readonly")
talent_statut_menu.pack(anchor="w")

tk.Label(center_frame, text="Choisir 3 compétences statut :").pack(anchor="w")
competence_statut_frame = tk.Frame(center_frame)
competence_statut_frame.pack(anchor="w")

# --- Résumé
summary_frame = tk.Frame(main_frame)
summary_frame.grid(row=0, column=2, sticky="nw")

tk.Label(summary_frame, text="Résumé du personnage", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 5))
summary_text = tk.Text(summary_frame, width=45, height=35, wrap="word", state="disabled")
summary_text.pack(fill="both", expand=True)

def exporter_pdf():
    if pnj_var.get():
        print("Pas de PDF pour un PNJ.")
        return
    texte = summary_text.get("1.0", "end").strip()
    nom = nom_var.get() or "SansNom"
    fichier = f"{nom}.pdf"
    c = pdf_canvas.Canvas(fichier, pagesize=A4)
    y = 800
    for line in texte.split("\n"):
        c.drawString(100, y, line)
        y -= 20
    c.save()
    print(f"PDF enregistré : {fichier}")

btn_pdf = tk.Button(summary_frame, text="Exporter en PDF", command=exporter_pdf)
btn_pdf.pack(pady=5)

# --- Fonctions de mise à jour
def maj_pnj():
    etat = not pnj_var.get()
    race_menu.config(state="readonly" if etat else "disabled")
    statut_menu.config(state="readonly" if etat else "disabled")
    talent_statut_menu.config(state="readonly" if etat else "disabled")
    for spin in carac_widgets:
        spin.config(state="normal" if etat else "disabled")
    for cb in competence_race_frame.winfo_children():
        cb.config(state="normal" if etat else "disabled")
    for cb in competence_statut_frame.winfo_children():
        cb.config(state="normal" if etat else "disabled")
    btn_pdf.config(state="normal" if not pnj_var.get() else "disabled")
    maj_resume()

def maj_points():
    total = sum(var.get() for key, var in caracs.items() if key != "Chance")
    over60 = any((var.get() + races[race_var.get()]["caracs"][key]) > 60 for key, var in caracs.items() if key != "Chance")
    if total > 120:
        points_restants.set("Erreur : plus de 120 points alloués")
    elif over60:
        points_restants.set("Erreur : une caractéristique dépasse 60")
    else:
        points_restants.set(f"Points restants : {120 - total}")
    maj_resume()

def limiter_choix_statut():
    count = sum(var.get() for var in competence_statut_vars.values())
    for comp, var in competence_statut_vars.items():
        if not var.get():
            var.set(0 if count >= 3 else var.get())
    maj_resume()

def limiter_choix_race():
    count = sum(var.get() for var in competence_race_vars.values())
    for comp, var in competence_race_vars.items():
        if not var.get():
            var.set(0 if count >= 4 else var.get())
    maj_resume()


def maj_race_related():
    race = races[race_var.get()]
    talents_race_label.config(text=", ".join(race["talents"]))
    maj_competences_race(race["competences"])
    maj_resume()

def maj_statut_related():
    statut = statuts[statut_var.get()]
    talent_statut_menu.config(values=statut["talents"])
    if statut["talents"]:
        talent_statut_var.set(statut["talents"][0])
    maj_competences_statut(statut["competences"])
    maj_resume()

def maj_competences_race(liste):
    for cb in competence_race_frame.winfo_children():
        cb.destroy()
    competence_race_vars.clear()
    for comp in liste:
        var = tk.IntVar()
        var.trace_add("write", lambda *_, v=var: limiter_choix_race())
        cb = tk.Checkbutton(competence_race_frame, text=comp, variable=var, command=limiter_choix_race)
        cb.pack(anchor="w")
        competence_race_vars[comp] = var
    limiter_choix_race()

def maj_competences_statut(liste):
    for cb in competence_statut_frame.winfo_children():
        cb.destroy()
    competence_statut_vars.clear()
    for comp in liste:
        var = tk.IntVar()
        var.trace_add("write", lambda *_, v=var: maj_resume())
        cb = tk.Checkbutton(competence_statut_frame, text=comp, variable=var, command=limiter_choix_statut)
        cb.pack(anchor="w")
        competence_statut_vars[comp] = var
    limiter_choix_statut()

def maj_resume():
    texte = f"Nom : {nom_var.get()}"
    if pnj_var.get():
        texte += " (PNJ)"
        texte += "\nRésumé simplifié pour PNJ."
    else:
        rdata = races[race_var.get()]
        sdata = statuts[statut_var.get()]
        # --- Calcul des PV
        force = races[race_var.get()]["caracs"]["Force"] + caracs["Force"].get()
        endurance = races[race_var.get()]["caracs"]["Endurance"] + caracs["Endurance"].get()
        fm = races[race_var.get()]["caracs"]["Force Mentale"] + caracs["Force Mentale"].get()

        dure_a_cuire = (
            "Dur à cuire" in races[race_var.get()]["talents"]
            or talent_statut_var.get() == "Dur à cuire"
        )

        mod_endurance = 3 if dure_a_cuire else 2

        pv = (force // 10 + fm // 10 + (endurance // 10) * mod_endurance) * 15
        pv_var.set(f"PV : {pv}")

        texte += f"\nRace : {race_var.get()}\nStatut : {statut_var.get()}\n\n"
        texte += "Caractéristiques totales :\n"
        for key in caracs:
            base = rdata["caracs"][key]
            mod = caracs[key].get() if key != "Chance" else 0
            total = base + mod
            texte += f" - {key} : {total}\n"
        texte += f"\nPoints de Vie (PV) : {pv}\n"
        texte += "\nTalents raciaux : " + ", ".join(rdata["talents"]) + "\n"
        texte += "Talent de statut : " + talent_statut_var.get() + "\n"
        texte += "\nCompétences avec bonus :\n"
        all_comps = set(list(competence_race_vars.keys()) + list(competence_statut_vars.keys()))
        for comp in all_comps:
            bonus = 0
            if competence_race_vars.get(comp, tk.IntVar()).get():
                bonus += 5
            if competence_statut_vars.get(comp, tk.IntVar()).get():
                bonus += 5
            if bonus > 0:
                texte += f" - {comp} (+{bonus})\n"
        texte += "\nÉquipement :\n - " + "\n - ".join(sdata["equipement"])
    summary_text.config(state="normal")
    summary_text.delete("1.0", "end")
    summary_text.insert("1.0", texte)
    summary_text.config(state="disabled")

# --- Observateurs
for var in list(caracs.values()) + [nom_var, race_var, statut_var, talent_statut_var, pnj_var]:
    var.trace_add("write", lambda *_, v=var: maj_resume())

# --- Initialisation
maj_race_related()
maj_statut_related()
maj_points()
maj_resume()
maj_pnj()
root.mainloop()
