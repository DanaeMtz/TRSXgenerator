from yattag import Doc, indent


def trsx_sample_node(sample: str, sample_atr: dict) -> str:
    """generate one sample node"""
    doc, tag, text = Doc().tagtext()
    with tag("sample", *sample_atr.items()):
        text(sample)
    return doc.getvalue()


def trsx_samples_node(samples: dict) -> str:
    """generate the samples node"""
    doc, tag, text = Doc().tagtext()
    with tag("samples"):
        for key, value in samples.items():
            doc.asis(trsx_sample_node(sample=key, sample_atr=value))
    return indent(doc.getvalue(), indentation="\t")
