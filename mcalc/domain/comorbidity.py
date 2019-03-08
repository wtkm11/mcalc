"""
Comorbidity domain logic
"""
from typing import List
import pandas as pd

from mcalc.dataframes import comorbidity
from mcalc.domain.utils import extract_measure_data


def get_comorbidity_columns(measure_name: str) -> List[str]:
    """
    Get comorbidity columns for a given measure

    Parameters
    ----------
    measure_name : str
        The name of the measure

    Returns
    -------
    List[str]
        A list of comorbidity columns
    """
    return extract_measure_data(
        measure_name, comorbidity, "Comorbidity Columns"
    )
