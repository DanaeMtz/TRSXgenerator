import numpy as np
from functools import reduce


def _reduce_concat(x, sep=""):
    return reduce(lambda x, y: str(x) + sep + str(y), x)


def paste(*lists, sep=" ", collapse=None):
    result = map(lambda x: _reduce_concat(x, sep=sep), zip(*lists))
    if collapse is not None:
        return _reduce_concat(result, sep=collapse)
    return list(result)


Greeting_FR = [
    "je voulais",
    "je voudrais",
    "j'aimerais",
    "je veux",
    "j'appelle pour",
    "c'est pour",
    "pouvez-vous m’ aider à",
]

Greeting_EN = [
    "I wanted to",
    "I would like to",
    "I want to",
    "I'm calling",
    "I am trying to",
]

Money_expr_1_FR = ["de l'argent", "un montant", "une somme", "mes points"]
Money_expr_3_FR = ["de l'argent", "un montant", "une somme", "des fonds"]
Money_expr_2_FR = ["d'argent", "de mes points", "de fonds", "de sous"]

# Amounts = np.linspace(start=500, stop=4900, num=23, dtype=int)
# Amounts = np.linspace(start=600, stop=5000, num=23, dtype=int)
# Amounts = np.linspace(start=600, stop=6100, num=23, dtype=int)
# Amounts = np.linspace(start=500, stop=6000, num=23, dtype=int)
# Amounts = np.linspace(start=100, stop=5000, num=23, dtype=int)
Amounts = np.linspace(start=400, stop=4800, num=23, dtype=int)
dollars = np.repeat(["$"], 23)
Amounts_dollars = paste(Amounts, dollars)

Amounts_FR = [
    # "100 piasses", # change pièces
    "100 $",
    # "200 piasses",
    "20000 $",
    # "300 piasses",
    "3000 $",
    # "400 piasses",
    "4000 $",
    # "500 piasses",
    "5000 $",
]

# ACTION VERBS

# INVEST
Inv_verb_FR = [
    "acheter",
    "ajouter",
    "contribuer",
    "cotiser",
    "déplacer",  # also used for WITHDRAWAL
    "déposer",  # also used for WITHDRAWAL
    "échanger",
    "effectuer un transfert",  # also used for WITHDRAWAL
    "épargner",
    "faire de l'épargne systématique",  # SYSTEMATIC INVEST
    "programmer des virements",  # SYSTEMATIC INVEST
    "ajouter un prélèvement systématique",  # SYSTEMATIC INVEST
    "faire déposer",  # also used for WITHDRAWAL
    "faire prélever",  # SYSTEMATIC INVEST
    "faire transférer",  # also used for WITHDRAWAL
    "faire un dépôt",  # also used for WITHDRAWAL
    "faire un transfert",  # also used for WITHDRAWAL
    "faire une contribution",
    "investir",
    "mettre",  # also used for WITHDRAWAL
    "placer",
    "prendre",
    "rajouter",
    "transférer",  # also used for WITHDRAWAL
]

Inv_verb_EN = []

# WITHDRAWAL
Withd_verb_FR = [
    "déplacer",  # also used for INVEST
    "déposer",  # also used for INVEST
    "effectuer un transfert",  # also used for INVEST
    "enlever",
    "faire déposer",  # also used for INVEST
    "faire transférer",  # also used for INVEST
    "faire un dépôt",  # also used for INVEST
    "faire un retrait",
    "faire un transfert",  # also used for INVEST
    "mettre",  # also used for INVEST
    "prendre",
    "récuperer",
    "retirer",
    "retrait",
    "sortir",
    "transférer",  # also used for INVEST
    "vendre",
]

Withd_verb_EN = []

# REQUEST_BALANCE
Bal_verb_FR = ["avoir", "savoir", "vérifier"]
Bal_interrogative_clauses = ["c'est quoi", "combien", "quel est"]

Bal_verb_EN = []

# OPEN ACCOUNT
Open_verb_FR = []

Open_verb_EN = []

# CLOSE ACCOUNT
Close_verb_FR = [
    "fermer",
    "annuler",
]

# INVESTMENT ACCOUNTS (compte investissement)
Inv_account_FR = [
    "CELI",
    "compte libre d’impôt",
    "REER",
    "compte d'épargne-retraite",
    "REEE",
    "compte R trois E",
    "compte d’épargne pour les études",
    "compte épargne pour les études",
    "régime d'épargne de mes enfants",
]

Inv_expressions_FR = ["fonds mutuels", "CGP"]

# REGULAR ACCOUNTS
TRANSACTIONAL_PERSONAL_FR = [
    "compte chèques",
    "compte chèque",
    "compte bancaire",
    "compte courant",
    "compte progressif",
    "compte épargne",
    "compte d'épargne",
]

INVESTMENT_PERSONAL_FR = [
    "celi",
    "compte libre d’impôt",
    "compte d’épargne libre d’impôt",
    "reer",
    "compte d’épargne-retraite",
    "régime enregistré d’épargne retraite",
    "reee",
    "R trois E",
    "compte d’épargne pour les études",
    "régime d'épargne de mes enfants",
    "régime enregistré d’épargne-études",
    "ferr",
    "fond de revenu de retraite",
    "fonds enregistré de revenu de retraite",
    "cri",
    "compte de retraite immobilisé",
    "FRV",
    "fonds de revenu viager",
]

# for dictionaries
registered_plans = {
    "TFSA": [
        "celi",
        "compte d'épargne libre d’impôt",
        "compte libre d'impôt",
        "TFSA",
        "tax-free savings account",
    ],
    "RRSP": [
        "reer",
        "régime enregistré d’épargne retraite",
        "compte d'épargne-retraite",
        "RRSP",
        "RSP",
        "Registered Retirement Savings Plan",
    ],
    "RESP": [
        "reee",
        "régime enregistré d’épargne-études",
        "régime d'épargne de mes enfants",
        "compte d’épargne pour les études",
        "R trois E",
        "RESP",
        "Registered Education Savings Plan",
    ],
    "CPG": [
        "CPG",
        "Certificat",
        "Placement garanti",
        "GIC",
        "Guaranteed Investment Certificate",
        "Guaranteed Certificate",
        "Certificate",
    ],  # not a plan, but can be placed in a CELI or in a REER
    "FERR": [
        "ferr",
        "fonds de revenu de retraite",
        "fonds enregistré de revenu de retraite",
        "RRIF",
        "Registered Retirement Income Funds",
    ],
}

pension_plans = {
    "LIRA": [
        "CRI",
        "compte de retraite immobilisé",
        "LIRA",
        "Locked-in retirement account",
    ],
    "FRV": ["FRV", "fonds de revenu viager", "LIF", "Life Income Fund"],
}





