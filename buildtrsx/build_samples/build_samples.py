from yattag import Doc, indent


def trsx_sample_node(sample: str, sample_atr: dict) -> str:
    """generate the sample node"""
    doc, tag, text = Doc().tagtext()
    with tag("sample", *sample_atr.items()):
        doc.asis(sample)
    return doc.getvalue()


def trsx_samples_node(samples: dict) -> str:
    """generate the samples node"""
    doc, tag, text = Doc().tagtext()
    with tag("samples"):
        for key, value in samples.items():
            doc.asis(trsx_sample_node(sample=key, sample_atr=value))
    return indent(doc.getvalue(), indentation="\t")


def trsx_annotation_node(entity: str, literal: str) -> str:
    """generate the annotations for the augmented data"""
    doc, tag, text = Doc().tagtext()
    with tag("annotation", conceptref=entity):
        text(literal)
    return indent(doc.getvalue(), indentation="\t")


def trsx_annotated_literals(entities: dict, samples: dict) -> dict:
    """stock annotated literals in a dictionary
    Args:
        entities: dictionary containing the relationships between entities
        samples: dictionary containing the literals to the entities possessing a relationship
    Returns:
        result: dictionary containing the annotated literals with its corresponding labels
    """
    nodes = list()
    result = dict()
    for entity, relation in entities.items():
        if entity in samples.keys() and relation["type"] == "isA":
            for literal in samples[entity]:
                doc, tag, text = Doc().tagtext()
                with tag("annotation", conceptref=entity):
                    doc.asis(
                        trsx_annotation_node(
                            entity=relation["conceptref"], literal=literal
                        )
                    )
                annotation_node = indent(doc.getvalue(), indentation="\t")
                nodes += [(entity, annotation_node)]
    # put the annotation nodes in a dictionary, entity as a key
    for key, value in nodes:
        result.setdefault(key, []).append(value)

    return result
