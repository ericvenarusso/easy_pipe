import pytest

import pandas as pd

from easy_pipe.text.process import *


def test_remove_accents():
	df = pd.DataFrame([{'test': 'Jhóñ Dõé'}])

	df = df.pipe(remove_accents, 'test')


	assert df['test'].values[0] == 'Jhon Doe'

def test_remove_punctuation():
	df = pd.DataFrame([{'test': 'jhon@ doe!'}])

	df = df.pipe(remove_punctuation, 'test')


	assert df['test'].values[0] == 'jhon doe'

def test_to_lower():
	df = pd.DataFrame([{'test': 'Jhon Doe'}])

	df = df.pipe(to_lower, 'test')


	assert df['test'].values[0] == 'jhon doe'

def test_to_upper():
	df = pd.DataFrame([{'test': 'Jhon Doe'}])

	df = df.pipe(to_upper, 'test')


	assert df['test'].values[0] == 'JHON DOE'

def test_to_capitalize():
	df = pd.DataFrame([{'test': 'jhon doe'}])

	df = df.pipe(to_capitalize, 'test')


	assert df['test'].values[0] == 'Jhon doe'
	