from buildtrsx.build_project import (
    trsx_sources_node,
    trsx_metadata_node,
    trsx_gather_nodes,
)

# metadata node
metadata_node = trsx_metadata_node(
    author="Danae Martinez",
    version="1.0.0",
    description="my NLU model",
    date="february 2022",
)
print(metadata_node)

# sources node
sources_nlu = {"My_data": {"type": "CUSTOM"}, "Prod_data": {"type": "VERINT"}}

sources_node = trsx_sources_node(sources=sources_nlu)
print(sources_node)

# example 2: optional attributes for each source
source1 = {"type": "CUSTOM"}
source2 = {
    "uri": "http://localhost:80/my_local_dtv_domain",
    "version": "1.0",
    "type": "PREBUILT",
}
source3 = {
    "uri": "http://localhost:80/ncs_ref_rejection_model",
    "version": "1.0",
    "type": "REJECTION",
}
source4 = {
    "displayName": "nuance_custom_data",
    "version": "1.0",
    "type": "CUSTOM",
    "useForOOV": "true",
}
sources = {
    "IOT_Domain": source1,  # key (source' name) value (optional attributes)
    "DTV_Domain": source2,
    "NCSRef_Rejection": source3,
    "My_data": None,
    "nuance_custom_data": source4,
}

sources_node2 = trsx_sources_node(sources=sources)
print(sources_node2)

# example 3: empty project
empty_project = trsx_sources_node(sources={"nuance_custom_data": source4})
print(empty_project)

# wrapped nodes
project_attributes = {
    "xmlns:nuance": "https://developer.nuance.com/mix/nlu/trsx",
    "xml:lang": "eng-USA",  # 'fra-CAN'
    "nuance:enginePackVersion": "hosted",
}

print(
    trsx_gather_nodes(
        metadata_node=metadata_node,
        sources_node=sources_node,
        attributes=project_attributes,
    )
)
