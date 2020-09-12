import inspect
import os

from .definitions import DATA_DIR


class Data:
    def __init__(self, problem_filename=None):
        paths = [ problem_filename ]

        if not problem_filename:
            paths = [ s[1] for s in reversed(inspect.stack()) ]

        for path in paths:
            filename = os.path.basename(path)
            problem = os.path.splitext(filename)[0]

            try: self.problem_number = int(problem)
            except ValueError: continue

            return

        raise Exception('Expected file to be named N.py, '
                        'with N being an integer')


    def read(self, filename):
        problem = str(self.problem_number)
        filename = os.path.join(DATA_DIR, problem, filename)
        with open(filename, 'r') as file:
            return file.read()


def read_data(filename, problem_filename=None):
    return Data(problem_filename).read(filename)

