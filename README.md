# Fast Advent of Code Python package

An interface for fast and efficient solving of [Advent of Code](https://adventofcode.com/) (AoC) problems.

## About

As a contestant at AoC your task is to read a problem description and implement a solution. The mission of `fast-aoc` package is to make all the remaining steps as automatic as possible. It should save you some crucial amount of seconds and therefore improve your overall standings at the contest.

The package automatically does the following:
- downloads and stores input data of a problem,
- using a template it prepares an initial structure of your solution,
- parses input data,
- runs your solutions on custom test inputs (TODO),
- runs your solution on official input data,
- submits your answer to AoC site,
- caches wrong and correct answers and prevents you to resubmit the same wrong answer twice,
- saves logs of your solving process for you to later analyze your performance.

The package is written in Python and (for now) intended only for contestants who write their solutions in Python. It is built on top of an excellent package [`advent-of-code-data`](https://github.com/wimglenn/advent-of-code-data) which already implements interactions with AoC site and caching of answers.

## Install

The package requires Python version `>=3.6`.

TODO: release to PyPI

## Configure

Before you start using the package you have to configure some parameters. In command line check the following:
```bash
aoc config --help
```
and
```bash
aoc config --show
```
You can set these parameters either in the command line
```bash
aoc config --token <your AoC token> \
           --folder <folder with your solutions>
```
or manually by editing a file `~/.config/aocd/fast_aoc_config.json`.

## Solve

The package implements a simple *2-step solving process*.

**1. Start solving a problem**

If you are about to start solving a problem for the current day run the command:
```bash
aoc start
```
This will wait until the problem is released, download and save input data and prepare the basic structure of your program. The created program structure will contain functions `solve_a` and `solve_b` which you have to implement for parts A and B of the problem, respectively.

Alternatively, if you are about to start solving an older problem you have to specify additional parameters for year and day:
 ```bash
aoc start -y 2019 -d 1
```

**2. Submit a solution**

Once you have implemented any of the functions `solve_a` or `solve_b` you can run a command:
```bash
aoc submit
```
This will run your solution on official input data, submit the answer to AoC and inform you about the verdict.

Note the following:
- If a function returns `None` (i.e. default result of unimplemented function) that answer won't be submitted to AoC.
- A function can return an answer of any type. The answer will be cast to a string before being submitted to AoC.
- If a part of the problem has already been solved the corresponding function won't be even executed.

Alternatively, if you are solving an older problem you have to specify additional parameters for year and day:
 ```bash
aoc submit -y 2019 -d 1
```

**Test a solution (optional)**

TODO

## More features

TODO

## License and Conduct
The package license is available [here](https://github.com/AleksMat/fast-aoc/blob/master/LICENSE).

Please use this package at your own risk. It is advised that you first test it and get familiar with its content before using it at an active AoC contest. The author does not take responsibility for any bad performance you might have because of this package.

If you notice any problems or think of any useful new features please report them on [GitHub issues](https://github.com/AleksMat/fast-aoc/issues). Any pull requests are also much appreciated.


**Happy Coding!**
