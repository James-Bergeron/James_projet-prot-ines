# Mon projet

Mon projet est basé sur le concept de l'épicerie où le personnage doit ramasser des provisions d'une certaine catégorie d'aliments et suppléments avec un budget fixe à ne pas dépasser.


# But

Le but de l'épicerie est de ramasser 1275 grammes de protéines de différentes sources afin d'en avoir assez pour une semaine complète.

# Fonctionnement de chaque partie

- Main.py: Ce fichier contient le code qui permet de mettre en marche le programme de l'épicerie et de ramasser toutes les données pertinentes dans "utilite_prot.py" afin d'avoir la facture ou s'il n'y a pas assez de données pour créer la facture, le code va dire qu'il y a un manque de données.
  
- utilite_prot.py: Ce fichier contient le code qui rassemble les informations essentielles du fichier csv et du fichier json et il s'occupe de générer la facture avec les données ramassées.

- liste_prot1.csv: C'est le fichier excel transféré en csv qui contient toutes les données sur les aliments achetés, la quantité réelle, le nombre de grammes par portions de 100g pour chaque aliment, le prix des quantités requises, le prix des articles réels avec taxes incluses, etc...
  
- ventes_prot.json: C'est le fichier json qui contient l'id, c'est-à-dire, le numéro de l'aliment attribué à chacun et le nombre d'unité acheté pour chaque article.

- facture.txt: C'est le fichier texte est la sortie où la facture de l'épicerie va être générée, à la fin de l'exécution du code.

- obligations.txt: C'est le fichier qui présente des contraintes pour l'épicerie de protéines afin d'avoir assez de de grammes de protéines pour la semaine.