
project_attributes = {'xmlns:nuance':'https://developer.nuance.com/mix/nlu/trsx',
                      'xml:lang':'eng-USA', # 'fra-CAN'
                      'nuance:enginePackVersion':'hosted'}

from buildtrsx.build_project import trsx_source_node, trsx_sources_node
from yattag import Doc, indent

def wrap_metadata_node(func):
    def wrapper(nuance_ver: str = "2.5",  # Required attribute for the project's node
                attributes: dict = None,
                **entries):
        """Encapsulate all nodes and incorporate attributes for the project's node."""
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
            with tag("entry", key = key):
                text(value)
    return indent(doc.getvalue(), indentation="\t")

metadata_node = trsx_metadata_node(author = "Danae Martinez",
                                   version = "1.0.0",
                                   description = "my NLU model",
                                   date = "january 2022",
                                   attributes = project_attributes)



print(metadata_node)

print(trsx_metadata_node._original(author = "Danae Martinez"))