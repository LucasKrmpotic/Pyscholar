# -*- coding: utf-8 -*-

"""Console script for pyscholar."""
import sys
import click
from pyfiglet import Figlet

from pyscholar.config.config import Config


@click.group()
def main():
    """Console script for pyscholar."""
    f = Figlet(font='big')
    click.echo(f.renderText('PyScholar'))
    return 0


@main.group()
def storage():
    pass


@storage.command('set_strategy')
@click.argument('name')
def set_strategy(name):
    config_ = Config()
    click.echo(config_.set('storage', 'strategy', name))
    return 0

@storage.command('file_name')
@click.argument('name')
def file_name(name):
    config_ = Config()
    click.echo(config_.set('storage', 'file_name', name))
    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
