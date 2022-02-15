from buildtrsx.build_samples.build_utterances import generate_utterances

semantic_sig1_invest = {
    "action_verb": ["take", "transfer", "withdraw"],
    "origin_prep": ["from my"],
    "origin_account": ["chequing account", "checking account", "savings account"],
    "destination_prep": ["to my", "over to my", "into my", "to put in my"],
    "destination_account": [
        "TFSA",
        "Tax-Free Savings Account",
        "CELI",
        "RRSP",
        "RSP",
        "RESP",
    ],
}
semantic_sig1_utterances = generate_utterances(dictionary=semantic_sig1_invest)
print(semantic_sig1_utterances[0])
