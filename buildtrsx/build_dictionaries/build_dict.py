from yattag import Doc, indent
from typing import List, Dict
import re
from buildtrsx.utils.functions import append_new_line


def trsx_dictionary_node(entity: str, literals: dict) -> str:
    """Generate the entry node with the attributes literal and value."""
    doc, tag, text = Doc().tagtext()
    with tag("dictionary", conceptref=entity):
        for value in literals:
            for literal in literals[value]:
                doc.stag("entry", literal=literal, value=value)
    return indent(doc.getvalue(), indentation="\t")


def trsx_dictionaries_node(entities: dict) -> str:
    """Create the dictionaries node"""
    doc, tag, text = Doc().tagtext()
    with tag("dictionaries"):
        for entity, literals in entities.items():
            doc.asis(trsx_dictionary_node(entity=entity, literals=literals))
    return indent(doc.getvalue(), indentation="\t")


def parse_jsgf_dict(filepath: str) -> List[Dict[str, List[str]]]:
    """
    Parse a jsgf output composed of values and literals

    Parameters
    ----------
    filepath : str
        Filepath for file_object to be parsed

    Returns
    -------
    values_and_literals: List[Dict[str, List[str]]]
        List containing the parsed values and literals
    """

    # use https://regexper.com to visualise the regexes and https://regex101.com/ to test them
    regex_dict = {
        'LITERAL_WITH_VALUE': re.compile(r'\[([A-Za-z0-9_À-ÿ\s]+)\]\(([A-Za-z0-9_À-ÿ\s]+)\)'),
        'LITERAL': re.compile(r'(^[A-Za-z0-9_À-ÿ\s]+)'),
    }

    append_new_line(filepath)

    values_and_literals = {}

    # Open the file and read through it line by line
    with open(filepath, 'r', encoding="utf-8") as file_object:
        line = file_object.readline()
        while line:
            # try to match with the regexes
            for key, rx in regex_dict.items():
                matches = rx.finditer(line)
                if matches:
                    for match in matches:
                        if key == 'LITERAL_WITH_VALUE':
                            values_and_literals[(match.group(2)).strip()] = [(match.group(1)).strip()]
                        else:  # key == 'LITERAL' -> without canonical form
                            values_and_literals[(match.group(1)).strip()] = [(match.group(1)).strip()]

            line = file_object.readline()

    return values_and_literals