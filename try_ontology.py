from buildtrsx.build_ontology.build_ontology import trsx_link_node, trsx_intents_node, \
    trsx_relations_node, trsx_settings_node, trsx_concepts_node, trsx_ontology_node

# build ontology script

entity1_make_inv = {'conceptref':'FROM_ACCOUNT', 'sourceref': 'some_source'}
entity2_make_inv = {'conceptref':'TO_ACCOUNT', 'sourceref': 'some_source'}
entity3_make_inv = {'conceptref': 'ACCOUNT_TYPE', 'sourceref': 'some_source'}
entity4_make_inv = {'conceptref': 'AMOUNT', 'sourceref': 'some_source'}
entity1_open_acc = {'conceptref':"ACCOUNT_TYPE"}


intent_entities = {"MAKE_INVESTMENT": [entity1_make_inv,
                                       entity2_make_inv,
                                       entity3_make_inv,
                                       entity4_make_inv],
                   "OPEN_ACCOUNT" : [entity1_open_acc],
                   "OUT_OF_DOMAIN" : [],
                   "GOODBYE" : []}

print(trsx_link_node(entity = intent_entities["MAKE_INVESTMENT"][0]))
intents_node = trsx_intents_node(intents = intent_entities)
print(intents_node)

entities = {"TO_ACCOUNT":{'type':"isA", 'conceptref':"ACCOUNT_TYPE"},
            "FROM_ACCOUNT":{'type':"isA", 'conceptref':"ACCOUNT_TYPE", "sourceref": "some source"},
            "AMOUNT":{'type':"isA", 'conceptref':"nuance_AMOUNT"},
            "BANK_ACCOUNT":{'type':"hasA", 'conceptref':["ACCOUNT_BALANCE", "ACCOUNT_NUMBER", "ACCOUNT_TYPE"]}}

print(trsx_relations_node(entity_rel = entities["FROM_ACCOUNT"]))
print(trsx_relations_node(entity_rel = entities["BANK_ACCOUNT"]))

setting = {"ACCOUNT_TYPE":{'name':'isSensitive', 'value':"true"},
           "BANK_ACCOUNT":{'name':'isSensitive', 'value':"true"}}

print(trsx_settings_node(setting = setting["BANK_ACCOUNT"]))

concepts_node = trsx_concepts_node(entities = entities)
ontology_node = trsx_ontology_node(intents_node = intents_node,
                                   concepts_node = concepts_node)