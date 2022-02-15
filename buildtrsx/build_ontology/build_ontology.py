from yattag import Doc, indent


def ontology_wrapper(func):
    """encapsulates one node at a time"""

    def wrapper(
        base_attribute="http://localhost:8080/resources/ontology-1.0.xml",
        *args,
        **kwargs
    ):
        """Encapsulate intents node and incorporate attributes for the ontology's node."""
        doc, tag, text = Doc().tagtext()
        with tag("ontology", base=base_attribute):
            doc.asis(func(*args, **kwargs))
        return indent(doc.getvalue(), indentation="\t")

    wrapper._original = func
    return wrapper


def trsx_link_node(entity: dict) -> str:
    """An intent is linked to a set of entities."""
    doc, tag, text = Doc().tagtext()
    doc.stag("link", *entity.items())
    return indent(doc.getvalue(), indentation="\t")


def trsx_links_node(entities: list):
    """generate the links node"""
    doc, tag, text = Doc().tagtext()
    for entity in entities:
        with tag("links"):
            doc.asis(trsx_link_node(entity=entity))
    return indent(doc.getvalue(), indentation="\t")

def trsx_intents_node(intents: dict) -> str:
    """Generate the intents node"""
    doc, tag, text = Doc().tagtext()
    with tag("intents"):
        for key, value in intents.items():
            if value:
                with tag("intent", name=key):
                    doc.asis(trsx_links_node(entities=value))
            else:
                doc.stag("intent", name=key)

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
                doc.stag("relation", type=entity_rel["type"], conceptref=entity)
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
            if entities[key]:
                with tag("concept", name=key):
                    doc.asis(trsx_relations_node(entity_rel=entities[key]))
            else:
                doc.stag("concept", name=key)
    return indent(doc.getvalue(), indentation="\t")


@ontology_wrapper
def trsx_gather_subnodes_ontology(**kwargs: str) -> str:
    """gather all sub nodes and put them inside the project node"""
    doc, tag, text = Doc().tagtext()
    for subnode in kwargs.values():
        doc.asis(subnode)
    return doc.getvalue()
