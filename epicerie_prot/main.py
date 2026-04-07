"""
Auteur: James Bergeron
Nom du projet: Épicerie Prot
Date: 2026/03/17
"""

import os
from epicerie_prot.utilite_prot import lire_liste_prot1, lire_ventes_prot, generer_facture

"""
Fonction principale du projet d'épicerie de protéines. Elle lit les données des produits et des ventes, puis génère une facture.
"""
def main():    
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    fichier_produits = os.path.join(BASE_DIR, "infos_epicerie", "liste_prot1.csv")
    fichier_ventes = os.path.join(BASE_DIR, "infos_epicerie", "ventes_prot.json")
    chemin_sortie = os.path.join(BASE_DIR, "infos_epicerie", "facture_prot.txt")

    produits = lire_liste_prot1(fichier_produits)
    ventes = lire_ventes_prot(fichier_ventes)

    if produits and ventes:
        generer_facture(produits, ventes, chemin_sortie)
        print("Facture générée avec succès !")
    else:
        print("Erreur: données manquantes.")


if __name__ == "__main__":
    main()
    