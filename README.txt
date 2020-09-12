Here you can find my solutions to problems found on the Project Euler website.

https://projecteuler.net/


Create virtualenv:    $ make venv && . venv/bin/activate
Install dependencies: $ make upgrade

Run: $ python solved/1.py


You are free to use this directory structure as a skeleton to store your own
solutions to problems presented on the Project Euler platform. Please make
sure to also copy the LICENSE.txt stored in the same directory as this file.

bin/     scripts for easier management of solutions.
desk/    quite literally the working desk on which I solve my current problem.
drawer/  solutions that are not solutions and need more brainpower.
solved/  working solutions to problems that I've solved.

I use direnv and .envrc to automatically add scripts in bin/ to my PATH.

gen <N>  generates a script from /template.py and puts it on your desk.
         N is the unique number of the problem on the projecteuler.net site.
         optionally opens the file in Sublime Text if that's installed.

run <N>  runs the problem with the number N by looking for it in
		 the current directory or in any of desk/, solved/ or drawer/.

fin <N>  finishes the problem with the number N
         by moving it into the solved/ folder.

repl     clears the terminal and opens an interactive Python REPL.
         press CTRL-D to exit. press CTRL-L to clear the output buffer.


Everything in this repository is licensed under the MIT License.
Copyright (c) 2020 Jonas van den Berg
