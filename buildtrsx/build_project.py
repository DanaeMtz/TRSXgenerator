from yattag import Doc, indent


def project_wrapper(func):
    """ "encapsulates one node at a time"""

    def wrapper(nuance_ver: str = "2.5", attributes: dict = None, *args, **kwargs):
        """Encapsulate sources or metadata node and incorporate attributes for the project's node."""
        doc, tag, text = Doc().tagtext()
        doc.asis('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>')
        if attributes is None:
            with tag("project", ("nuance:version", nuance_ver)):
                doc.asis(func(*args, **kwargs))
                doc.stag(
                    "ontology", base="http://localhost:8080/resources/ontology-1.0.xml"
                )
        else:
            with tag("project", ("nuance:version", nuance_ver), *attributes.items()):
                doc.asis(func(*args, **kwargs))
                doc.stag(
                    "ontology", base="http://localhost:8080/resources/ontology-1.0.xml"
                )
        return indent(doc.getvalue(), indentation="\t")
    wrapper._original = func
    return wrapper


def trsx_source_node(name: str, source: dict = None) -> str:
    """List sources used to label imported data."""
    doc, tag, text = Doc().tagtext()
    if source is None:
        doc.stag("source", name=name)
    else:
        doc.stag("source", name=name, *source.items())
    return doc.getvalue()


def trsx_sources_node(sources: dict) -> str:
    """Gather all sources of data and wrap them up within the sources node."""
    doc, tag, text = Doc().tagtext()
    with tag("sources"):
        for name, source in sources.items():
            doc.asis(trsx_source_node(name=name, source=source))
    return indent(doc.getvalue(), indentation="\t")


def trsx_metadata_node(**entries: str) -> str:
    """Manage extra details about the project, such as author or
    version and encapsulate the info within the metadata node."""
    doc, tag, text = Doc().tagtext()
    with tag("metadata"):
        for key, value in entries.items():
            with tag("entry", key=key):
                text(value)
    return indent(doc.getvalue(), indentation="\t")


@project_wrapper
def trsx_gather_nodes(**kwargs: str) -> str:
    """empty project using two nodes"""
    doc, tag, text = Doc().tagtext()
    for node in kwargs.values():
        doc.asis(node)
    return doc.getvalue()
