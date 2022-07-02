# IMPORTS
from itertools import islice
import collections
# Vars
person_col = collections.namedtuple('Person', 'idp nom prenom idadr')
personne_data_array = []

###########################
# EXTRACT

file_input_personne = open("./input/personne.txt", "r")

###########################
# TRANSFORM
for line in islice(file_input_personne, 1, None):

    fields = line.split(";")

    idp = fields[0]
    nom = fields[1]
    prenom = fields[2]
    idadr = fields[3][:-1]

    personne_data_array.append(person_col(idp, nom, prenom, idadr))
###########################
# LOAD
with open("./output/per_out.txt", "w") as txt_file:

    txt_file.write("idp;nom;prenom;idadr\n")

    for line in personne_data_array:
        txt_file.write(";".join(line) + "\n")

file_input_personne.close()
