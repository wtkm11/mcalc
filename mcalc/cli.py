"""
CLI commands
"""

import click

@click.group()
def cli():
    pass

@click.command()
@click.argument("measure_name")
def measure(measure_name: str):
    """
    Calculate measure

    Parameters
    ----------
    measure_name : str
        The name of the measure (ex: AMI)
    """
    raise NotImplementedError

cli.add_command(measure)

if __name__ == "__main__":
    cli()
