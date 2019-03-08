"""
Diagnosis code domain logic
"""
from typing import List

from mcalc.dataframes import diagnosis_codes
from mcalc.domain.utils import extract_measure_data


def get_diagnosis_codes(measure_name: str) -> List[str]:
    """
    Get diagnosis codes for a measure name

    Parameters
    ----------
    measure_name : str
        The name of the measure

    Returns
    -------
    List[str]
        A list of diagnosis codes
    """
    return extract_measure_data(
        measure_name, diagnosis_codes, "Diagnosis Codes"
    )
