# Traitement et analyse de données simulées
# Description de l'exercice :

# Vous disposez d'un ensemble de données simulées générées avec la bibliothèque Faker. Ces données représentent des informations telles que des adresses IP, des adresses MAC, des noms d'ordinateurs, des systèmes d'exploitation, des sites web consultés, etc. Votre tâche est de manipuler et d'analyser ces données en utilisant les concepts et les instructions vus précédemment.

# Instructions :

# 1. Importez la bibliothèque Faker et générez un ensemble de données simulées comprenant au moins 100 enregistrements.
# 2. Affichez les premières lignes des données pour vous familiariser avec leur structure.
# 3. Effectuez un filtrage des données en fonction de critères spécifiques. Par exemple, filtrez les adresses IP avec un masque de sous-réseau particulier ou filtrez les transactions avec un montant supérieur à une valeur donnée.
# 4. Triez les données en fonction d'attributs spécifiques. Par exemple, triez les adresses IP par ordre croissant ou décroissant, ou triez les noms d'utilisateurs par ordre alphabétique.
# 5. Calculez des statistiques à partir des données. Par exemple, calculez la moyenne des montants de transaction, déterminez le nombre total d'utilisateurs avec une adresse e-mail valide, ou identifiez les systèmes d'exploitation les plus couramment utilisés.
# 6. Recherchez et supprimez les doublons dans les données. Identifiez les enregistrements en double en fonction d'attributs spécifiques et supprimez les doublons pour obtenir un ensemble de données unique.
# 7. Manipulez les chaînes de caractères pour extraire des informations spécifiques. Par exemple, extrayez les noms de domaine à partir des adresses e-mail ou recherchez des mots-clés dans les noms d'utilisateurs.
# 8. Utilisez des bibliothèques de visualisation de données pour représenter graphiquement certains aspects des données. Par exemple, créez un graphique pour représenter la répartition des adresses IP par pays ou visualisez les montants de transaction par mois.
# Consignes supplémentaires :

# 1. Chaque étudiant doit travailler individuellement sur les exercices.
# 2. Chaque étudiant est invité à présenter ses solutions et ses résultats aux autres étudiants lors d'une séance d'échange d'expériences.
# 3. Pendant la séance d'échange, les autres étudiants peuvent poser des questions, discuter des différentes approches utilisées et suggérer des améliorations ou des alternatives.

# Cet exercice répond également au question de celui-ci 
# https://github.com/orgs/it-akademy-students/projects/22/views/2?pane=issue&itemId=31260174

from collections import Counter
from faker import Faker 
import matplotlib.pyplot as plt

fake = Faker()

data = []

for _ in range(139):
    record = {
        'ip_address': fake.ipv4_private(),
        'mac_address': fake.mac_address(),
        'computer_name': fake.user_name(),
        'os': fake.random_element(['Windows', 'Linux', 'Mac']),
        'website': fake.url()
    }
    data.append(record)
print("------------------------------------------------------------------------------")
print("Show three first lignes of data ")
    
# show the first 3 records of the data set
for record in data [:3]:
  print(record)
  print("---------------------------------------")

print("------------------------------------------------------------------------------")
print("return only ip starting by '192' ")

def ipFilter(filter):
  # initiate filtered_ips
  filtered_ips = []

  # function takes a subNetwork mask and return the ip corresponding to the subNetwork
  for record in data:
    splitIp =  record['ip_address'].split('.')[0]
    # print(splitIp)
    if int(splitIp) == int(filter):
      filtered_ips.append(record['ip_address'])

  print(filtered_ips)
  
  
# call the ip filter function 
ipFilter("192")

print("------------------------------------------------------------------------------")
print("sort data by a given key ")

"""sort a given set of data by a specific key in asc order
"""
def sortBy(list: list, key: str):
  list.sort(key=lambda user:user[key])
  print(list)


sortBy(data, "computer_name")

print("------------------------------------------------------------------------------")

"""count the occurrences of specific key in dataset 
"""
def countSpecificKey(data: list, key: str):
  os_list = [item[key] for item in data]
  return dict(Counter(os_list))

os_dict = countSpecificKey(data, "os")

def totalOs():
  return sum(os_dict.values())

"""get the most present os
"""
def maxOs():
  return max(os_dict, key=os_dict.get)

"""get the least present os
"""
def minOs(): 
  return min(os_dict, key=os_dict.get)

def getKeyPercentages(data_dict: dict): 
  return {key: round((count / totalOs()) * 100) for key, count in data_dict.items()}

print(f"Here are the how many time the os as been seen {os_dict}")
print(f"Number on connexion {totalOs()}")
print(f"the os that has been the most seen is {maxOs()}")
print(f"the os that has been the least seen is {minOs()}")
print(f"Percentage of connexion by os {getKeyPercentages(os_dict)}")

print("------------------------------------------------------------------------------")
print("Delete all duplicate element from data based on given key")

"""delete duplicate in list based on specified field 
"""
def deleteDuplicateByKey(data_list: list, key: str):
  data_key_set = set()
  unique_data_list = []
  
  # loop on data_list
  for record in data_list:
    # check if specific key is in unique data_key_set list
    if record[key] not in data_key_set:
      # add the value of the specific key in unique data_key_set list
      data_key_set.add(record[key])
      # add the record in a new list
      unique_data_list.append(record)
  return unique_data_list
  
  
print(deleteDuplicateByKey(data, 'os'))

print("------------------------------------------------------------------------------")
print("Generate a visual by givin a set of data, a title and the graphic size")

# generate a visual form data

# count repetition of specific élément
list_of_os = countSpecificKey(data, 'os')
# calculate the percentages of repetition
list_of_os_percentages = getKeyPercentages(list_of_os)
# determine the size of graphique window
graphic_scale = [10, 10]

"""
generate a visual form data
"""
def generate_graphic(data_dict: dict, title: str, scale: list):
  # define figure's size
  plt.subplot(131)
  plt.figure(figsize=(scale))
  plt.bar(data_dict.keys(), data_dict.values())
  plt.ylabel('%')
  plt.suptitle(title)
  plt.show()

generate_graphic(list_of_os_percentages, "récurrence des OS en pourcentage", graphic_scale)
