# Votre mission consiste à créer un programme en Python pour gérer les adresses IP et les plages d'adresses IP.

# Vous devez créer les fonctions suivantes :

# Fonction de validation d'adresse IP :
  #  Créez une fonction appelée "valider_adresse_ip" qui prend en entrée une adresse IP sous forme de chaîne de caractères.
  #  La fonction doit vérifier si l'adresse IP est correctement formatée en respectant les règles de syntaxe (quatre octets séparés par des points).
  #  La fonction doit renvoyer une valeur booléenne : True si l'adresse IP est valide, False sinon.
# Fonction de conversion en binaire :
  #  Créez une fonction appelée "convertir_en_binaire" qui prend en entrée une adresse IP sous forme de chaîne de caractères.
  #  La fonction doit convertir chaque octet de l'adresse IP en une représentation binaire sur 8 bits.
  #  La fonction doit renvoyer une chaîne de caractères contenant la représentation binaire de l'adresse IP.
# Fonction de calcul du masque de sous-réseau :
  #  Créez une fonction appelée "calculer_masque_sous_reseau" qui prend en entrée le nombre d'hôtes souhaités.
  #  La fonction doit déterminer le nombre de bits nécessaires pour représenter le nombre d'hôtes.
  #  La fonction doit calculer le masque de sous-réseau correspondant à ce nombre de bits.
  #  La fonction doit renvoyer le masque de sous-réseau sous forme de chaîne de caractères.
# Votre programme doit ensuite demander à l'utilisateur d'entrer une adresse IP et effectuer les opérations suivantes :
  #  Valider l'adresse IP en utilisant la fonction "valider_adresse_ip".
  #  Si l'adresse IP est valide, afficher sa représentation binaire en utilisant la fonction "convertir_en_binaire".
  #  Demander à l'utilisateur de spécifier le nombre d'hôtes souhaités.
  #  Calculer et afficher le masque de sous-réseau en utilisant la fonction "calculer_masque_sous_reseau".
  #  Assurez-vous de tester votre programme avec différentes adresses IP et nombres d'hôtes pour vérifier son bon fonctionnement.
# N'hésitez pas à personnaliser cet exercice en ajoutant des fonctionnalités supplémentaires ou en modifiant les exigences selon vos besoins. Bonne programmation !
import ipaddress
import math

"""
  verify ip format 
  return boolean
"""
def valider_adresse_ip(ip: str):
  try:
    ipaddress.ip_address(ip)
    return True
  except ValueError:
    return False
  
"""
convert ip to binary on 8 bit
return str on conversion
"""
def convertir_en_binaire(ip: str):
  binary_ip = '.'.join(format(int(x), '08b') for x in ip.split('.'))
  return binary_ip

"""
  determine the number of bit necessary to represent the nb_host
  calculate the subnet mask according to the previous result
  return subnet mask as str
"""  
def calculer_masque_sous_reseau(nb_hosts: int):
  # calculate the number of bits necessary for the hosts
  host_bits = math.ceil(math.log2(nb_hosts + 2))
  
  # calculate the number of bits for the network
  network_bits = 32 - host_bits
  
  # create the subnet mask
  mask = [0, 0, 0, 0]
  for i in range(4):
      if network_bits > 7:
          mask[i] = 255
          network_bits -= 8
      else:
          mask[i] = 256 - 2 ** (8 - network_bits)
          network_bits = 0
  
  subnet_mask = '.'.join(str(i) for i in mask)

  return subnet_mask

"""
  check if value is an integer
"""
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

print('hello there!')  
is_valid_ip = False
while not is_valid_ip:
  print('For me to be able to give you a subnet mask, please provide a valid ip address')
  ip = input()
  if not valider_adresse_ip(ip):
    print("------------------------------------------------------------------------------")
    print('The ip address provided is not valide. \nPlease check your ip address')
    print("------------------------------------------------------------------------------")
    continue
  print('the ip address provided is valide')
  print('The binary representation of ypu ip address is')
  print(convertir_en_binaire(ip))
  is_valid_ip = True
  is_int = False
  while not is_int:
    print('How many hosts would you like to allow on the network')
    host_required = input()
    if not is_integer(host_required):
      print('please provide a valid integer')
      continue
    subnet_mask = calculer_masque_sous_reseau(int(host_required))
    print(f'your subnet mask will be {subnet_mask}')
    print(f'the binary version of your subnet mask will be {convertir_en_binaire(subnet_mask)}')
    is_int = True

# program must ask the user to provide an ip address
  # must validate ip
  # if validated print binary of ip address
# must ask the number of host needed
  # must calculate the subnet mask
  
  
  