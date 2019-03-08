"""
Tests domain
"""
from unittest import TestCase

import pandas as pd

from mcalc.domain.utils import extract_measure_data
from mcalc.domain.exceptions import UnknownMeasureException
from mcalc.domain.records import filter_records_by_codes


class ExtractMeasureDataTests(TestCase):
    """
    Tests of extract_measure_data function
    """

    def setUp(self):
        """
        Set up test data
        """
        self.data = pd.DataFrame(
            index=["ABC", "BCD", "CDE"],
            data={
                "Diagnosis codes": [
                    "code 1, code red, code fish",
                    "code 5, code green, code turtle",
                    "code 12, code blue, code snake",
                ],
            }
        )

    def test_returns_diagnosis_codes(self):
        """
        Test that a list of diagnosis codes is returned
        """
        codes = extract_measure_data("BCD", self.data, "Diagnosis codes")
        self.assertTrue(isinstance(codes, list))

    def test_raises_exception_if_measure_unknown(self):
        """
        Test that an exception is raised if the measure is unknown
        """
        with self.assertRaises(UnknownMeasureException):
            extract_measure_data("???", self.data, "Diagnosis codes")


class FilterRecordsByCodesTests(TestCase):
    """
    Tests of filter_records_by_codes function
    """

    def test_returns_filtered_dataframe(self):
        """
        Test that a filtered DataFrame is returned
        """
        dcs = ["EXPECTED_1", "EXPECTED_2"]
        data = pd.DataFrame({
            "encounter_id": [6, 5, 8],
            "diagnosis_code": ["EXPECTED_2", "UNEXPECTED", "EXPECTED_1"],
        })
        filtered = filter_records_by_codes(data, dcs)
        self.assertTrue(isinstance(filtered, pd.DataFrame))
        self.assertFalse(any(filtered.diagnosis_code.isin(["UNEXPECTED"])))
