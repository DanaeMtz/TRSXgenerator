from buildtrsx.build_ontology.build_ontology import (
    trsx_intents_node,
    trsx_concepts_node,
    trsx_gather_subnodes_ontology,
)
from buildtrsx.build_project import trsx_gather_nodes

# example of intents node
intent = {
    "MAKE_WITHDRAWAL": [
        {"conceptref": "FROM_ACCOUNT"},
        {"conceptref": "TO_ACCOUNT"},
        {"conceptref": "AMOUNT"},
    ],
    "MAKE_INVESTMENT": [
        {"conceptref": "FROM_ACCOUNT"},
        {"conceptref": "TO_ACCOUNT"},
        {"conceptref": "AMOUNT"},
    ],
}
intents_node = trsx_intents_node(intents=intent)
print(intents_node)

# example of concepts (entities) node
entities = {
    "TO_ACCOUNT": {},
    "FROM_ACCOUNT": {},
    "AMOUNT": {},
    "ACCOUNT_TYPE": {},
}

concepts_node = trsx_concepts_node(entities=entities)
print(concepts_node)

# example 2: add relations
entities_rel = {
    "TO_ACCOUNT": {"type": "isA", "conceptref": "ACCOUNT_TYPE"},
    "FROM_ACCOUNT": {"type": "isA", "conceptref": "ACCOUNT_TYPE"},
    "AMOUNT": {"type": "isA", "conceptref": "nuance_AMOUNT"},
    "ACCOUNT_TYPE": {},
}

concepts_node2 = trsx_concepts_node(entities=entities_rel)
print(concepts_node2)

# gather the two sub-nodes and wrap them into the ontology node
ontology_node = trsx_gather_subnodes_ontology(
    intents_node=intents_node, concepts_node=concepts_node
)
print(ontology_node)

# wrap with in the project's node
project_attributes = {
    "xmlns:nuance": "https://developer.nuance.com/mix/nlu/trsx",
    "xml:lang": "eng-USA",  # 'fra-CAN'
    "nuance:enginePackVersion": "hosted",
}

project_node = trsx_gather_nodes(
    ontology_node=ontology_node, attributes=project_attributes
)
print(project_node)
