"""
Diagnosis code domain logic
"""
from typing import List

from mcalc.dataframes import diagnosis_codes


class UnknownMeasureException(Exception):
    """ An exception to raise if the measure is unknown """


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
    try:
        codes = diagnosis_codes.loc[measure_name]["Diagnosis Codes"].split(",")
    except KeyError:
        raise UnknownMeasureException(
            "'{name}' is unknown".format(name=measure_name)
        )
    else:
        return [
            code.strip()
            for code in codes
        ]
