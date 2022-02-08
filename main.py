from buildtrsx.build_dictionaries.build_dict import trsx_dictionary
from buildtrsx.build_project import trsx_project_node, trsx_metadata_node, trsx_sources_node
from buildtrsx.build_ontology.build_ontology import trsx_links_node, trsx_intents_node, trsx_relations_node, trsx_settings_node, trsx_entities_node

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

#Intent-entity links
ontology_investment = {'REQUEST_BALANCE': ['ACCOUNT_TYPE']
                       , 'REQUEST_FOLLOWUP': ['ACCOUNT_TYPE']
                       , 'OPEN_ACCOUNT': ['ACCOUNT_TYPE']
                       , 'MAKE_INVESTMENT': ['FROM_ACCOUNT', 'TO_ACCOUNT', 'AMOUNT']
                       , 'MAKE_WITHDRAWAL': ['FROM_ACCOUNT', 'TO_ACCOUNT', 'AMOUNT']
                       , 'MAKE_AMENDMENT': ['ACCOUNT_TYPE']
                       , 'OUT_OF_DOMAIN' : []
                       }
#Entity types (possible options: List, Relationship, dynamic, etc)
entity_types = {'ACCOUNT_TYPE':{'entity_type':'List'}
                , 'FROM_ACCOUNT': {'entity_type':'Relationship'}
                , 'TO_ACCOUNT': {'entity_type':'Relationship'}
                , 'AMOUNT': {'entity_type':'Relationship'}
                , 'BANK_ACCOUNT': {'entity_type':'Relationship'}
                }
# Entity relationships (relationships that entities can have between entities. {isA, hasA, hasReferrers})
entity_relations_types = {'ACCOUNT_TYPE': {'entity_type':'List'}
                        , 'FROM_ACCOUNT': {'entity_type':'Relationship', 'type':"isA", 'conceptref':"ACCOUNT_TYPE"}
                        , 'TO_ACCOUNT': {'entity_type':'Relationship', 'type':"isA", 'conceptref':"ACCOUNT_TYPE"}
                        , 'AMOUNT': {'entity_type':'Relationship', 'type':"isA", 'conceptref':"nuance_AMOUNT"}
                        , 'BANK_ACCOUNT': {'entity_type':'Relationship', 'type':"hasA", 'conceptref': ['ACCOUNT_BALANCE', 'ACCOUNT_NUMBER', 'ACCOUNT_TYPE']}
                        }

#print(entity_types['ACCOUNT_TYPE']['entity_type'])
#print(trsx_relations_node(rel_dict={'entity_type':'Relationship', 'type':"hasA", 'conceptref': ['ACCOUNT_BALANCE', 'ACCOUNT_NUMBER', 'ACCOUNT_TYPE']}))
#print(trsx_relations_node(rel_dict={'entity_type':'Relationship', 'type':"isA", 'conceptref':"nuance_AMOUNT"}))
#print(trsx_settings_node())
print(trsx_entities_node(rel_typ_dict = entity_relations_types))
#print(entity_relationships['BANK_ACCOUNT'])
#{'type':"isA", 'conceptref':"ACCOUNT_TYPE"}

#print(entity_relationships['FROM_ACCOUNT']['type'])
#print(entity_relationships['FROM_ACCOUNT']['conceptref'])
#print(trsx_relations_node(type = entity_relationships['FROM_ACCOUNT']['type']
#                          , conceptref = entity_relationships['FROM_ACCOUNT']['conceptref']))
print(trsx_intents_node(int_ent_dict = ontology_investment))
#print(trsx_dictionary(dictionary = ACCOUNT_TYPE))
#print(trsx_project_node())
#print(trsx_metadata_node(str="str"))
#print(trsx_sources_node())
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


