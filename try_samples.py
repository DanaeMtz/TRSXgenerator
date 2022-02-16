from buildtrsx.build_samples.build_samples import trsx_sample_node, trsx_samples_node
from buildtrsx.build_samples.build_utterances import generate_utterances, generate_utterances_dict

# example of one semantic signature
sem_sig1 = {
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

sem_sig1_samples = generate_utterances(semantic_sig=sem_sig1)
sample_atr = {"intentref": "MAKE_INVESTMENT", "count": "1", "excluded": "false"}
samples_sem_sig1 = generate_utterances_dict(samples = sem_sig1_samples, samples_attr = sample_atr)
print(trsx_samples_node(samples=samples_sem_sig1))