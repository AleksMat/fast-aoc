""" Module where solution is being executed
"""
import logging
import time

from aocd import PuzzleUnsolvedError
from aocd.models import Puzzle

LOGGER = logging.getLogger(__name__)


class Runner:

    PARTS = ['a', 'b']

    def __init__(self, year, day, test=False):

        self.year = year
        self.day = day
        self.test = test

        self.problem = Puzzle(year=self.year, day=self.day)  # TODO: at this point a connection to AOC starts :S
        self.input_data = self.problem.input_data

    def get_expected_answer(self, part):

        try:
            if part == 'a':
                return self.problem.answer_a
            return self.problem.answer_b
        except (PuzzleUnsolvedError, AttributeError):
            return None

    def submit_answer(self, answer, part):
        """ Submits the answer
        """
        if part == 'a':
            self.problem.answer_a = answer
        else:
            self.problem.answer_b = answer

    def execute(self, solutions):
        """ Function that executes solution for given year and day
        """
        for solution, part in zip(solutions, self.PARTS):

            expected_answer = self.get_expected_answer(part)

            if expected_answer is not None and not self.test:
                continue

            LOGGER.info(f'Starting to solve part {part}')

            start = time.time()
            answer = solution(self.input_data)
            elapsed_time = time.time() - start

            if answer is None:
                LOGGER.info(f'Solution for part {part} is not yet implemented')
                continue

            LOGGER.info(f'Finished solving part {part}, answer is {answer}, time spent {elapsed_time:0.3f}s')  # TODO nicer time formatting

            if expected_answer is not None:
                if str(answer) == expected_answer:
                    LOGGER.info('Answer is correct!')
                else:
                    LOGGER.info(f'Answer is wrong, correct answer is {expected_answer}')

            if not self.test:
                self.submit_answer(answer, part)
