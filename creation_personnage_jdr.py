import tkinter as tk
from tkinter import ttk
import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas as pdf_canvas

root = tk.Tk()
root.title("Création de Personnage")
frame = tk.Frame(root)
frame.pack()

# --- Données de base
races = {
    "Humain": {"CC": 20, "CT": 20, "Force": 20, "Endurance": 20, "Initiative": 20,
               "Agilité": 20, "Dextérité": 20, "Intelligence": 20, "Force Mentale": 20, "Sociabilité": 20},
    "Barbare": {"CC": 30, "CT": 20, "Force": 25, "Endurance": 25, "Initiative": 20,
                "Agilité": 20, "Dextérité": 20, "Intelligence": 0, "Force Mentale": 20, "Sociabilité": 20}
}

# --- Variables
nom_var = tk.StringVar()
race_var = tk.StringVar(value="Humain")
statut_var = tk.StringVar(value="Citadin")
caracs = {key: tk.IntVar(value=0) for key in races["Humain"].keys()}
points_restants = tk.StringVar(value="Points restants : 120")
result_text = tk.StringVar()

# --- Fonctions principales
def maj_points():
    total = sum(var.get() for var in caracs.values())
    points_restants.set(f"Points restants : {120 - total}")
    if total > 120:
        result_text.set("Erreur : plus de 120 points alloués.")
    else:
        result_text.set("")

def calculer_caracs():
    total = sum(var.get() for var in caracs.values())
    if total > 120:
        result_text.set("Erreur : plus de 120 points alloués.")
        return

    bonus = races.get(race_var.get(), {})
    texte = f"Nom : {nom_var.get()}\nRace : {race_var.get()}\nStatut : {statut_var.get()}\n"
    for key, var in caracs.items():
        val = var.get() + bonus.get(key, 0)
        if not (10 <= val <= 60):
            result_text.set(f"Erreur : {key} ({val}) hors limites (10-60).")
            return
        texte += f"{key} : {val}\n"
    result_text.set(texte)

def sauvegarder_pdf():
    nom = nom_var.get() or "SansNom"
    fichier = f"{nom}.pdf"
    c = pdf_canvas.Canvas(fichier, pagesize=A4)
    c.drawString(100, 800, "Fiche de Personnage")
    y = 780
    for line in result_text.get().split("\n"):
        c.drawString(100, y, line)
        y -= 20
    c.save()
    print(f"PDF enregistré : {fichier}")

# --- UI
tk.Label(frame, text="Nom du personnage").pack()
tk.Entry(frame, textvariable=nom_var).pack()

tk.Label(frame, text="Race").pack()
ttk.Combobox(frame, textvariable=race_var, values=list(races.keys())).pack()

tk.Label(frame, text="Statut social").pack()
ttk.Combobox(frame, textvariable=statut_var, values=["Citadin", "Courtisan", "Guerrier"]).pack()

tk.Label(frame, text="Caractéristiques (total 120 max)").pack()
carac_frame = tk.Frame(frame)
carac_frame.pack()

for key, var in caracs.items():
    ligne = tk.Frame(carac_frame)
    ligne.pack(anchor="w", padx=5, pady=2)
    tk.Label(ligne, text=key, width=15).pack(side=tk.LEFT)
    spin = tk.Spinbox(ligne, from_=0, to=40, textvariable=var, width=5, command=maj_points)
    spin.pack(side=tk.LEFT)
    spin.bind("<KeyRelease>", lambda event: maj_points())

tk.Label(frame, textvariable=points_restants).pack(pady=5)
tk.Button(frame, text="Calculer", command=calculer_caracs).pack()
tk.Button(frame, text="Sauvegarder PDF", command=sauvegarder_pdf).pack(pady=5)
tk.Label(frame, textvariable=result_text, justify="left").pack(pady=10)

root.mainloop()
