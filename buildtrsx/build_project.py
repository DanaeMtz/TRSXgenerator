from yattag import Doc, indent

#List of sources used to label data

def trsx_project_node(nuance_lang # "fra-CAN" or "eng-USA"
                      , nuance_ver = '2.5'
                      , nuance_xmlns = 'https://developer.nuance.com/mix/nlu/trsx'
                      , nuance_pack = "hosted" # should I use a flexible argument?
                      #, metadata_node
                      #, sources_node
                      #, ontology_node
                      #, dictionaries_node
                      #, samples_node
                      ):
    """ The project node is required for a TRSX file to be valid and for an import to proceed

    Parameters
    ----------
    nuance_ver : str
         (Default value = '2.5')
    nuance_lang :
         (Default value = 'fra-CAN'#)
    metadata_node# :
        
    sources_node# :
        
    ontology_node# :
        
    dictionaries_node# :
        
    samples_node :
        

    Returns
    -------

    """
    doc, tag, text = Doc().tagtext()
    with tag("project"
            , ('xmlns:nuance', nuance_xmlns)
            , ('xml:lang', nuance_lang)
            , ('nuance:version', nuance_ver)
            , ('nuance:enginePackVersion', nuance_pack)):
        text("metadata_node, sources_node, ontology_node, dictionaries_node, samples_node")
    return(indent(doc.getvalue(), indentation='    '))


def trsx_project_node2(attributes, nuance_ver = '2.5'):
    doc, tag, text = Doc().tagtext()
    with tag("project", ('nuance:version', nuance_ver), *attributes.items()):
        text("metadata_node, sources_node, ontology_node, dictionaries_node, samples_node")
    return (indent(doc.getvalue(), indentation='    '))

def trsx_metadata_node(**entries):
    """manage extra details about your project such as author or version.

    Parameters
    ----------

    Returns
    -------

    """
    doc, tag, text = Doc().tagtext()
    with tag("metadata"):
        for key, value in entries.items():
            with tag("entry", key=key):
                text(value)
    return(indent(doc.getvalue(), indentation = '    '))

def trsx_source_node(source):
    """

    Parameters
    ----------

    Returns
    -------

    """
    doc, tag, text = Doc().tagtext()
    doc.stag('source', *source.items())
    return(doc.getvalue())

def trsx_sources_node(sources):
    """

    Parameters
    ----------

    Returns
    -------

    """
    doc, tag, text = Doc().tagtext()
    with tag("sources"):
        for source in sources.values():
            doc.asis(trsx_source_node(source = source))
    return (indent(doc.getvalue(), indentation='    '))