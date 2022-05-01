from build_investment_menu.ontology_investment import entities, project_attributes
from buildtrsx.build_samples.build_utterances import generate_utterances_dict
from buildtrsx.build_samples.build_samples import (
    trsx_samples_node,
    generate_annotated_utterances,
    parse_jsgf_output,
)
from buildtrsx.build_project import trsx_gather_nodes
import re

INTENT = "AMENDMENT"

regex_dict = {
    "INVESTMENT_PERSONAL": re.compile(r"\[([\w\s]+)\]\(INVESTMENT_PERSONAL\)"),
    "TRANSACTIONAL_PERSONAL": re.compile(r"\[([\w\s]+)\]\(TRANSACTIONAL_PERSONAL\)"),
    "AMOUNT": re.compile(r"\[([\w\s]+)\]\(AMOUNT\)"),
    "text_chunk": re.compile(r"([\w\s]+)[\[|\n]"),
}

# Generating the samples node
utt_list = parse_jsgf_output(
    filepath="build_investment_menu/jsgf_outputs/" + INTENT.lower() + ".txt",
    regex_dict=regex_dict,
)


annotated_utterances = generate_annotated_utterances(
    sem_sig=utt_list, entities=entities, sample_size=1
)

dict_utterances = generate_utterances_dict(
    samples=annotated_utterances,
    samples_attr={"intentref": INTENT, "fullyVerified": "true"},
)

samples_node = trsx_samples_node(samples=dict_utterances)

trsx = trsx_gather_nodes(
    samples_node=samples_node,
    attributes=project_attributes,
)

with open("outputs/samples_" + INTENT.lower() + ".trsx", "w", encoding="utf-8") as f:
    f.write(trsx)
