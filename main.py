from buildtrsx.build_project import trsx_gather_nodes
from buildtrsx.build_ontology.build_ontology import (
    trsx_intents_node,
    trsx_concepts_node,
    trsx_gather_subnodes_ontology,
)

intents_investment = {
    "MAKE_AMENDMENT": [{"conceptref": "ACCOUNT_TYPE"}],
    "MAKE_INVESTMENT": [
        {"conceptref": "FROM_ACCOUNT"},
        {"conceptref": "TO_ACCOUNT"},
        {"conceptref": "AMOUNT"},
    ],
    "MAKE_WITHDRAWAL": [
        {"conceptref": "FROM_ACCOUNT"},
        {"conceptref": "TO_ACCOUNT"},
        {"conceptref": "AMOUNT"},
    ],
    "OPEN_ACCOUNT": [{"conceptref": "ACCOUNT_TYPE"}],
    "REQUEST_BALANCE": [{"conceptref": "ACCOUNT_TYPE"}],
    "REQUEST_FOLLOW_UP": [{"conceptref": "ACCOUNT_TYPE"}],
    "NO_INTENT": [],
}

# intents without entitites associated
intents_node = trsx_intents_node(intents=intents_investment)
print(intents_node)

entities = {
    "TO_ACCOUNT": {},  # {'type':"isA", 'conceptref':"ACCOUNT_TYPE"},
    "FROM_ACCOUNT": {},  # {'type':"isA", 'conceptref':"ACCOUNT_TYPE", "sourceref": "some source"},
    "AMOUNT": {},  # {'type':"isA", 'conceptref':"nuance_AMOUNT"},
    "ACCOUNT_TYPE": {},
}  # {'type':"hasA", 'conceptref':["ACCOUNT_BALANCE", "ACCOUNT_NUMBER", "ACCOUNT_TYPE"]}}


concepts_node = trsx_concepts_node(entities=entities)
print(concepts_node)
