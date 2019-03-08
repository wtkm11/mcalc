"""
Records domain logic
"""
from typing import Dict, List
import pandas as pd

from mcalc.domain.comorbidity import get_comorbidity_columns


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


class LACEScore:
    """
    Calculate LACE scores
    """

    def __init__(self, comorbidity_columns: str):
        self.comorbidity_columns = comorbidity_columns

    def __call__(self, row: Dict):
        """
        Calculate the LACE score for a row

        Parameters
        ----------
        row : Dict
            A dictionary-like representation of the data in a row

        Returns
        -------
        int
            The LACE score
        """
        return (
            # Length of Stay
            self.get_length_of_stay_lace(row["LengthofStay"]) +
            # Acute Admissions
            # 3 if row["EmergencyAdmission"] == "Yes" else 0 +
            # Comorbidity
            self.count_comorbidity(row, self.comorbidity_columns) +
            # ED visits
            self.get_ed_visits_lace(row["ED_visits"])
        )

    def get_length_of_stay_lace(self, value: int) -> int:
        """
        Determine the length of stay LACE point value

        Parameters
        ----------
        value : int
            The length of stay for the patient

        Returns
        -------
        int
            The number of LACE points to assign
        """
        if value < 1:
            return 0
        if value >= 14:
            return 7
        if 4 <= value <= 6:
            return 4
        if 7 <= value <= 13:
            return 5
        return value

    def get_ed_visits_lace(self, value: int) -> int:
        """
        Determine the ED Visits LACE point value

        Parameters
        ----------
        value : int
            The number of ED visits for the patient

        Returns
        -------
        int
            The number of LACE points to assign

        Raises
        ------
        ValueError
            If the visit count is less than zero
        """
        if value >= 4:
            return 4
        if value < 0:
            raise ValueError("LACE points undefined")
        return value

    def count_comorbidity(self, row: Dict, columns: List[str]) -> int:
        """
        Count up "Yes" values in selected comorbidity columns

        Parameters
        ----------
        row : Dict
            A dictionary-like representation of the data in a row
        columns : List[str]
            A list of names of columns to include in the calculation

        Returns
        -------
        int
            The comorbidity score
        """
        return sum(row[col] == "Yes" for col in columns)

    @staticmethod
    def get_highscore_percent(scores: pd.Series) -> float:
        """
        Get the percentage of highscore (> 9) records

        Parameters
        ----------
        scores : pandas.Series
            A data series of calculated LACE scores

        Returns
        -------
        float
            The percentage of records that achieved high scores
        """
        return float(sum(scores > 9)) / len(scores)
