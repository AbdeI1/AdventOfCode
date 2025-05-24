# Advent of Code Solution Repo

This repo contains my solutions for [Advent of Code](https://adventofcode.com/)

## Structure

Each solution is designed to be self contained and not rely on any other files (with an exception for 2019 where half the problems needed and intcode interpreter, so all those problems rely on the [`intcode.py`](/2019/intcode.py) file in that directory). Additionally, for any single day, each part is also designed to not rely on the other. \
Each file is designed to read from an `input.txt` file in the same directory and will print two lines to `stdout` for solutions to part 1 and 2. \
For the most part, only the standard library is used, however installation of some popular libraries may be required for some solutions.

The [`wrapper.py`](/wrapper.py) contains helpful functions that automate:

* initializing the directory structure and code files
* downloading the input and placing it in the right location
* running the solution file and submitting whatever is printed

requires the [advent-of-code-data](https://pypi.org/project/advent-of-code-data/) package as well as pasting your Advent of Code session token into a file named `.session.data` in the same directory. Check the package page for more details on how to get session token. \
Some problems require drawing letters (or other things) in a grid, then printing out the grid to read the solution. For these problems,
the automatic submit won't work.

## Reporting Issues

The majority of the problems were only tested on my inputs and gave me the right solution. While I generalized my solutions so that they don't overfit on my input, I haven't tested it on any extra inputs. If any of the solutions give you the wrong answer on your input, be sure to report it as a GitHub issue and paste your input (use `wrong answer` tag).

## Additional Help

If you want extra help for a solution, feel free to open an issue requesting an explanation (use `question` tag). I will try to respond and elaborate on my solution.
