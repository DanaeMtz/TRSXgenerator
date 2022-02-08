from yattag import Doc, indent

def trsx_links_node(entities):
    """An intent is linked to a set of entities.
    The links node describes the entities that can
    be used in sample annotations for this intent

    Parameters
    ----------
    entities : list
        A list of the entities linked to a given intent


    Returns
    The correponding Links node in XML format

    """
    doc, tag, text = Doc().tagtext()
    with tag("links"):
        for entity in entities:
            doc.stag('link', conceptref = entity)
    return indent(doc.getvalue(), indentation = '    ')

def trsx_intents_node(int_ent_dict):
    """The intents node contains the ontology intents

    Parameters
    ----------
    dictionary : dict
        Dictionary containing Intent(keys)-entity(values as list) links


    Returns
    -------

    """
    doc, tag, text = Doc().tagtext()
    with tag("intents"):
        for key in int_ent_dict:
            if int_ent_dict[key]:
                with tag("intent", name=key):
                    doc.asis(trsx_links_node(entities = int_ent_dict[key]))
            else:
                doc.stag('intent', name=key)
    return indent(doc.getvalue(), indentation = '    ')


def trsx_relations_node(rel_dict):
    """The relations node specifies the relation between entities.

    Parameters
    ----------
    rel_dict : dict
        dictionary of the relationships between entities


    Returns
    -------
    The correponding relations node in XML format
    """
    doc, tag, text = Doc().tagtext()
    with tag("relations"):
        if rel_dict['type'] == 'isA': # The relation node cannot contain two isA relations.
            doc.stag('relation', type = rel_dict['type'], conceptref = rel_dict['conceptref'])
        else:
            for entity in rel_dict['conceptref']:
                doc.stag('relation', type = rel_dict['type'], conceptref = entity)
    return indent(doc.getvalue(), indentation = '    ')

def trsx_settings_node():
    #TODO: undestand the function of this node
    doc, tag, text = Doc().tagtext()
    with tag("settings"):
        doc.stag('setting', name = 'isSensitive', value = "true")
    return indent(doc.getvalue(), indentation = '    ')

def trsx_entities_node(rel_typ_dict):
    """The concepts node contains the ontology entities

    Parameters
    ----------
    rel_typ_dict : dict


    Returns
    -------
    The correponding concepts node in XML format

    """
    doc, tag, text = Doc().tagtext()
    with tag("concepts"):
        for key in rel_typ_dict:
            with tag("concept", name = key):
                if rel_typ_dict[key]['entity_type'] == 'List':
                    doc.asis(trsx_settings_node())
                else:
                    doc.asis(trsx_relations_node(rel_dict = rel_typ_dict[key]))
    return indent(doc.getvalue(), indentation='    ')


def trsx_ontology(intents, entities, relations):
    """

    Parameters
    ----------
    intents :

    entities :

    relations :


    Returns
    -------

    """
    #TODO: add a function to create an ontology using the required XML format
    pass
