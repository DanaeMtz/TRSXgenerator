import pandas as pd
from typing import List, Dict
import os


def df2dict(df: pd.DataFrame) -> Dict[str, List[str]]:

	utt_dict: Dict[str, List[str]] = {}

	for index, row in df.iterrows():
		cmd = row['Command']
		if cmd.islower():  # this is not a pre-defined entity, but a chunk of text
			cmd = cmd + "_" + str(index)  # adds the index, as we can have multiple chunks of text in a same utt
		utt_dict[cmd] = [row['Value']]

	return utt_dict


def append_new_line(filepath):
	"""
	Append '\n' at the EOF to make sure the regexes work with the last line of text
	"""

	file_size = os.stat(filepath).st_size

	with open(filepath, 'rb') as f:
		f.seek(-1, os.SEEK_END)
		last_char = f.read(1)

	if file_size > 0 and last_char != b'\n':
		with open(filepath, "a") as file_object:
			file_object.write("\n")
