from yattag import Doc

def trsx_project(lang):
    doc, tag, text = Doc().tagtext()
    with tag("project", ('xml:lang', lang), ('nuance:version', '2.5')):
        text('rest of the sections')
    return(doc.getvalue())