from yattag import Doc, indent

def trsx_dictionary(dictionary):
    """Generate the entry node with the attributes literal and value.

    Parameters
    ----------
    dictionary : dict
    dictionary associated to a List entity

    Returns
    -------
    XML file
    """
    doc, tag, text = Doc().tagtext()
    with tag("dictionary", conceptref="ACCOUNT_TYPE"):
        for key in dictionary:
            for value in dictionary[key]:
                doc.stag('entry', literal=value, value=key)
    return indent(doc.getvalue(), indentation = '    ')