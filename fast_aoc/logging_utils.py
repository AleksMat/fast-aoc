""" Module defining logging functionalities of the package
"""
import logging
import sys

from .storage import ProblemStorage


def set_logging(year, day):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    for handler in logger.handlers:
        handler.close()
        logger.removeHandler(handler)

    # Std out handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(message)s')
    handler.setFormatter(formatter)
    handler.addFilter(StdoutFilter())
    logger.addHandler(handler)

    logs_filename = ProblemStorage().get_logs_file(year, day)
    handler = logging.FileHandler(logs_filename, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s:%(lineno)d:\n\t%(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler.setFormatter(formatter)
    logger.addHandler(handler)


class StdoutFilter(logging.Filter):
    """ Filters log messages passed to standard output
    """
    def filter(self, record):
        """ Shows only logs from fast-aoc package and high-importance logs
        """
        if record.levelno >= logging.WARNING:
            return True

        return record.name.startswith('fast_aoc')
