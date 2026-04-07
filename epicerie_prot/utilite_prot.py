"""
Fichier: utilite_prot.py
Description: Fonctions utilitaires pour le projet d'épicerie de protéines
Auteur: James Bergeron
Date: 24-03-2026
"""

import pandas as pd
import json
import os


def lire_liste_prot1(chemin_fichier):
    """
    Lit un fichier CSV contenant les produits.

    Paramètre:
    chemin_fichier (str): chemin relatif vers le fichier CSV

    Retour:
    dict: dictionnaire des produits indexés par ID
    """
    try:
        df = pd.read_csv(chemin_fichier, sep=";", decimal=",")
        produits = {}

        for _, row in df.iterrows():
            produits[int(row["ID"])] = {
                "Nom de protéines": row["Nom de protéines"],
                "Nb de grammes en moyenne de prot pour 100g de l'aliment": row["Nb de grammes en moyenne de prot pour 100g de l'aliment"],
                "Qté prot par semaine": row["Qté prot par semaine"],
                "Prix des articles avec taxes en unité": row["Prix des articles avec taxes en unité"]
            }
        
        return produits
    
    except FileNotFoundError:
        print("Erreur: fichier produits introuvable.")
        return {}
    except Exception as e:
        print(f"Erreur inattendue: {e}")
        return {}


def lire_ventes_prot(chemin_fichier):
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


def generer_facture(produits, ventes, infos_sortie):
    """
    Génère un fichier de facture basé sur les ventes.

    Paramètres:
    produits (dict): dictionnaire des produits
    ventes (list): liste des ventes
    chemin_sortie (str): chemin relatif du fichier de sortie
    """
    try:
        total_revenu = 0
        total_proteines = 0
        lignes = []

        for vente in ventes:
            pid = int(vente["id_produit"])
            qte_article = int(vente["qte_article"])

            if pid in produits:
                produit = produits[pid]
                revenu = float(produit["Prix des articles avec taxes en unité"]) * qte_article
                proteines_total = float(produit["Qté prot par semaine"]) * qte_article

                total_revenu += revenu
                total_proteines += proteines_total

                lignes.append(
                    f"{produit['Nom de protéines']} - Qté: {qte_article} - Revenu: {revenu:.2f}$ - Protéines par semaine: {proteines_total}g"
                )

        # Créer dossier si nécessaire
        os.makedirs(os.path.dirname(infos_sortie), exist_ok=True)

        with open(infos_sortie, "w", encoding="utf-8") as f:
            f.write("=== Facture d'épicerie de protéines ===\n\n")
            for ligne in lignes:
                f.write(ligne + "\n")

            f.write(f"\nTotal revenu: {total_revenu:.2f}$\n")
            f.write(f"Total protéines: {total_proteines:.2f} g\n\n")

            f.write("Budget de 190$ dépassé!" if total_revenu > 190 else "Budget de 190$ respecté!")
            f.write("\nProtéines totales inférieures à 2000g!" if total_proteines < 2000 else "Protéines totales respectées!")
            f.write("\n\nMerci d'avoir utilisé notre service d'épicerie de protéines !")

    except Exception as e:
        print(f"Erreur lors de l'écriture du rapport: {e}")