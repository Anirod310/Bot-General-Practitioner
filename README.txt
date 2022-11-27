Titre :  Médecin généraliste

Description : Le programme pose une série de questions, et va dans sa base de données
pour rechercher des symptomes correspondants aux réponses de l'utilisateur. Si lors des
questions, l'utilisateur décrit des symptomes inconnus, on envoie le rapport au médecin
pour qu'il ajoute les symptomes et éventuelles maladies à la base de données.

outils : python basique(tableaux, if/else etc), fichiers csv

plan : 	1-Création base de données avec quelques maladies et quelques symptomes associés
(en fichier CSV)
	2-Création fonction 1:
		-suites de questions
	3-Création fonction 2:
		-conversion input des utilisateurs en liste
	4-Création fonction 3:
		-parcours de la liste et recherche de mots correspondants a des symptomes
		-Si pas de symptomes trouvés, envoie de l'input au médecin
		-correspondance des symptomes avec une maladie, pour cela:
		-ajout d'un "point" de correspondance a chaque couple symptome/maladie
	5-Création fonction 4: 
		-donner une maladie très probable, puis la deuxième plus probable
		-donner une liste de tests(ordonnances) à faire pour confirmer ou non
		la présence de la maladie