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


def generate_utterances(semantic_sig: dict) -> list:
    """store all possible formulations for one semantic signature in a list"""
    df = expand_grid(dictionary=semantic_sig)
    #print(df.head())
    return list(df.apply(concat_string, 1))


def generate_utterances_dict(samples: list, samples_attr: dict) -> dict:
    """create a dictionary with samples as keys and attributes as values"""
    samples_dict = {}
    for sample in samples:
        samples_dict[sample] = samples_attr
    return samples_dict
