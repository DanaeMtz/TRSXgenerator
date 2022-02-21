from buildtrsx.build_dictionaries.build_dict import (
    trsx_dictionaries_node,
)
from buildtrsx.build_project import trsx_gather_nodes

account_type = {
    "CELI": [
        "CELI",
        "Compte libre d’impôt",
        "Compte d’épargne libre d’impôt",
        "TFSA",
        "Tax-Free Savings Account",
    ],
    "REER": [
        "REER",
        "Compte d’épargne-retraite",
        "Régime enregistré d’épargne retraite",
        "RRSP",
        "Registered Retirement Savings Plan",
        "Retirement Savings Plan" "RSP",  # the client uses "RSP" to refert to "RRSP"
    ],
    "REEE": [
        "REEE",
        "R trois E",
        "Compte d’épargne pour les études",
        "Régime d'épargne de mes enfants",
        "Régime enregistré d’épargne-études",
        "RESP",
        "Registered Education Savings Plan",
    ],
}

global_commands = {
    "agent": ["agent", "humain", "opérateur", "personne", "quelqu’un", "représentant"],
    "menu principal": ["menu", "menu principal", "recommencer"],
    "sortir": ["sortir"],
}
literals = {"ACCOUNT_TYPE": account_type, "COMMAND": global_commands}

dictionaries_node = trsx_dictionaries_node(entities=literals)

project_attributes = {
    "xmlns:nuance": "https://developer.nuance.com/mix/nlu/trsx",
    "xml:lang": "fra-CAN",
    "nuance:enginePackVersion": "hosted",
}

trsx = trsx_gather_nodes(
    dictionaries_node=dictionaries_node, attributes=project_attributes
)

with open("outputs/dictionaries_test.trsx", "w", encoding="utf-8") as f:
    f.write(trsx)