from buildtrsx.build_project import (
    trsx_sources_node,
    trsx_metadata_node,
    trsx_gather_nodes,
)
from buildtrsx.build_ontology.build_ontology import (
    trsx_intents_node,
    trsx_links_node,
    trsx_concepts_node,
    trsx_gather_subnodes_ontology,
)
# metadata node
metadata_node = trsx_metadata_node(
    author="Danae Martinez",
    version="1.0.0",
    description="investment NLU model",
    date="february 2022",
)

# sources node
sources = {
    "nuance_custom_data": {
        "displayName": "nuance_custom_data",
        "version": "1.0",
        "type": "CUSTOM",
        "useForOOV": "true",
    },
    "verint": {"displayName": "verint", "version": "1.0"},
    "cc_ana_cc": {"displayName": "cc_ana_cc", "version": "1.0"},
    "my_data": None,
}

# metadata node
sources_node = trsx_sources_node(sources=sources)

project_attributes = {
    "xmlns:nuance": "https://developer.nuance.com/mix/nlu/trsx",
    "xml:lang": "fra-CAN",
    "nuance:enginePackVersion": "hosted",
}

# ontology node
intents = {
    "MAKE_WITHDRAWAL": [
        {"conceptref": "FROM_ACCOUNT"},
        {"conceptref": "TO_ACCOUNT"},
        {"conceptref": "ACCOUNT_TYPE"},
        {"conceptref": "AMOUNT"},
    ],
    "MAKE_INVESTMENT": [
        {"conceptref": "FROM_ACCOUNT"},
        {"conceptref": "TO_ACCOUNT"},
        {"conceptref": "ACCOUNT_TYPE"},
        {"conceptref": "AMOUNT"},
    ],
    "REQUEST_FOLLOW_UP": [
        {"conceptref": "ACCOUNT_TYPE"},
        {"conceptref": "AMOUNT"},
        {"conceptref": "DATE"},
        {"conceptref": "DATE_TRANSACTION"},
    ],
    "MAKE_AMENDMENT": [{"conceptref": "ACCOUNT_TYPE"}],
    "OPEN_ACCOUNT": [{"conceptref": "ACCOUNT_TYPE"}],
    "REQUEST_BALANCE": [{"conceptref": "ACCOUNT_TYPE"}],
    "OUT_OF_DOMAIN": [],
    "GOODBYE": []
}

intents_node = trsx_intents_node(intents=intent)

entities = {
    "TO_ACCOUNT": {"type": "isA", "conceptref": "ACCOUNT_TYPE"},
    "FROM_ACCOUNT": {"type": "isA", "conceptref": "ACCOUNT_TYPE"},
    "AMOUNT": {"type": "isA", "conceptref": "nuance_AMOUNT"},
    "INVESTMENT_ACCOUNT": {"type": "hasA", "conceptref": ["ACCOUNT_TYPE", "ACCOUNT_NUMBER", "ACCOUNT_BALANCE"]},
    "ACCOUNT_TYPE": {},

}

concepts_node = trsx_concepts_node(entities=entities)
print(concepts_node)



trsx = trsx_gather_nodes(
    metadata_node=metadata_node,
    sources_node=sources_node,
    attributes=project_attributes,
)

print(trsx)

with open("test.trsx", "w", encoding="utf-8") as f:
    f.write(trsx)
