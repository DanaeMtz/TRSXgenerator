from buildtrsx.build_dictionaries.build_dict import trsx_dictionary
from buildtrsx.build_project import trsx_project

#---# ACCOUNT TYPES #---#

registered_plans_FR = {"CELI": ["CELI", "Compte d’épargne libre d’impôt", "Compte libre d’impôt"],
                       "REER": ["REER", "Régime enregistré d’épargne retraite", "Compte d'épargne-retraite"],
                       "REEE": ["REEE", "Régime enregistré d’épargne-études", "Régime d'épargne de mes enfants", "Compte d’épargne pour les études", "Compte R trois E"],
                       "CPG": ["CPG" , "Certificat de placement garanti", "Certificat", "Placement garanti"] # not a plan, but can be placed in a CELI or in a REER
                       }

Annuities_retirement_funds_FR = {"FERR": ["FERR", "Fonds enregistré de revenu de retraite", "Compte de revenu de retraite"],
                                 "CRI": ["CRI", "Compte de retraite immobilisé"],
                                 "FRV": ["FRV", "Fonds de revenu viager"]
                                 }

regular_accounts_FR = {"Compte chèques": ["Compte chèques", "Compte bancaire", "Compte courant"],
                       "Compte épargne à intérêt élevé": ["Compte épargne à intérêt élevé", "Compte épargne","Compte d'épargne"]
                       }

ACCOUNT_TYPE = {**registered_plans_FR, **regular_accounts_FR, **Annuities_retirement_funds_FR}
print(trsx_dictionary(dictionary = ACCOUNT_TYPE))
#print(trsx_project(lang = 'fra-CAN'))
#print(trsx_dictionary(dictionary = Annuities_retirement_funds_FR))
#print(trsx_dictionary(dictionary = regular_accounts_FR))

#def trsx_dictionary(dictionary):
#    doc, tag, text = Doc().tagtext()
#    for key in dictionary:
#        for value in dictionary[key]:
#            #print(key, 'corresponds to', value)
#            doc.stag('entry', literal=value, value=key)
#
#    return doc.getvalue()

#if __name__ == '__main__':
#    print(trsx_dictionary(dictionary = registered_plans_FR))


