import inspect
import os

from .definitions import DATA_DIR
from .problem import Script


# TODO: move Data class to problem.py

class Data:
    def __init__(self, problem_filename=None):
        paths = [ problem_filename ]

        if not problem_filename:
            paths = [ s[1] for s in reversed(inspect.stack()) ]

        for path in paths:
            problem_number = Script(path).problem_number
            if problem_number is not None:
                self._problem_number = problem_number
                return

            # TODO: throw below exception in Script() and
            #   reraise if no valid path has been found.

        raise Exception('Expected file to be named N.py, '
                        'with N being an integer')


    def read(self, filename):
        problem = str(self._problem_number)
        filename = os.path.join(DATA_DIR, problem, filename)

        with open(filename, 'r') as file:
            return file.read()


def read_data(filename, problem_filename=None):
    return Data(problem_filename).read(filename)
