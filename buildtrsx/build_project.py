from yattag import Doc, indent


def trsx_metadata_node(**entries: str) -> str:
    """Manage extra details about the project, such as author or
    version and encapsulate the info within the metadata node."""
    doc, tag, text = Doc().tagtext()
    with tag("metadata"):
        for key, value in entries.items():
            with tag("entry", key = key):
                text(value)
    return indent(doc.getvalue(), indentation="\t")


def trsx_source_node(name: str, # Required attribute of the source node
                     source: dict = None # Optional attributes of the source node
                     ) -> str:
    """List sources used to label imported data."""
    doc, tag, text = Doc().tagtext()
    if source is None:
        doc.stag("source", name = name)
    else:
        doc.stag("source", name = name, *source.items())
    return doc.getvalue()


def trsx_sources_node(sources: dict) -> str:
    """Gather all sources of data and wrap them within the sources node."""
    doc, tag, text = Doc().tagtext()
    with tag("sources"):
        for name, source in sources.items():
            doc.asis(trsx_source_node(name = name, source = source))
    return indent(doc.getvalue(), indentation="\t")


def trsx_project_node(
    nuance_ver: str = "2.5", # Required attribute
    attributes: dict = None,
    metadata_node: str = None,
    sources_node: str = None,
    ontology_node: str = None,
    dictionaries_node: str = None,
    samples_node: str = None
) -> str:
    """Encapsulate all nodes and incorporate attributes for the project's node."""
    doc, tag, text = Doc().tagtext()
    if attributes is None:  # nuance:version is the only required attribute
        with tag("project", ("nuance:version", nuance_ver)):
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
    else:
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
