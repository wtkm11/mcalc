"""
Utilities
"""
from typing import List

import pandas as pd

from mcalc.domain.exceptions import UnknownMeasureException


def extract_measure_data(
        measure_name: str,
        dataframe: pd.DataFrame,
        data_column_name: str
) -> List[str]:
    """
    Extract data related to a measure

    Parameters
    ----------
    measure_name : str
        The name of the measure
    dataframe : str
        The dataframe from which to extract data
    data_column_name : str
        The name of the column in which measure-related data is stored

    Returns
    -------
    List[str]
        A list of data related to the measure (ex: diagnosis codes or
        comorbidity column names)

    Raises
    ------
    UnknownMeasureException
        If the measure name is found in the table
    """
    try:
        row = dataframe.loc[measure_name]
    except KeyError:
        raise UnknownMeasureException(
            "'{name}' is unknown".format(name=measure_name)
        )
    return [
        code.strip()
        for code in row[data_column_name].split(",")
    ]
