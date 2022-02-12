from yattag import Doc, indent


def wrap_metadata_node(func):
    def wrapper(
        nuance_ver: str = "2.5",  # Required attribute for the project's node
        attributes: dict = None,
        **entries
    ):
        """Encapsulate the metadata node and incorporate attributes for the project's node."""
        doc, tag, text = Doc().tagtext()
        if attributes is None:
            with tag("project", ("nuance:version", nuance_ver)):
                doc.asis(func(**entries))
        else:
            with tag("project", ("nuance:version", nuance_ver), *attributes.items()):
                doc.asis(func(**entries))
        return indent(doc.getvalue(), indentation="\t")

    wrapper._original = func
    return wrapper


@wrap_metadata_node
def trsx_metadata_node(**entries: str) -> str:
    """Manage extra details about the project, such as author or
    version and encapsulate the info within the metadata node."""
    doc, tag, text = Doc().tagtext()
    with tag("metadata"):
        for key, value in entries.items():
            with tag("entry", key=key):
                text(value)
    return indent(doc.getvalue(), indentation="\t")


def trsx_source_node(
    name: str,  # Required attribute of the source node
    source: dict = None,  # Optional attributes of the source node
) -> str:
    """List sources used to label imported data."""
    doc, tag, text = Doc().tagtext()
    if source is None:
        doc.stag("source", name=name)
    else:
        doc.stag("source", name=name, *source.items())
    return doc.getvalue()


def wrap_sources_node(func):
    def wrapper(
        sources,
        nuance_ver: str = "2.5",  # Required attribute for the project's node
        attributes: dict = None,
    ):
        """Encapsulate sources node and incorporate attributes for the project's node."""
        doc, tag, text = Doc().tagtext()
        if attributes is None:
            with tag("project", ("nuance:version", nuance_ver)):
                doc.asis(func(sources))
        else:
            with tag("project", ("nuance:version", nuance_ver), *attributes.items()):
                doc.asis(func(sources))
        return indent(doc.getvalue(), indentation="\t")

    wrapper._original = func
    return wrapper


@wrap_sources_node
def trsx_sources_node(sources: dict) -> str:
    """Gather all sources of data and wrap them up within the sources node."""
    doc, tag, text = Doc().tagtext()
    with tag("sources"):
        for name, source in sources.items():
            doc.asis(trsx_source_node(name=name, source=source))
    return indent(doc.getvalue(), indentation="\t")


def trsx_project_node(
    nuance_ver: str = "2.5",  # Required attribute
    attributes: dict = None,
    metadata_node: str = None,
    sources_node: str = None,
    ontology_node: str = None,
    dictionaries_node: str = None,
    samples_node: str = None,
) -> str:
    """Encapsulate all nodes and incorporate attributes for the project's node."""
    doc, tag, text = Doc().tagtext()
    if attributes is None:  # nuance:version is the only required attribute
        with tag("project", ("nuance:version", nuance_ver)):
            text("rest of optional nodes")
    else:
        with tag("project", ("nuance:version", nuance_ver), *attributes.items()):
            text("rest of optional nodes")
    return indent(doc.getvalue(), indentation="\t")
