"""
CLI commands
"""

import click
from mcalc.dataframes import records
from mcalc.domain.comorbidity import get_comorbidity_columns
from mcalc.domain.diagnosis_codes import get_diagnosis_codes
from mcalc.domain.records import filter_records_by_codes, LACEScore

@click.group()
def cli():
    pass

@click.command()
@click.argument("measure_name")
def lace(measure_name: str):
    """
    Calculate LACE score

    Parameters
    ----------
    measure_name : str
        The name of the measure (ex: AMI)
    """
    diagnosis_codes = get_diagnosis_codes(measure_name)
    filtered = filter_records_by_codes(records, diagnosis_codes)
    comorbidity_columns = get_comorbidity_columns(measure_name)
    lace_calculator = LACEScore(comorbidity_columns)
    lace_scores = filtered.apply(lace_calculator, axis=1)
    print(LACEScore.get_highscore_percent(lace_scores))

cli.add_command(lace)

if __name__ == "__main__":
    cli()
