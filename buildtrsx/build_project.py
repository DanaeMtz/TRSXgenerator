from yattag import Doc, indent

#List of sources used to label data

def trsx_project_node(nuance_ver = '2.5'
                      , nuance_lang = 'fra-CAN'
                      #, metadata_node
                      #, sources_node
                      #, ontology_node
                      #, dictionaries_node
                      #, samples_node
                      ):
    doc, tag, text = Doc().tagtext()
    with tag("project", ('xml:lang', nuance_lang), ('nuance:version', nuance_ver)):
        text("some content")
    return(doc.getvalue())

def trsx_metadata_node(str
                    #, entry
                       ):
    doc, tag, text = Doc().tagtext()
    with tag("metadata"):
        with tag("entry", key=str):
            text(str)
    return(indent(doc.getvalue(), indentation = '    '))

def trsx_sources_node(source_name ="name"
                      , source_uri = "uri"
                      , source_version = "string"
                      , source_type = "type"):
    doc, tag, text = Doc().tagtext()
    with tag("sources"):
        doc.stag("source", name = source_name, uri = source_uri, version = source_version, type = source_type)
    return(indent(doc.getvalue(), indentation = '    '))

