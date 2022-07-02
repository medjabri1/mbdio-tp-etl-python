# IMPORTS
from itertools import islice
import numpy
import collections
# Create collections
person_col = collections.namedtuple('Person', 'idp nom prenom idadr')
adresse_col = collections.namedtuple('Adresse', 'idadr loc ville')
personne_data_array = []
adresse_data_array = []
personne_adresse_data_array = []
###########################
# EXTRACT
file_input_personne = open("./input/personne.txt", "r")
file_input_adresse = open("./input/adresse.txt", "r")
###########################
# TRANSFORM
for line in islice(file_input_personne, 1, None):

    fields = line.split(";")

    idp = fields[0]
    nom = fields[1]
    prenom = fields[2]
    idadr = fields[3][:-1]

    personne_data_array.append(person_col(idp, nom, prenom, idadr))

for line in islice(file_input_adresse, 1, None):

    fields = line.split(";")

    idadr = fields[0]
    loc = fields[1]
    ville = fields[2][:-1]

    adresse_data_array.append(adresse_col(idadr, loc, ville))
###########################
# LOAD

for personne in personne_data_array:
    for adresse in adresse_data_array:
        if int(personne.idadr) == int(adresse.idadr):
            personne_adresse_data_array.append(
                [personne.idp, personne.nom, personne.prenom, adresse.idadr, adresse.loc, adresse.ville])


with open("./output/per_adr.txt", "w") as txt_file:

    txt_file.write("idp;nom;prenom;idadr;loc;ville\n")

    for line in personne_adresse_data_array:
        txt_file.write(";".join(line) + "\n")

file_input_personne.close()
file_input_adresse.close()
