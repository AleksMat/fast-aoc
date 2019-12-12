""" Module for handling where problems are being stored
"""
import os
import shutil

from .config import Config
from .importing import import_module


class ProblemStorage:
    """ Problem storage class
    """

    def __init__(self, config=None):

        self.config = config or Config(raise_undefined=True)

    def get_year_folder(self, year):
        """ Return folder path for a given year
        """
        return os.path.join(self.config.folder, str(year))

    def get_problem_folder(self, year, day):
        """ Returns folder path for given problem
        """
        return os.path.join(self.get_year_folder(year), f'problem-{day}')

    def get_problem_file(self, year, day):
        return os.path.join(self.get_problem_folder(year, day), 'solution.py')

    def get_logs_file(self, year, day):
        return os.path.join(self.config.CONFIG_FOLDER, self.config.token, f'{year}_{day:02d}_logs.txt')

    @staticmethod
    def get_template_file():
        return os.path.join(os.path.dirname(__file__), 'template.py')

    def create_problem_template(self, year, day):

        problem_folder = self.get_problem_folder(year, day)

        if not os.path.exists(problem_folder):
            os.makedirs(problem_folder)

        problem_file = self.get_problem_file(year, day)
        if not os.path.isfile(problem_file):
            shutil.copyfile(self.get_template_file(), problem_file)

    def fill_problem_template(self, year, day, input_data):
        problem_file = self.get_problem_file(year, day)

        with open(problem_file, 'r') as fp:
            code = fp.read()

        # TODO: find better way to do the following
        code = code.replace('{{year}}', str(year)).replace('{{day}}', str(day))
        code = code.replace('{{input_data}}', self.summarize_input_data(input_data))

        with open(problem_file, 'w') as fp:
            fp.write(code)

    @staticmethod
    def summarize_input_data(input_data):

        lines = input_data.split('\n')

        if len(lines) > 8:
            lines = lines[:4] + ['...', f'{len(lines) - 8} more', '...'] + lines[-4:]

        return '\n    '.join(ProblemStorage.summarize_line(line) for line in lines)

    @staticmethod
    def summarize_line(line):
        if len(line) > 100:
            return line[:75] + f'...{len(line) - 100} more...' + line[-25:]
        return line

    def get_solution(self, year, day):
        """ Provides the solution
        """
        problem_file = self.get_problem_file(year, day)

        solution_module = import_module('solution', problem_file)

        return solution_module.solve_a, solution_module.solve_b


def get_common_module(year, config=None):
    """ Imports a common module for a given year
    """
    storage = ProblemStorage(config=config)

    module_path = storage.get_year_folder(year)

    return import_module('common', os.path.join(module_path, 'common.py'))
