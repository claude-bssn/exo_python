# Python practice 
# [D33] Python - Initiation à la programmation réseau et sécurité

This repo is based on the requirements of the python evaluation
## installation 

Dans le but du cours d'initiation à la programmation réseau et de sécurité, nous souhaitons générer une liste de paquets pour un exercice de sécurité réseau.

Il est important de souligner que la collecte et l'exploitation de données réseau doivent être effectuées dans le respect de la législation et de l'éthique en matière de confidentialité et de sécurité des données.

Manipuler des données sensibles ou privées sans consentement approprié est illégal et contraire aux principes éthiques.

Il est recommandé d'utiliser des ensembles de données synthétiques ou anonymisées pour les exercices pratiques afin de préserver la confidentialité des données réelles et de respecter les lois sur la protection des données.

Pour des fins d'exercice, nous pouvons utiliser des bibliothèques Python pour générer des données aléatoires, telles que Faker.

Exemple qui utilise Faker pour générer des informations aléatoires sur les paquets réseau :
```
from faker import Faker

  fake = Faker()

  # Génération d'un paquet réseau aléatoire
  def generate_packet():
      packet = {
          "ip_address": fake.ipv4(),
          "mac_address": fake.mac_address(),
          "computer_name": fake.hostname(),
          "os": fake.user_agent(),
          "website": fake.url(),
          # Ajoutez d'autres informations du paquet ici
      }
      return packet

  # Génération d'une liste de paquets
  packets = [generate_packet() for _ in range(10)]

  # Affichage des paquets
  for packet in packets:
      print(packet)
```

Ce code utilise la bibliothèque Faker pour générer des informations aléatoires sur les paquets réseau.

La fonction generate_packet() crée un dictionnaire représentant un paquet avec des informations telles que l'adresse IP, l'adresse MAC, le nom de l'ordinateur, le système d'exploitation, le site web consulté, etc.

Ensuite, une liste de paquets est générée en appelant cette fonction plusieurs fois. Les paquets sont ensuite affichés à l'écran.

Ne pas oublier pas que l'utilisation de données synthétiques est recommandée pour les exercices pratiques afin de respecter les règles de confidentialité et de sécurité des données.

Pour installer la bibliothèque Faker, nous pouvons utiliser l'outil de gestion de packages Python appelé pip.

Les étapes à suivre :

Ouvrir une fenêtre de terminal ou de ligne de commande.

S'assurer d'avoir pip installé sur le système en exécutant la commande suivante :

```pip --version```

Si pip est déjà installé, nous verrons la version de pip affichée. Sinon, il va falloir installer pip en suivant les instructions appropriées pour votre système d'exploitation.

Une fois que vous avez pip installé, nous pouvons installer la bibliothèque Faker en exécutant la commande suivante :

```pip install faker```

Cela téléchargera et installera la bibliothèque Faker ainsi que ses dépendances.

Une fois l'installation terminée, nous pouvons utiliser Faker dans notre code Python en important la bibliothèque. Par exemple, nous pouvons utiliser from faker import Faker pour importer la bibliothèque, puis créer une instance de la classe Faker pour générer des données aléatoires.
Ne pas oublier d'exécuter ces commandes dans l'environnement Python approprié, tel que l'environnement virtuel ou le répertoire de projet souhaité.

## Traitement et analyse de données simulées
Description de l'exercice :

Vous disposez d'un ensemble de données simulées générées avec la bibliothèque Faker. Ces données représentent des informations telles que des adresses IP, des adresses MAC, des noms d'ordinateurs, des systèmes d'exploitation, des sites web consultés, etc. Votre tâche est de manipuler et d'analyser ces données en utilisant les concepts et les instructions vus précédemment.

Instructions :

 1. Importez la bibliothèque Faker et générez un ensemble de données simulées comprenant au moins 100 enregistrements.
 2. Affichez les premières lignes des données pour vous familiariser avec leur structure.
 3. Effectuez un filtrage des données en fonction de critères spécifiques. Par exemple, filtrez les adresses IP avec un masque de sous-réseau particulier ou filtrez les transactions avec un montant supérieur à une valeur donnée.
 4. Triez les données en fonction d'attributs spécifiques. Par exemple, triez les adresses IP par ordre croissant ou décroissant, ou triez les noms d'utilisateurs par ordre alphabétique.
 5. Calculez des statistiques à partir des données. Par exemple, calculez la moyenne des montants de transaction, déterminez le nombre total d'utilisateurs avec une adresse e-mail valide, ou identifiez les systèmes d'exploitation les plus couramment utilisés.
 6. Recherchez et supprimez les doublons dans les données. Identifiez les enregistrements en double en fonction d'attributs spécifiques et supprimez les doublons pour obtenir un ensemble de données unique.
 7. Manipulez les chaînes de caractères pour extraire des informations spécifiques. Par exemple, extrayez les noms de domaine à partir des adresses e-mail ou recherchez des mots-clés dans les noms d'utilisateurs.
 8. Utilisez des bibliothèques de visualisation de données pour représenter graphiquement certains aspects des données. Par exemple, créez un graphique pour représenter la répartition des adresses IP par pays ou visualisez les montants de transaction par mois.
Consignes supplémentaires :

 1. Chaque étudiant doit travailler individuellement sur les exercices.
 2. Chaque étudiant est invité à présenter ses solutions et ses résultats aux autres étudiants lors d'une séance d'échange d'expériences.
 3. Pendant la séance d'échange, les autres étudiants peuvent poser des questions, discuter des différentes approches utilisées et suggérer des améliorations ou des alternatives.
