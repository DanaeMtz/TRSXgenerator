from yattag import Doc, indent


def trsx_dictionary_node(entity: str, literals: dict) -> str:
    """Generate the entry node with the attributes literal and value."""
    doc, tag, text = Doc().tagtext()
    with tag("dictionary", conceptref=entity):
        for value, literal in literals.items():
            doc.stag("entry", literal=literal, value=value)
    return indent(doc.getvalue(), indentation="\t")


def trsx_dictionaries_node(entities: dict) -> str:
    """Create the dictionaries node"""
    doc, tag, text = Doc().tagtext()
    with tag("dictionaries"):
        for entity, literals in entities.items():
            doc.asis(trsx_dictionary_node(entity=entity, literals=literals))
    return indent(doc.getvalue(), indentation="\t")
