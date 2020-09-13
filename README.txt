Here you can find my solutions to problems found on the Project Euler website.

https://projecteuler.net/


Create virtualenv:     $ make venv && . activate
Install dependencies:  $ make upgrade


The project consists of the following relevant directories:

bin/     scripts for easier management of solutions.
desk/    quite literally the working desk on which I solve my current problem.
drawer/  solutions that are not solutions and need more brainpower.
solved/  working solutions to problems that I've solved.


After activating the virtual environment with the wrapper script above
you can use the following helper commands to manage your solutions:

generate N
	Generates a script from /template.py and puts it on your desk.
	N is the unique number of the problem on the projecteuler.net site.
	Optionally opens the file in Sublime Text if that's installed.

solve N
	Runs (solves) problem number N by looking for it in these directories:
	the current working directory, desk/, solved/ and drawer/.

finish N
	Finishes problem number N by moving it into the solved/ folder.

check [N1 [N2 [...]]]
	Checks if problems N1, N2, ... give the correct solution.
	If no problem is specified, all solutions in solved/ are tested.
	This is useful if shared code is modified and you would like
	to make sure that your solutions are still working correctly.

repl
	Clears the terminal and opens an interactive Python REPL.
	Press CTRL-D to exit and CTRL-L to clear the output buffer.


You are free to use this directory structure as a skeleton to store
your own solutions to problems presented on the Project Euler platform.

Everything in this repository is licensed under the MIT License.
Copyright (c) 2020 Jonas van den Berg
