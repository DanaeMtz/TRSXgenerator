from itertools import product
import pandas as pd


def expand_grid(dictionary):
    """generate all possible formulations for a given semantic signature"""
    return pd.DataFrame(
        [row for row in product(*dictionary.values())], columns=dictionary.keys()
    )


def concat_string(row):
    """paste all string columns from one row"""
    return " ".join(row)

def generate_utterances_df(semantic_sig: dict):
    """store all possible formulations for one semantic signature in a list"""
    df = expand_grid(dictionary=semantic_sig)
    return df.apply(concat_string, 1)


def generate_utterances(semantic_sig: dict, sample_size: int) -> list:
    """store all possible formulations for one semantic signature in a list"""
    df = expand_grid(dictionary=semantic_sig)
    if len(df.index) < sample_size:
        df = df.sample(n=sample_size, replace=True)
    else:
        df = df.sample(n=sample_size)
    return list(df.apply(concat_string, 1))


def generate_utterances_dict(samples: list, samples_attr: dict) -> dict:
    """create a dictionary with samples as keys and attributes as values"""
    samples_dict = {}
    for sample in samples:
        samples_dict[sample] = samples_attr
    return samples_dict
