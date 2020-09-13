from functools import cached_property
import importlib.util as importlib
import inspect
import os
import uuid

from .definitions import DATA_DIR, DESK_DIR, DRAWER_DIR, SOLVED_DIR


DIRECTORIES = [
    os.getcwd(),
    DESK_DIR,
    SOLVED_DIR,
    DRAWER_DIR
]


class Script:
    def __init__(self, file=None, *, number=None):
        if (file is None) == (number is None):
            raise TypeError("__init__() requires exactly one argument")

        filename = str(file if number is None else number)

        if not filename.lower().endswith('.py'):
            filename += '.py'

        path = os.path.abspath(filename)

        if not os.path.exists(path):
            for directory in DIRECTORIES:
                path = os.path.abspath(os.path.join(directory, filename))
                if os.path.exists(path):
                    break
                path = None

        if not path:
            raise Exception("Unable to locate file {}".format(filename))

        self._path = path

    @property
    def path(self):
        return self._path

    @cached_property
    def problem_number(self):
        filename = os.path.basename(self.path)
        number = os.path.splitext(filename)[0]

        try: return int(number)
        except ValueError:
            return None

    @cached_property
    def uuid(self):
        class_name = self.__class__.__name__
        return uuid.uuid3(uuid.UUID(int=self.problem_number), class_name)

    @cached_property
    def module_name(self):
        return 'p{}-{}'.format(self.problem_number, self.uuid.bytes.hex())

    def create_module(self):
        spec = importlib.spec_from_file_location(self.module_name, self.path)
        module = importlib.module_from_spec(spec)
        spec.loader.exec_module(module)

        return module


class Problem:
    def __init__(self, module):
        self._module = module

        if not hasattr(module, 'solve') or not callable(module.solve):
            raise Exception("Module does not have a solve() function")

        if not hasattr(module, 'solution'):
            raise Exception("Module does not have a 'solution' variable")

        if module.solution is not None \
                and not isinstance(module.solution, str):
            raise Exception("The module's solution is required "
                            "to be a string (str) or empty (None)")

        if not hasattr(module, 'args'):
            raise Exception("Module does not have an 'args' variable")

        if not isinstance(module.args, tuple):
            raise Exception("The module's 'args' variable "
                            "is required to be a tuple")

        # TODO: add optional **kwargs

        try:
            inspect.signature(module.solve).bind(*module.args)
        except TypeError as e:
            raise Exception("The module's function signature of solve() is "
                            "not compatible with the values in 'args'") from e

    @property
    def module(self):
        return self._module

    @property
    def solution(self):
        return self.module.solution

    @property
    def solve_function(self):
        return self.module.solve

    @property
    def args(self):
        return self.module.args

    @property
    def is_solved(self):
        return self.solution is not None

    def solve(self):
        return self.solve_function(*self.args)


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
