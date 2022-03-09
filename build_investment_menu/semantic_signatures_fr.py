# MAKE_INVESTMENT
# SS1
# TO_ACCOUNT (isA) ACCOUNT_TYPE

SS1_S1 = {  # SS1_S1 = semantic signature 1, structure 1
    "action_verb": [
        "cotiser",
        "déposer",
        "épargner",
        "faire un dépôt",
        "faire un transfert",
        "investir",
        "placer",
        "transférer",
        "programmer des virements",
        "faire de l'épargne systématique",
        "ajouter un prélèvement systématique",
    ],
    "destination_prep": ["dans mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
}

SS1_S2 = {
    "action_verb": [
        "ajouter",
        "contribuer",
        "cotiser",
        "déposer",
        "épargner",
        "investir",
        "mettre",
        "placer",
        "rajouter",
        "transférer",
    ],
    "money_expr": ["de l'argent", "un montant", "une somme", "mes points"],
    "destination_prep": ["à mon", "dans mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
}


SS1_S3 = {
    "action_verb": [
        "faire un dépôt",
        "faire un transfert",
    ],
    "money_expr": ["d'argent", "de mes points", "des fonds", "des sous"],
    "destination_prep": ["à mon", "vers mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
}


# MAKE_INVESTMENT
# SS2
# TO_ACCOUNT (isA) ACCOUNT_TYPE
# AMOUNT (isA) nuance_AMOUNT

SS2_S1 = {
    "action_verb": [
        "ajouter",
        "contribuer",
        "cotiser",
        "déposer",
        "épargner",
        "investir",
        "mettre",
        "placer",
        "rajouter",
        "transférer",
    ],
    "AMOUNT": ["200 dollars", "600 dollars", "1200 dollars", "500 piasses"],
    "destination_prep": ["à mon", "dans mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
}

SS2_S2 = {
    "action_verb": [
        "faire un dépôt de",
        "faire un transfert de",
    ],
    "AMOUNT": ["400 dollars", "900 dollars", "1700 dollars", "300 piasses"],
    "destination_prep": ["à mon", "vers mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
}

# MAKE_INVESTMENT
# SS3
# TO_ACCOUNT (isA) ACCOUNT_TYPE
# FROM_ACCOUNT (isA) ACCOUNT_TYPE

SS3_S1 = {
    "action_verb": ["prendre"],
    "origin_prep": ["de mon"],
    "FROM_ACCOUNT": [
        "compte chèques",
        "compte bancaire",
        "compte courant",
        "compte épargne",
    ],
    "destination_prep": ["pour mettre dans mon", "et de le mettre dans mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
}

SS3_S2 = {
    "action_verb": ["prendre"],
    "money_expr": ["d'argent", "de mes points", "des fonds", "des sous", "mes points"],
    "origin_prep": ["de mon"],
    "FROM_ACCOUNT": [
        "compte chèques",
        "compte bancaire",
        "compte courant",
        "compte épargne",
    ],
    "destination_prep": ["pour mettre dans mon", "et de le mettre dans mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
}

SS3_S3 = {
    "action_verb": [
        "ajouter",
        "contribuer",
        "cotiser",
        "déposer",
        "épargner",
        "investir",
        "mettre",
        "placer",
        "rajouter",
        "transférer",
    ],
    "money_expr": ["de l'argent", "un montant", "une somme"],
    "origin_prep": ["à mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
    "destination_prep": ["à partir de mon"],
    "FROM_ACCOUNT": [
        "compte chèques",
        "compte bancaire",
        "compte courant",
        "compte épargne",
    ],
}

SS3_S4 = {
    "action_verb": [
        "ajouter",
        "contribuer",
        "cotiser",
        "déposer",
        "épargner",
        "investir",
        "mettre",
        "placer",
        "rajouter",
        "transférer",
    ],
    "money_expr": ["de l'argent", "un montant", "une somme"],
    "destination_prep": ["de mon"],
    "FROM_ACCOUNT": [
        "compte chèques",
        "compte bancaire",
        "compte courant",
        "compte épargne",
    ],
    "origin_prep": ["à mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
}

# MAKE_INVESTMENT
# SS4
# TO_ACCOUNT (isA) ACCOUNT_TYPE
# FROM_ACCOUNT (isA) ACCOUNT_TYPE
# AMOUNT (isA) nuance_AMOUNT

SS4_S1 = {
    "action_verb": ["prendre"],
    "AMOUNT": ["100 dollars", "250 dollars", "500 dollars", "100 dollars", "200 piasses", "800 piasses"],
    "origin_prep": ["de mon"],
    "FROM_ACCOUNT": [
        "compte chèques",
        "compte bancaire",
        "compte courant",
        "compte épargne",
    ],
    "destination_prep": ["pour mettre dans mon", "et de le mettre dans mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
}

SS4_S2 = {
    "action_verb": [
        "ajouter",
        "contribuer",
        "cotiser",
        "déposer",
        "épargner",
        "investir",
        "mettre",
        "placer",
        "rajouter",
        "transférer",
    ],
    "AMOUNT": ["700 dollars", "2500 dollars", "3500 dollars", "2300 dollars", "600 piasses", "1700 piasses"],
    "origin_prep": ["à mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
    "destination_prep": ["à partir de mon"],
    "FROM_ACCOUNT": [
        "compte chèques",
        "compte bancaire",
        "compte courant",
        "compte épargne",
    ],
}

SS4_S3 = {
    "action_verb": [
        "ajouter",
        "contribuer",
        "cotiser",
        "déposer",
        "épargner",
        "investir",
        "mettre",
        "placer",
        "rajouter",
        "transférer",
    ],
    "AMOUNT": ["400 dollars", "4000 dollars", "2100 dollars", "3800 dollars", "300 piasses", "800 piasses"],
    "destination_prep": ["de mon"],
    "FROM_ACCOUNT": [
        "compte chèques",
        "compte bancaire",
        "compte courant",
        "compte épargne",
    ],
    "origin_prep": ["à mon"],
    "TO_ACCOUNT": [
        "CELI",
        "compte libre d’impôt",
        "REER",
        "compte d'épargne-retraite",
        "REEE",
        "compte R trois E",
        "compte d’épargne pour les études",
    ],
}
