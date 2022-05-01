from buildtrsx.build_dictionaries.build_dict import (
    trsx_dictionaries_node,
)
from buildtrsx.build_project import trsx_gather_nodes

Banking_account = {
    "compte chèques": [
        "compte chèques",
        "compte chèque",
        "compte bancaire",
        "compte de banque" "compte courant",
        "compte progressif",
    ],
    "compte épargne": [
        "compte épargne",
        "compte d'épargne",
    ],
    "marge de crédit": ["marge de crédit"],
}

Investment_account = {
    "TFSA": [
        "celi",
        "compte libre d’impôt",
        "compte d’épargne libre d’impôt",
        "TFSA",
        "tax-free savings account",
    ],
    "RRSP": [
        "reer",
        "compte d’épargne-retraite",
        "régime enregistré d’épargne retraite",
        "RRSP",
        "registered retirement savings plan",
        "retirement savings plan",
        "RSP",  # the client uses "RSP" to refert to "RRSP"
    ],
    "RESP": [
        "reee",
        "R trois E",
        "compte d’épargne pour les études",
        "régime d'épargne de mes enfants",
        "régime enregistré d’épargne-études",
        "RESP",
        "registered education savings plan",
    ],
    "RRIF": [
        "ferr",
        "fond de revenu de retraite",
        "fonds enregistré de revenu de retraite",
        "RRIF",
        "registered retirement income funds",
    ],
    "LIRA": [
        "cri",
        "compte de retraite immobilisé",
        "lira",
        "locked-in retirement account",
    ],
    "LIF": [
        "frv",
        "fonds de revenu viager",
        "lif",
        "life income fund",
    ],
}

Global_commands = {
    "AGENT": ["agent", "humain", "opérateur", "personne", "représentant", "quelqu'un"],
    "MAIN_MENU": ["menu", "menu principal", "recommencer", "reprendre", "revenir"],
}

literals = {
    "INVESTMENT_PERSONAL": Investment_account,
    "TRANSACTIONAL_PERSONAL": Banking_account,
    "COMMAND": Global_commands,
}

dictionaries_node = trsx_dictionaries_node(entities=literals)
print(dictionaries_node)

project_attributes = {
    "xmlns:nuance": "https://developer.nuance.com/mix/nlu/trsx",
    "xml:lang": "fra-CAN",  # "eng-USA",
    "nuance:enginePackVersion": "hosted",
    "nuance:version": "2.5",
}

trsx = trsx_gather_nodes(
    dictionaries_node=dictionaries_node, attributes=project_attributes
)

with open("outputs/dictionaries_investment.trsx", "w", encoding="utf-8") as f:
    f.write(trsx)
