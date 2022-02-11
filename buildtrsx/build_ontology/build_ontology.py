from yattag import Doc, indent


def trsx_link_node(entity: dict) -> str:
    """An intent is linked to a set of entities."""
    doc, tag, text = Doc().tagtext()
    doc.stag("link", *entity.items())
    return indent(doc.getvalue(), indentation="\t")


def trsx_intents_node(intents: dict) -> str:
    """Generate the intents node"""
    doc, tag, text = Doc().tagtext()
    with tag("intents"):
        for key, value in intents.items():
            if value:
                with tag("intent", name = key):
                    with tag("links"):
                        for subdict in value:
                            doc.asis(trsx_link_node(entity = subdict))
            else:
                doc.stag("intent", name = key)

    return indent(doc.getvalue(), indentation="\t")


def trsx_relations_node(entity_rel: dict) -> str:
    """The relations node specifies the relation between entities"""
    doc, tag, text = Doc().tagtext()
    with tag("relations"):
        if (
            entity_rel["type"] == "isA"
        ):  # The relation node cannot contain two isA relations.
            doc.stag("relation", *entity_rel.items())
        else:
            for entity in entity_rel["conceptref"]:
                doc.stag("relation", type = entity_rel["type"], conceptref = entity)
    return indent(doc.getvalue(), indentation="\t")


def trsx_settings_node(setting: dict) -> str:
    """TODO: investigate when is this node necessary"""
    doc, tag, text = Doc().tagtext()
    with tag("settings"):
        doc.stag("setting", *setting.items())
    return indent(doc.getvalue(), indentation="\t")


def trsx_concepts_node(entities: dict) -> str:
    """TODO: incorporate the setting and regex node when appropriate"""
    doc, tag, text = Doc().tagtext()
    with tag("concepts"):
        for key in entities:
            with tag("concept", name=key):
                doc.asis(trsx_relations_node(entity_rel=entities[key]))
    return indent(doc.getvalue(), indentation="\t")


def trsx_ontology_node(
    base_attribute = "http://localhost:8080/resources/ontology-1.0.xml",
    intents_node: str = None,
    concepts_node: str = None,
) -> str:
    """create an ontology using the required XML format"""
    doc, tag, text = Doc().tagtext()
    with tag("ontology", base=base_attribute):
        if intents_node is None:
            doc.asis(concepts_node)
        if concepts_node is None:
            doc.asis(intents_node)
        else:
            doc.asis(concepts_node)
            doc.asis(intents_node)
    return indent(doc.getvalue(), indentation="\t")
