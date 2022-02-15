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


def generate_utterances(dictionary):
    """store all possible formulations in a list"""
    df = expand_grid(dictionary=dictionary)
    return list(df.apply(concat_string, 1))
