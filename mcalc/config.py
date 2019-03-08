"""
Configuration settings
"""
from pkg_resources import resource_filename

# File paths
DIAGNOSIS_CODES = resource_filename('mcalc.data', "diagnosis_codes.csv")
RECORDS = resource_filename("mcalc.data", "Sample Data 2016.csv")
COMORBIDITY = resource_filename('mcalc.data', "comorbidity_columns.csv")
