"""
The comorbidity columns dataframe
"""
import pandas as pd

from mcalc.config import COMORBIDITY

# Load the comorbidity columns
comorbidity = pd.read_csv(COMORBIDITY, sep=",", index_col=0)
