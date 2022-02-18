# MAKE_INVESTMENT
# SS1
# TO_ACCOUNT (isA) ACCOUNT_TYPE


# structure 1
SS1_S1 = {  # SS1_S1 = semantic signature 1, structure 1
    "action_verb": [
        "contribute",
        "make a contribution",
        "make a transfer",
        "make contribution",
    ],
    "destination_prep": ["to my"],
    "TO_ACCOUNT": ["TFSA", "Tax-Free Savings Account", "CELI", "RRSP", "RSP", "RESP"],
}
# structure 2
SS1_S2 = {
    "action_verb": ["periodic purchase", "recurring purchase"],
    "destination_prep": ["for my"],
    "TO_ACCOUNT": ["TFSA", "Tax-Free Savings Account", "CELI", "RRSP", "RSP", "RESP"],
}
# structure 3
SS1_S3 = {
    "action_verb": ["buy"],
    "destination_prep": ["funds from my", "a GIC from my"],
    "TO_ACCOUNT": ["TFSA", "Tax-Free Savings Account", "CELI", "RRSP", "RSP", "RESP"],
}
# structure 4
SS1_S4 = {
    "action_verb": ["invest"],
    "destination_prep": ["in my"],
    "TO_ACCOUNT": ["TFSA", "Tax-Free Savings Account", "CELI", "RRSP", "RSP", "RESP"],
}
# structure 5
SS1_S5 = {
    "action_verb": ["transfer", "take"],
    "money_expr": ["money", "some money", "funds", "the funds"],
    "destination_prep": ["to my", "over to my", "into my", "to put in my"],
    "TO_ACCOUNT": ["TFSA", "Tax-Free Savings Account", "CELI", "RRSP", "RSP", "RESP"],
}
# structure 6
SS1_S6 = {
    "action_verb": ["convert", "trade", "use"],
    "money_expr": ["my points"],
    "destination_prep": ["to add to my"],
    "TO_ACCOUNT": ["TFSA", "Tax-Free Savings Account", "CELI", "RRSP", "RSP", "RESP"],
}

# structure 7
SS1_S7 = {
    "action_verb": ["forward", "trade", "convert"],
    "money_expr": ["my points"],
    "destination_prep": ["towards", "for"],
    "TO_ACCOUNT": ["TFSA", "Tax-Free Savings Account", "CELI", "RRSP", "RSP", "RESP"],
}

# MAKE_INVESTMENT
# SS2
# TO_ACCOUNT (isA) ACCOUNT_TYPE
# AMOUNT (isA) nuance_AMOUNT

SS2_S1 = {
    "action_verb": ["transfer", "take"],
    "AMOUNT": ["500 dollars", "500 bucks"],
    "destination_prep": ["to my", "over to my", "into my", "to put in my"],
    "TO_ACCOUNT": ["TFSA", "Tax-Free Savings Account", "CELI", "RRSP", "RSP", "RESP"],
}

# MAKE_INVESTMENT
# SS3
# TO_ACCOUNT (isA) ACCOUNT_TYPE
# FROM_ACCOUNT (isA) ACCOUNT_TYPE

SS3_S1 = {
    "action_verb": ["take", "transfer", "withdraw"],
    "origin_prep": ["from my"],
    "FROM_ACCOUNT": ["chequing account", "checking account", "savings account"],
    "destination_prep": ["to my", "over to my", "into my", "to put in my"],
    "TO_ACCOUNT": ["TFSA", "Tax-Free Savings Account", "CELI", "RRSP", "RSP", "RESP"],
}

SS3_S2 = {
    "action_verb": ["take", "transfer", "withdraw"],
    "money_expr": ["money", "some money", "funds", "the funds"],
    "origin_prep": ["from my"],
    "FROM_ACCOUNT": ["chequing account", "checking account", "savings account"],
    "destination_prep": ["to my", "over to my", "into my", "to put in my"],
    "TO_ACCOUNT": ["TFSA", "Tax-Free Savings Account", "CELI", "RRSP", "RSP", "RESP"],
}

# MAKE_INVESTMENT
# SS4
# TO_ACCOUNT (isA) ACCOUNT_TYPE
# FROM_ACCOUNT (isA) ACCOUNT_TYPE
# AMOUNT (isA) nuance_AMOUNT

SS4_S1 = {
    "action_verb": ["take", "transfer", "withdraw"],
    "AMOUNT": ["500 dollars", "500 bucks"],
    "origin_prep": ["from my"],
    "FROM_ACCOUNT": ["chequing account", "checking account", "savings account"],
    "destination_prep": ["to my", "over to my", "into my", "to put in my"],
    "TO_ACCOUNT": ["TFSA", "Tax-Free Savings Account", "CELI", "RRSP", "RSP", "RESP"],
}