```
L'objectif de cet exercice est de vous permettre d'appliquer les connaissances en programmation et en manipulation de données sur un ensemble de données simulées.Vous aurez ainsi l'occasion de développer vos compétences, d'échanger des expériences et d'améliorer vos solutions grâce aux discussions avec vos pairs.
```

## géneration 
 - Génération de données personnelles : Utilisez Faker pour générer des noms, adresses, numéros de téléphone et adresses e-mail aléatoires.

 - Génération de données réseau : Utilisez Faker pour générer des adresses IP, adresses MAC et noms d'hôtes aléatoires pour simuler des données de réseau.

 - Création de données d'utilisateurs : Générez des utilisateurs avec des attributs tels que nom, adresse, numéro de téléphone, adresse e-mail et mot de passe aléatoires.

 - Génération de données de transactions : Créez des enregistrements de transactions avec des attributs tels que le nom du client, le montant de la transaction, la date et l'heure, le numéro de compte, etc.

 - Simulation de logs : Générez des logs système ou réseau avec des informations telles que l'adresse IP source, l'adresse IP de destination, le protocole, l'heure, etc.

 - Création d'un annuaire téléphonique : Générez une liste de contacts avec des noms, numéros de téléphone et adresses e-mail aléatoires.

 - Simulation de données de vente : Générez des données de vente avec des attributs tels que le nom du produit, le prix, la quantité, le client, etc.

 - Création de données d'étudiants : Générez des informations d'étudiants avec des attributs tels que le nom, l'âge, l'adresse, la filière, etc.

 - Simulation de données météorologiques : Générez des données fictives par exemple ( des données météorologiques fictives avec des attributs tels que la température, l'humidité, la vitesse du vent, etc. )

 - Création de données fictives par exemple ( de réservation d'hôtel : Générez des réservations d'hôtel avec des attributs tels que le nom du client, la date d'arrivée, la date de départ, le nombre de chambres, etc.)

## exploitation et exploration

- Filtrage des données : Demandez aux étudiants de filtrer les données en fonction de certains critères, tels que la recherche des adresses IP avec un certain masque de sous-réseau, ou la recherche des noms d'utilisateurs commençant par une lettre spécifique.

- Tri des données : trier les données en fonction de différents attributs, par exemple trier les adresses IP par ordre croissant ou décroissant, ou trier les transactions par montant croissant.

- Statistiques et analyses : calculer des statistiques à partir des données générées. calculer la moyenne des montants de transaction, le nombre total d'utilisateurs avec une adresse e-mail valide, ou la fréquence d'utilisation des systèmes d'exploitation.

- Recherche de doublons : détecter et de supprimer les doublons dans les données. identifier les adresses IP en double ou les noms d'utilisateurs en double.

- Manipulation de chaînes de caractères : effectuer des opérations sur les chaînes de caractères générées. Par exemple, extraire les noms de domaine à partir des adresses e-mail, ou rechercher des mots-clés spécifiques dans les noms d'utilisateurs.

- Visualisation des données : utiliser des bibliothèques de visualisation de données, telles que Matplotlib ou Plotly, pour créer des graphiques ou des diagrammes à partir des données générées pour représenter par exemple graphiquement la répartition des adresses IP par pays ou visualiser les montants de transaction par mois.

## gestion des adresses IP et des plages d'adresses

Votre mission consiste à créer un programme en Python pour gérer les adresses IP et les plages d'adresses IP.

Vous devez créer les fonctions suivantes :

### Fonction de validation d'adresse IP :
- Créez une fonction appelée "valider_adresse_ip" qui prend en entrée une adresse IP sous forme de chaîne de caractères.
- La fonction doit vérifier si l'adresse IP est correctement formatée en respectant les règles de syntaxe (quatre octets séparés par des points).
- La fonction doit renvoyer une valeur booléenne : True si l'adresse IP est valide, False sinon.
### Fonction de conversion en binaire :
- Créez une fonction appelée "convertir_en_binaire" qui prend en entrée une adresse IP sous forme de chaîne de caractères.
- La fonction doit convertir chaque octet de l'adresse IP en une représentation binaire sur 8 bits.
- La fonction doit renvoyer une chaîne de caractères contenant la représentation binaire de l'adresse IP.
### Fonction de calcul du masque de sous-réseau :
 - Créez une fonction appelée "calculer_masque_sous_reseau" qui prend en entrée le nombre d'hôtes souhaités.
 - La fonction doit déterminer le nombre de bits nécessaires pour représenter le nombre d'hôtes.
 - La fonction doit calculer le masque de sous-réseau correspondant à ce nombre de bits.
 - La fonction doit renvoyer le masque de sous-réseau sous forme de chaîne de caractères.

 Votre programme doit ensuite demander à l'utilisateur d'entrer une adresse IP et effectuer les opérations suivantes :
 - Valider l'adresse IP en utilisant la fonction "valider_adresse_ip".
 - Si l'adresse IP est valide, afficher sa représentation binaire en utilisant la fonction "convertir_en_binaire".
 - Demander à l'utilisateur de spécifier le nombre d'hôtes souhaités.
 - Calculer et afficher le masque de sous-réseau en utilisant la fonction "calculer_masque_sous_reseau".
 - Assurez-vous de tester votre programme avec différentes adresses IP et nombres d'hôtes pour vérifier son bon fonctionnement.

N'hésitez pas à personnaliser cet exercice en ajoutant des fonctionnalités supplémentaires ou en modifiant les exigences selon vos besoins. Bonne programmation !






