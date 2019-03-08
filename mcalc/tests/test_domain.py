"""
Tests domain
"""
from unittest import TestCase

import pandas as pd

from mcalc.domain.utils import extract_measure_data
from mcalc.domain.exceptions import UnknownMeasureException
from mcalc.domain.records import filter_records_by_codes, LACEScore


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


class LACEScoreTests(TestCase):
    """
    Tests of the LACEScore class
    """

    def setUp(self):
        """
        Set up test data
        """
        self.score = LACEScore([])

    """
    get_length_of_stay_lace
    """

    def test_get_length_of_stay_lace(self):
        """
        Test that the length of stay LACE points can be calculated
        """
        self.assertEqual(self.score.get_length_of_stay_lace(0), 0)
        self.assertEqual(self.score.get_length_of_stay_lace(9001), 7)
        self.assertEqual(self.score.get_length_of_stay_lace(5), 4)
        self.assertEqual(self.score.get_length_of_stay_lace(8), 5)
        self.assertEqual(self.score.get_length_of_stay_lace(1), 1)

    """
    get_ed_visits_lace
    """

    def test_ed_visits_lace(self):
        """
        Test that the ED_visitss LACE points can be calculated
        """
        self.assertEqual(self.score.get_ed_visits_lace(10), 4)
        self.assertEqual(self.score.get_ed_visits_lace(1), 1)

    def test_ed_visits_lace_raises_value_error(self):
        """
        Test that get_ed_visits_lace raises a ValueError for out of range values
        """
        with self.assertRaises(ValueError):
            self.score.get_ed_visits_lace(-1000)

    """
    count_comorbidity
    """

    def test_count_comorbidity(self):
        """
        Test that the comorbidity count can be calculated
        """
        data = [
            {
                "encounter_id": 1,
                "col1": "Yes",
                "col2": "Yes",
                "col3": "Yes"
            },
            {
                "encounter_id": 2,
                "col1": "Yes",
                "col2": "No",
                "col3": "Yes"
            },
            {
                "encounter_id": 3,
                "col1": "No",
                "col2": "No",
                "col3": "Yes"
            },
        ]
        cols = ["col1", "col2"]
        self.assertEqual(2, self.score.count_comorbidity(data[0], cols))
        self.assertEqual(1, self.score.count_comorbidity(data[1], cols))
        self.assertEqual(0, self.score.count_comorbidity(data[2], cols))

    """
    __call__
    """

    def test_calculate_lace(self):
        """
        Test that the LACE score can be calculated
        """
        self.assertEqual(
            LACEScore(["como1"])({
                "encounter_id": 1,
                "como1": "Yes",
                "LengthofStay": 0,
                "Inpatient_visits": 0,
                "ED_visits": 0,
            }),
            1
        )

    """
    get_highscore_percent
    """

    def test_get_highscore_percent(self):
        """
        Test that the highscore percentage can be calculated
        """
        lace_scores = pd.Series([1, 9001, 0, -1, 11])
        self.assertEqual(LACEScore.get_highscore_percent(lace_scores), 0.4)
