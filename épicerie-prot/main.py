"""
Auteur: James Bergeron
Nom du projet: Épicerie Prot
Date: 2026/04/17
"""

import os
from utilite_prot import lire_liste_prot1, lire_ventes-prot, generer_facture


def main():
    """
    Fonction principale du programme.
    """
    base_path = os.path.dirname(__file__)

    chemin_produits = os.path.join(base_path, "infos-épicerie", "liste_prot1.csv")
    chemin_ventes = os.path.join(base_path, "infos-épicerie", "ventes-prot.json")
    chemin_sortie = os.path.join(base_path, "infos_sortie", "facture.txt")

    produits = lire_liste_prot1(chemin_produits)
    ventes = lire_ventes-prot(chemin_ventes)

    if produits and ventes:
        generer_facture(produits, ventes, chemin_sortie)
        print("Facture générée avec succès !")
    else:
        print("Erreur: données manquantes.")


if __name__ == "__main__":
    main()