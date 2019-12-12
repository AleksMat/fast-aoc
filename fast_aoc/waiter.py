""" Utilities for awaiting a new problem
"""
import datetime as dt
import logging
import time

from aocd.models import Puzzle

LOGGER = logging.getLogger(__name__)

def wait_for_problem(year, day):

    problem_start = dt.datetime(year=year, month=12, day=day, hour=6, minute=0, second=0)  # TODO: improve

    while dt.datetime.now() < problem_start:
        sleep_time = (problem_start - dt.datetime.now()).total_seconds() + 0.1

        if sleep_time > 5:
            sleep_time = sleep_time * 0.9

        LOGGER.info(f'Problem has not yet started, sleeping for {sleep_time}s')
        time.sleep(sleep_time)

        # TODO: make countdown

    input_data = None
    while input_data is None:
        try:
            input_data = Puzzle(year=year, day=day).input_data
        except BaseException as exception:
            LOGGER.error(f'Failed to get data: {exception}')
            time.sleep(0.5)

    return input_data
