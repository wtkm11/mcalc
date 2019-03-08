"""
The records dataframe
"""
import pandas as pd

from mcalc.config import RECORDS

# Load the raw data records
records = pd.read_csv(RECORDS, sep=",", index_col=0)
