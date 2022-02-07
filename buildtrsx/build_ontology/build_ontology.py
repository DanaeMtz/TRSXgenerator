from yattag import Doc, indent

def trsx_ontology(intents, entities, relations):
    #TODO: add a function to create an ontology using the required XML format
    pass

def trsx_links_node(entities):
    """An intent is linked to a set of entities.
    The links node describes the entities that can
    be used in sample annotations for this intent
    """
    doc, tag, text = Doc().tagtext()
    with tag("links"):
        for entity in entities:
            doc.stag('link', conceptref = entity)
    return indent(doc.getvalue(), indentation = '    ')

def trsx_intents_node(dictionary):
    """The intents node contains the ontology intents
    """
    doc, tag, text = Doc().tagtext()
    with tag("intents"):
        for key in dictionary:
            with tag("intent", name = key):
                doc.asis(trsx_links_node(entities = dictionary[key]))
    return indent(doc.getvalue(), indentation = '    ')

def trsx_relations_node(dictionary):
    """The relations node specifies the relation between entities.
    """
    doc, tag, text = Doc().tagtext()
    with tag("relations"):
        for concept in dictionary['conceptref']:
            doc.stag('relation', type = dictionary['type'], conceptref = concept)
    return indent(doc.getvalue(), indentation = '    ')

def trsx_settings_node():
    doc, tag, text = Doc().tagtext()
    with tag("settings"):
        doc.stag('setting', name = 'isSensitive', value = "true")
    return indent(doc.getvalue(), indentation = '    ')

def trsx_entities_node(dict_ent_rels, dict_ent_types):
    """The concepts node contains the ontology entities """
    doc, tag, text = Doc().tagtext()
    with tag("concepts"):
        for key in dict_ent_types:
            with tag("concept", name = key):
                if dict_ent_types[key]['entity_type'] == 'List':
                    doc.asis(trsx_settings_node())
                else:
                    doc.asis(trsx_relations_node(dictionary = dict_ent_rels[key]))
    return indent(doc.getvalue(), indentation='    ')

