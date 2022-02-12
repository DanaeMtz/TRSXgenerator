from buildtrsx.build_project import trsx_sources_node, trsx_metadata_node

# try sources node
# optional attributes for each source
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

project_attributes = {
    "xmlns:nuance": "https://developer.nuance.com/mix/nlu/trsx",
    "xml:lang": "eng-USA",  # 'fra-CAN'
    "nuance:enginePackVersion": "hosted",
}

# call the sources node
sources_node = trsx_sources_node._original(sources=sources)
print(sources_node)

# call the wrapped sources node
wrapped_sources_node = trsx_sources_node(sources=sources, attributes=project_attributes)
print(wrapped_sources_node)

# metadata node
# call the metadata node
metadata_node = trsx_metadata_node._original(author="Danae Martinez")
print(metadata_node)

wrapped_metadata_node = trsx_metadata_node(
    author="Danae Martinez",
    version="1.0.0",
    description="my NLU model",
    date="january 2022",
    attributes=project_attributes,
)
print(wrapped_metadata_node)
