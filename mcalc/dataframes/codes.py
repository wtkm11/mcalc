"""
The diagnosis codes dataframe
"""
import pandas as pd

from mcalc.config import DIAGNOSIS_CODES

# Load the raw diagnosis_codes
diagnosis_codes = pd.read_csv(DIAGNOSIS_CODES, sep=";", index_col=0)
