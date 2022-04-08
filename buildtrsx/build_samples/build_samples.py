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
        if (entity in samples.keys()) and (len(relation) != 0 and relation["type"] == "isA"):
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
        elif (entity in samples.keys()) and (len(relation) == 0):
            print(entity)
            for literal in samples[entity]:
                doc, tag, text = Doc().tagtext()
                doc.asis(trsx_annotation_node(entity=entity, literal=literal))
                nodes += [(entity, doc.getvalue())]
    # put the annotation nodes in a dictionary, entity as a key
    for key, value in nodes:
        result.setdefault(key, []).append(value)

    return result


def generate_annotated_utterances(
    sem_sig: list, entities: dict, sample_size: int
) -> list:
    """Generate utterances from a list containing the semantic signatures."""
    ann_utt = []
    for sig in sem_sig:
        result = trsx_annotated_literals(entities=entities, samples=sig)
        sig.update(result)
        utterances = generate_utterances(sig, sample_size=sample_size)
        ann_utt += utterances
    return ann_utt