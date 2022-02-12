from buildtrsx.build_project import trsx_metadata_node, trsx_sources_node, trsx_project_node

# metadata node
metadata_node = trsx_metadata_node(author = "Danae Martinez",
                                   version = "1.0.0",
                                   description = "my NLU model",
                                   date = "january 2022")
print(metadata_node)

# sources node
# optional attributes for each source
source1 = {'type':"CUSTOM"}
source2 = {'uri':"http://localhost:80/my_local_dtv_domain",  'version':"1.0",  'type':"PREBUILT"}
source3 = {'uri':"http://localhost:80/ncs_ref_rejection_model", 'version':"1.0", 'type':"REJECTION"}

sources = {'IOT_Domain':source1, # key (source' name) value (optional attributes)
           'DTV_Domain':source2,
           'NCSRef_Rejection':source3,
           'My_data':None}

sources_node = trsx_sources_node(sources = sources)
print(sources_node)

project_attributes = {'xmlns:nuance':'https://developer.nuance.com/mix/nlu/trsx',
                      'xml:lang':'eng-USA', # 'fra-CAN'
                      'nuance:enginePackVersion':'hosted'}

from yattag import Doc, indent

def trsx_project_node(
    nuance_ver: str = "2.5", # Required attribute
    attributes: dict = None,
    metadata_node: str = None,
    sources_node: str = None,
) -> str:
    """Encapsulate all nodes and incorporate attributes for the project's node."""
    doc, tag, text = Doc().tagtext()
    if attributes is None:  # nuance:version is the only required attribute
        with tag("project", ("nuance:version", nuance_ver)):
            text("other nodes")
    else:
        with tag("project", ("nuance:version", nuance_ver), *attributes.items()):
            text("other nodes")
    return indent(doc.getvalue(), indentation="\t")

print(trsx_project_node(attributes = project_attributes))



#project_node = trsx_project_node(metadata_node = metadata_node)
#print(project_node)
