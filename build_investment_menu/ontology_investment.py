from buildtrsx.build_project import (
    trsx_metadata_node,
    trsx_gather_nodes,
)
from buildtrsx.build_ontology.build_ontology import (
    trsx_intents_node,
    trsx_concepts_node,
    trsx_gather_subnodes_ontology,
)

# metadata node
metadata_node = trsx_metadata_node(
    author="Danae Martinez",
    version="1.0.1",
    description="Investment NLU model",
    date="May 2022",
)

project_attributes = {
    "xmlns:nuance": "https://developer.nuance.com/mix/nlu/trsx",
    "xml:lang": "fra-CAN",
    "nuance:enginePackVersion": "hosted",
    "nuance:version": "2.5",
}

# ontology node
intents = {
    "OPEN_ACCOUNT": [{"conceptref": "INVESTMENT_PERSONAL "}],
    "CLOSE_ACCOUNT": [{"conceptref": "INVESTMENT_PERSONAL "}],
    "REQUEST_BALANCE": [{"conceptref": "INVESTMENT_PERSONAL "}],
    "WITHDRAWAL": [
        {"conceptref": "INVESTMENT_PERSONAL "},
        {"conceptref": "TRANSACTIONAL_PERSONAL  "},
        {"conceptref": "AMOUNT"},
    ],
    "INVEST": [
        {"conceptref": "INVESTMENT_PERSONAL "},
        {"conceptref": "TRANSACTIONAL_PERSONAL  "},
        {"conceptref": "AMOUNT"},
    ],
    "INVEST_ATM": [
        {"conceptref": "INVESTMENT_PERSONAL "},
        {"conceptref": "TRANSACTIONAL_PERSONAL  "},
        {"conceptref": "AMOUNT"},
        {"conceptref": "PERIODICITY"},
    ],
    "AMENDMENT": [
        {"conceptref": "INVESTMENT_PERSONAL"},
        {"conceptref": "AMOUNT"},
        {"conceptref": "PERIODICITY"},
    ],
    "OUT_OF_DOMAIN": [],
    "GOODBYE": [],
    "OUI_NON": [],
}

intents_node = trsx_intents_node(intents=intents)
print(intents_node)

entities = {
    "AMOUNT": {"type": "isA", "conceptref": "nuance_AMOUNT"},
    "INVESTMENT_PERSONAL": {},
    "TRANSACTIONAL_PERSONAL": {},
    "COMMAND": {},  # handle global commands
    "OUI_NON": {"type": "isA", "conceptref": "YES_NO"},
}

concepts_node = trsx_concepts_node(entities=entities)
print(concepts_node)

# gather the two sub-nodes and wrap them into the ontology node
ontology_node = trsx_gather_subnodes_ontology(
    intents_node=intents_node, concepts_node=concepts_node
)

trsx = trsx_gather_nodes(
    metadata_node=metadata_node,
    ontology_node=ontology_node,
    attributes=project_attributes,
)

with open("outputs/ontology_investment.trsx", "w", encoding="utf-8") as f:
    f.write(trsx)
