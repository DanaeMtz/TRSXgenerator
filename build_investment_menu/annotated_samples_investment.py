import build_investment_menu.semantic_signatures as ss
from buildtrsx.build_samples.build_utterances import (
    generate_utterances,
    generate_utterances_dict,
)
from buildtrsx.build_samples.build_samples import (
    trsx_annotated_literals,
    trsx_samples_node,
)
from buildtrsx.build_project import trsx_gather_nodes


def generate_annotated_utterances(
    sem_sig: list, entities: dict, sample_size: int
) -> list:
    """generate utterances form a list containing the semantic signatures."""
    ann_utt = []
    for sig in sem_sig:
        result = trsx_annotated_literals(entities=entities, samples=sig)
        sig.update(result)
        utterances = generate_utterances(sig, sample_size=sample_size)
        ann_utt += utterances
    return ann_utt


# MAKE_INVESTMENT
sem_sig = [
    ss.SS1_S1,
    ss.SS1_S2,
    ss.SS1_S3,
    ss.SS1_S4,
    ss.SS1_S5,
    ss.SS1_S6,
    ss.SS1_S7,
    ss.SS2_S1,
    ss.SS3_S1,
    ss.SS3_S2,
    ss.SS4_S1,
]

entities = {
    "TO_ACCOUNT": {"type": "isA", "conceptref": "ACCOUNT_TYPE"},
    "FROM_ACCOUNT": {"type": "isA", "conceptref": "ACCOUNT_TYPE"},
    "AMOUNT": {"type": "isA", "conceptref": "nuance_AMOUNT"},
    "ACCOUNT_TYPE": {},
}

annotated_utterances = generate_annotated_utterances(
    sem_sig=sem_sig, entities=entities, sample_size=5
)

dict_utterances = generate_utterances_dict(
    samples=annotated_utterances, samples_attr={"intentref": "MAKE_INVESTMENT"}
)

samples_node = trsx_samples_node(samples=dict_utterances)
print(samples_node)

project_attributes = {
    "xmlns:nuance": "https://developer.nuance.com/mix/nlu/trsx",
    "xml:lang": "fra-CAN",
    "nuance:enginePackVersion": "hosted",
}

trsx = trsx_gather_nodes(
    samples_node=samples_node,
    attributes=project_attributes,
)

with open("outputs/samples_test.trsx", "w", encoding="utf-8") as f:
    f.write(trsx)
