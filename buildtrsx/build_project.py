from yattag import Doc, indent


def trsx_metadata_node(**entries: str) -> str:
    """manage extra details about your project such as author or version."""
    doc, tag, text = Doc().tagtext()
    with tag("metadata"):
        for key, value in entries.items():
            with tag("entry", key=key):
                text(value)
    return indent(doc.getvalue(), indentation="\t")


def trsx_source_node(source: dict) -> str:
    """list sources used to label imported data."""
    doc, tag, text = Doc().tagtext()
    doc.stag("source", *source.items())
    return doc.getvalue()


def trsx_sources_node(sources: dict) -> str:
    """gather all sources of data"""
    doc, tag, text = Doc().tagtext()
    with tag("sources"):
        for source in sources.values():
            doc.asis(trsx_source_node(source=source))
    return indent(doc.getvalue(), indentation="\t")


def trsx_project_node(
    attributes: dict,
    nuance_ver: str = "2.5",
    metadata_node: str = None,
    sources_node: str = None,
    ontology_node: str = None
) -> str:
    """encapsulate all nodes"""
    doc, tag, text = Doc().tagtext()

    with tag("project", ("nuance:version", nuance_ver), *attributes.items()):
        if metadata_node is None:
            doc.asis(sources_node)
            doc.asis(ontology_node)
        if sources_node is None:
            doc.asis(metadata_node)
            doc.asis(ontology_node)
        else:
            doc.asis(sources_node)
            doc.asis(metadata_node)
            doc.asis(ontology_node)
    return indent(doc.getvalue(), indentation="\t")
