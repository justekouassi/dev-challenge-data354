# Dev Challenge - Software Engineer 2023 - data354

## Objectif

Construire une plateforme web permettant à différents utilisateurs de consulter les données de ces capteurs.

## Fonctionnalités

1. Authentification (inscription, connexion, déconnexion)
2. Une fois connecté, l'utilisateur peut spécifier la période de son choix et les capteurs dont il veut observer les données. Des visuels seront alors générés présentant les différents indicateurs de la qualité de l'air.

## Pages

|Pages|Description|Entrées|Sorties|
|:-|:-|:-|:-|
|Inscription|Permet l'inscription d'un utilisateur|- email <br>- mot de passe|Page de connexion|
|Connexion|Aide un utilisateur à se connecter à la plateforme|- email <br>- mot de passe|Page d'accueil|
|Accueil|Permettre aux utilisateurs d'effectuer des opérations de lecture sur les données des capteurs|- horodatage de début <br>- horodatage de fin<br> - capteur (188 ou 189)|Graphiques présentant les valeurs des indicateurs (CO, O3, etc.) de la qualité de l'air sur une certaine période|

- Les pages d'inscription et de connexion sont accessibles à tous 
- La page d'accueil est accessible aux utilisateurs connectés

## Technologies et outils

- Développement web
	- Backend : Flask (Python)
	- Frontend : Bootstrap (HTML/CSS/JavaScript)
	- Graphique : plotly
	- SGBD : SQLite
	- Tests : unittest
	- Architecture : MVC

- Machine Learning
	- Langage : Python
	- Calcul numérique : Numpy
	- Analyse de données : Pandas
	- Visualisation : matplotlib, seaborn, plotly
	- Modélisation : Scikit Learn

- Hébergement : pythonanywhere

## Ressources

- URL API : https://airqino-api.magentalab.it/
- Site d'inspiration : https://map.airqino.it/
- Projet : AQ54
- Stations : 188 et 189
