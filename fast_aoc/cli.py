""" Command line interface module
"""
import datetime as dt
import logging

import click

from .config import Config
from .logging_utils import set_logging
from .runner import Runner
from .storage import ProblemStorage
from .waiter import wait_for_problem

LOGGER = logging.getLogger(__name__)


@click.group()
def aoc():
    """ The main CLI command
    """


def config_options(func):
    """ A helper function which joins click.option functions of each parameter from Config
    """
    for param in Config.get_params()[-1::-1]:
        func = click.option('--{}'.format(param), param,
                            help='Set a new value to configuration parameter "{}"'.format(param))(func)
    return func


@aoc.command()
@click.option('--show', is_flag=True, default=False, help='Show current configuration')
@click.option('--reset', is_flag=True, default=False, help='Reset configuration to initial state')
@config_options
def config(show, reset, **params):
    """ Configuration sub-command
    """
    cfg = Config(reset=reset, **params)
    cfg.save()

    if show:
        click.echo(str(cfg))
        click.echo('Configuration file location: {}'.format(cfg.get_config_path()))


# TODO improve these
year_option = click.option('-y', '--year', default=dt.datetime.now().year, help='Year of the problem')
day_option = click.option('-d', '--day', default=dt.datetime.now().day, help='Number of the problem')


@aoc.command()
@year_option
@day_option
def start(year, day):
    """ Start solving a problem
    """
    set_logging(year, day)
    LOGGER.debug('Running start')

    storage = ProblemStorage()
    storage.create_problem_template(year, day)

    input_data = wait_for_problem(year, day)

    storage.fill_problem_template(year, day, input_data)

    LOGGER.info('Problem template created in {}'.format(storage.get_problem_file(year, day)))


@aoc.command()
@year_option
@day_option
def test(year, day):
    """ Test your solution on test cases
    """
    set_logging(year, day)
    LOGGER.debug('Running test')

    solutions = ProblemStorage().get_solution(year, day)

    runner = Runner(year, day, test=True)
    runner.execute(solutions)


@aoc.command()
@year_option
@day_option
def submit(year, day):
    """ Submit your solution
    """
    set_logging(year, day)
    LOGGER.debug('Running submit')

    solutions = ProblemStorage().get_solution(year, day)

    runner = Runner(year, day, test=False)
    runner.execute(solutions)
