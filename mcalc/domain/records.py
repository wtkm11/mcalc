"""
Records domain logic
"""
from typing import List
import pandas as pd

from mcalc.dataframes import records

def filter_records_by_codes(
        records: pd.DataFrame,
        codes: List[str]
) -> pd.DataFrame:
    """
    Get records with selected diagnosis codes

    Parameters
    ----------
    records : pandas.DataFrame
        A dataframe of records to filter

    Returns
    -------
    pandas.DataFrame
        The filtered dataframe
    """
    return records[records.diagnosis_code.isin(codes)]
