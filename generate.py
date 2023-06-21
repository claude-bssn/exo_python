#  Génération de données personnelles : Utilisez Faker pour générer des noms, adresses, numéros de téléphone et adresses e-mail aléatoires.
#  Génération de données réseau : Utilisez Faker pour générer des adresses IP, adresses MAC et noms d'hôtes aléatoires pour simuler des données de réseau.
#  Création de données d'utilisateurs : Générez des utilisateurs avec des attributs tels que nom, adresse, numéro de téléphone, adresse e-mail et mot de passe aléatoires.
#  Génération de données de transactions : Créez des enregistrements de transactions avec des attributs tels que le nom du client, le montant de la transaction, la date et l'heure, le numéro de compte, etc.
#  Simulation de logs : Générez des logs système ou réseau avec des informations telles que l'adresse IP source, l'adresse IP de destination, le protocole, l'heure, etc.
#  Création d'un annuaire téléphonique : Générez une liste de contacts avec des noms, numéros de téléphone et adresses e-mail aléatoires.
#  Simulation de données de vente : Générez des données de vente avec des attributs tels que le nom du produit, le prix, la quantité, le client, etc.
#  Création de données d'étudiants : Générez des informations d'étudiants avec des attributs tels que le nom, l'âge, l'adresse, la filière, etc.
#  Simulation de données météorologiques : Générez des données fictives par exemple ( des données météorologiques fictives avec des attributs tels que la température, l'humidité, la vitesse du vent, etc. )
#  Création de données fictives par exemple ( de réservation d'hôtel : Générez des réservations d'hôtel avec des attributs tels que le nom du client, la date d'arrivée, la date de départ, le nombre de chambres, etc.)

from faker import Faker 
import faker_commerce
import uuid
import random

fake = Faker()
fake.add_provider(faker_commerce.Provider)

print("Personal data")

personal_data = []

for _ in range(10):
    record = {
        'last_name': fake.last_name(),
        'first_name': fake.first_name(),
        'address': fake.address(),
        'phone': fake.phone_number(),
        'email': fake.email()
    }
    personal_data.append(record)

print(personal_data)

print("------------------------------------------------------------------------------")
print("Users")

user = []

for _ in range(10):
    record = {
        'last_name': fake.last_name(),
        'first_name': fake.first_name(),
        'address': fake.address(),
        'phone': fake.phone_number(),
        'email': fake.email(),
        'password': fake.password()
    }
    user.append(record)

print(user)

print("------------------------------------------------------------------------------")
print("Transaction")

transactions = []

for _ in range(10):
    record = {
        'customer': fake.last_name(),
        'amount': round(fake.random.uniform(0.5, 500.0), 2),
        'transaction_time': fake.date_time(),
        'iban': fake.iban()
    }
    transactions.append(record)

print(transactions)

print("------------------------------------------------------------------------------")
print("Logs")

logs = []

for _ in range(10):
    record = {
        'ip': fake.ipv4_private(),
        'destination-ip': fake.ipv4_private(),
        'protocol': fake.random_element(['TCP', 'IP', 'UDP', 'POP', 'SMTP', 'FTP', 'HTTP', 'HTTPS']),
        'request_time': fake.date_time()
    }
    logs.append(record)

print(logs)

print("------------------------------------------------------------------------------")
print("Contacts")

contacts = []

for _ in range(10):
    record = {
      'last_name': fake.last_name(),
      'first_name': fake.first_name(),
      'phone': fake.phone_number(),
      'email': fake.email(),
    }
    contacts.append(record)

print(contacts)

print("------------------------------------------------------------------------------")
print("Sales")

rd = random.Random()
rd.seed(0)
sales = []

for _ in range(10):
    record = {
      'product': fake.ecommerce_name(),
      'price': round(fake.random.uniform(10.5, 1000.0), 2),
      'quantity': fake.numerify(text='###'),
      'customer': uuid.UUID(int=rd.getrandbits(128)),
    }
    sales.append(record)

print(sales)

print("------------------------------------------------------------------------------")
print("Students")
#  Création de données d'étudiants : Générez des informations d'étudiants avec des attributs tels que le nom, l'âge, l'adresse, la filière, etc.

students = []

for _ in range(10):
    record = {
      'name': fake.name(),
      'age': fake.random_int(min=17, max=45) ,
      'address': fake.address(),
      'cursus': fake.random_element({
        'Doctor of Arts (DA)',
        'Doctor of Business Administration (DBA)',
        'Doctor of Canon Law (JCD)',
        'Doctor of Design (DDes)',
        'Doctor of Engineering or Engineering Science (DEng, DESc, DES)',
        'Doctor of Education (EdD)',
        'Doctor of Fine Arts (DFA.)',
        'Doctor of Hebrew Letters (DHL)'
      }),
    }
    students.append(record)

print(students)

print("------------------------------------------------------------------------------")
print("Weather")
#  Simulation de données météorologiques : Générez des données fictives par exemple ( des données météorologiques fictives 
#  avec des attributs tels que la température, l'humidité, la vitesse du vent, etc. )

weather = []

for _ in range(10):
    record = {
      'temperature': round(fake.random.uniform(-30.00, 50.00), 2),
      'humidity': fake.random_int(min=0, max=100) ,
      'wind': round(fake.random.uniform(0.00, 200.00), 2),
      'state': fake.random_element({
        'sunny',
        'rain',
        'overcast',
        'snow',
        'storm',
        'light rain',
        'hurricane'
      }),
    }
    weather.append(record)

print(weather)

print("------------------------------------------------------------------------------")
print("Hotels")
#  Création de données fictives par exemple ( de réservation d'hôtel : Générez des réservations d'hôtel 
# avec des attributs tels que le nom du client, la date d'arrivée, la date de départ, le nombre de chambres, etc.)

hotels = []

for _ in range(10):
    record = {
      'customer': round(fake.random.uniform(-30.00, 50.00), 2),
      'checkin_date': fake.random_int(min=0, max=100) ,
      'checkout_date': round(fake.random.uniform(0.00, 200.00), 2),
      'room_number': fake.random_element({
        'sunny',
        'rain',
        'overcast',
        'snow',
        'storm',
        'light rain',
        'hurricane'
      }),
    }
    hotels.append(record)

print(hotels)