"""
Tests domain
"""
from unittest import TestCase

from mcalc.domain.diagnosis_codes import (
    get_diagnosis_codes, UnknownMeasureException
)


class GetDiagnosisCodesTests(TestCase):
    """
    Tests of get_diagnosis_codes function
    """

    def test_returns_diagnosis_codes(self):
        """
        Test that a list of diagnosis codes is returned
        """
        self.assertTrue(isinstance(get_diagnosis_codes("AMI"), list))

    def test_raises_exception_if_measure_unknown(self):
        """
        Test that an exception is raised if the measure is unknown
        """
        with self.assertRaises(UnknownMeasureException):
            get_diagnosis_codes("???")
