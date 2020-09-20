import importlib
import os.path
import sys
import re

import euler.problem


for number, filename in euler.problem.iterate_solved_scripts():
    name = '{}.p{}'.format(__name__, number)
    sys.modules[name] = euler.problem.LazyProblemModule(filename)
