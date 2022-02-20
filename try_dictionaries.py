from buildtrsx.build_dictionaries.build_dict import trsx_dictionary_node, trsx_dictionaries_node
from buildtrsx.build_project import trsx_gather_nodes


account_type = {
    "CELI": ["CELI", "Compte libre d’impôt"],
    "REER": ["REER", "Compte d’épargne-retraite"],
    "REEE": ["REEE", "R trois E"],
}
literals = {"ACCOUNT_TYPE": account_type}

dictionary_node = trsx_dictionary_node(entity="ACCOUNT_TYPE", literals=account_type)
print(dictionary_node)

dictionaries_node = trsx_dictionaries_node(entities=literals)
print(dictionaries_node)

project_attributes = {
    "xmlns:nuance": "https://developer.nuance.com/mix/nlu/trsx",
    "xml:lang": "eng-USA",  # 'fra-CAN'
    "nuance:enginePackVersion": "hosted",
}

project_node = trsx_gather_nodes(
    dictionaries_node=dictionaries_node, attributes=project_attributes
)
print(project_node)
