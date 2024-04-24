# Bienvenue sur le readme du projet Dragon Ball Draft Clash


## Prérequis :

- Xamp lancer la base de données (port 3306)
- Créer une Base : sae_api

## Lancer le Projet :

- Ouvrir dans un cmd le dossier ./server
- Executer la commande : flask run --debug
- Le port doit être 5000 sinon il faudra changer l'url dans ./client/app.py
- base_url = "http://127.0.0.1:5000/api/" (mettre le nouveau port)


- Ouvrir dans un cm le dossier ./client
- Executer la commande : flask run --port=8080 --debug


## Acceder au site : 

- Aller sur l'url "http://127.0.0.1:8080"


# Fonctionnement du site :

- Vous arrivez sur l'index du site :
- Vous avez 3 boutons :
- Jouer (si vous n'etes pas connectés : ouvre la page de connexion)
- Menu (ouvre le menu principal du jeu)
- Icone de profil (si vous n'etes pas connectés rediriger vers la page de connexion sinon vers le profil)

### Une fois connecté ou Inscrit

- Quand vous cliquez sur le bouton jouer :
- 3 modes de jeux s'offrent à vous
- Tutoriel
- Campagne
- Custom

#### Tutoriel
- Un diaporama d'images montre les differentes intéractions durant les combats

#### Campagne
- 4 niveaux actuellement s'offrent à vous pour jouer contre une IA

#### Custom
- Plusieurs champs à sélectionner pour créer vos propres combats


# L'api

Ce projet vient avec sa propre API faite Main possédant plusieurs Routes visibles dans le fichier ./server/app.py

Les Routes sont : 

- http://127.0.0.1:5000/api/users/
- http://127.0.0.1:5000/api/userInfos/X, où X est un id d'utilis
----
- http://127.0.0.1:5000/api/characters
- http://127.0.0.1:5000/api/characters/name, où name est le nom du personnage
(Vous pouvez remplacer name par un Id)
----
- http://127.0.0.1:5000/api/techniques
- http://127.0.0.1:5000/api/techniques/name,où name est le nom d'une technique
(Vous pouvez remplacer name par un Id)
----
- http://127.0.0.1:5000/api/stages/
- http://127.0.0.1:5000/api/stages/name,où name est le nom d'un terrain
----
- http://127.0.0.1:5000/api/TOB/
- http://127.0.0.1:5000/api/TOB/id,où id est l'ID d'un personnage
----
- http://127.0.0.1:5000/api/QuestStages/






