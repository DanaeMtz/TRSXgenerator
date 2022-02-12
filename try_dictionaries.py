from buildtrsx.build_dictionaries.build_dict import trsx_dictionary, trsx_dictionaries

account_type = {'CELI':['CELI','Compte d’épargne libre d’impôt', 'Compte libre d’impôt'],
                'REER':['REER','Régime enregistré d’épargne retraite', 'Compte d’épargne-retraite']}

entities_literals_dict = {"ACCOUNT_TYPE":account_type}

print(trsx_dictionary(entity = "ACCOUNT_TYPE", literals = account_type))
print(trsx_dictionaries(entities = entities_literals_dict))