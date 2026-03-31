"""
Fichier: utilite_prot.py
Description: Fonctions utilitaires pour le projet d'épicerie de protéines
Auteur: James Bergeron
Date: 24-04-2026
"""

import pandas as pd
import json
import os


def lire_produits(chemin_fichier):
    """
    Lit un fichier CSV contenant les produits.

    Paramètre:
    chemin_fichier (str): chemin relatif vers le fichier CSV

    Retour:
    dict: dictionnaire des produits indexés par ID
    """
    try:
        df = pd.read_csv(chemin_fichier)
        produits = {}

        for _, row in df.iterrows():
            produits[row["id"]] = {
                "nom": row["nom"],
                "categorie": row["categorie"],
                "proteines": row["proteines_pr_100g"],
                "prix": row["prix"]
            }

        return produits

    except FileNotFoundError:
        print("Erreur: fichier produits introuvable.")
        return {}
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return {}


def lire_ventes(chemin_fichier):
    """
    Lit un fichier JSON contenant les ventes.

    Paramètre:
    chemin_fichier (str): chemin relatif vers le fichier JSON

    Retour:
    list: liste des ventes
    """
    try:
        with open(chemin_fichier, "r", encoding="utf-8") as f:
            return json.load(f)

    except FileNotFoundError:
        print("Erreur: fichier ventes introuvable.")
        return []
    except json.JSONDecodeError:
        print("Erreur: JSON invalide.")
        return []
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return []


def generer_rapport(produits, ventes, chemin_sortie):
    """
    Génère un rapport texte basé sur les ventes.

    Paramètres:
    produits (dict): dictionnaire des produits
    ventes (list): liste des ventes
    chemin_sortie (str): chemin relatif du fichier de sortie
    """
    try:
        total_revenu = 0
        lignes = []

        for vente in ventes:
            pid = vente["id_produit"]
            quantite = vente["quantite"]

            if pid in produits:
                produit = produits[pid]
                revenu = produit["prix"] * quantite
                proteines_total = produit["proteines"] * quantite

                total_revenu += revenu

                lignes.append(
                    f"{produit['nom']} - Qté: {quantite} - Revenu: {revenu:.2f}$ - Protéines: {proteines_total}g"
                )

        # Créer dossier si nécessaire
        os.makedirs(os.path.dirname(chemin_sortie), exist_ok=True)

        with open(chemin_sortie, "w", encoding="utf-8") as f:
            f.write("=== Rapport des ventes ===\n\n")
            for ligne in lignes:
                f.write(ligne + "\n")

            f.write(f"\nTotal revenu: {total_revenu:.2f}$")

    except Exception as e:
        print(f"Erreur lors de l'écriture du rapport: {e}")