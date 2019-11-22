import re

import numpy as np
import pandas as pd

from unidecode import unidecode


def remove_accents(df: pd.DataFrame, col: str) -> pd.DataFrame:
	df = df.copy()

	df[col] = df[col].map(unidecode)
	return df

def remove_punctuation(df: pd.DataFrame, col: str) -> pd.DataFrame:
	df = df.copy()

	df[col] = df[col].apply(lambda x: re.sub(r'[^\w\s]', '', x))
	return df

def to_lower(df: pd.DataFrame, col: str) -> pd.DataFrame:
	df = df.copy()

	df[col] = df[col].apply(lambda x: x.lower())
	return df

def to_upper(df: pd.DataFrame, col: str) -> pd.DataFrame:
	df = df.copy()

	df[col] = df[col].apply(lambda x: x.upper())
	return df

def to_capitalize(df: pd.DataFrame, col: str) -> pd.DataFrame:
	df = df.copy()

	df[col] = df[col].apply(lambda x: x.capitalize())
	return df

def clean_names(df: pd.DataFrame, sep: str = '_') -> pd.DataFrame:
	df = df.copy()
	clean_column_names = []

	for column_name in df.columns:
		clean_punctuation = re.sub(r'[^\w\s]', sep, column_name)
		clean_spaces = re.sub(r'\s+', sep, clean_punctuation)
		lower_text = clean_spaces.lower()

		clean_column_names.append(lower_text)

	df.columns = clean_column_names
	return df
