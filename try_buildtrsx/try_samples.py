from buildtrsx.build_samples.build_samples import (
    trsx_annotated_literals,
    trsx_samples_node,
)
from buildtrsx.build_samples.build_utterances import (
    generate_utterances,
    generate_utterances_dict,
)

samples = {
    "action_verb": ["take", "transfer", "withdraw"],
    "origin_prep": ["from my"],
    "FROM_ACCOUNT": ["checking account", "savings account"],
    "destination_prep": ["to my", "over to my", "into my", "to put in my"],
    "TO_ACCOUNT": [
        "TFSA",
        "Tax-Free Savings Account",
        "CELI",
        "RRSP",
        "RSP",
        "RESP",
    ],
}

# in order to annotate the utterances correctly, we need to know the relations
entities = {
    "TO_ACCOUNT": {"type": "isA", "conceptref": "ACCOUNT_TYPE"},
    "FROM_ACCOUNT": {"type": "isA", "conceptref": "ACCOUNT_TYPE"},
    "AMOUNT": {"type": "isA", "conceptref": "nuance_AMOUNT"},
    "ACCOUNT_TYPE": {},
}

# generate all possible utterances from one specific semantic signature
utterances = generate_utterances(samples, sample_size=5)
print(utterances)

samples_ann = trsx_annotated_literals(entities=entities, samples=samples)
samples.update(samples_ann)

annotated_utterances = generate_utterances(samples, sample_size=5)

dict_utterances = generate_utterances_dict(
    samples=annotated_utterances,
    # samples=utterances,
    samples_attr={"intentref": "MAKE_INVESTMENT"}
)

samples_node = trsx_samples_node(samples=dict_utterances)
print(samples_node)
