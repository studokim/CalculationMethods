#!/usr/bin/env python
import argparse
import src.tasks.task01 as task01
import src.tasks.task02 as task02
import src.tasks.task04 as task04


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", type=int,
                        help="number of problem to solve")
    args = parser.parse_args()
    problem = args.problem
    match problem:
        case 1:
            task01.main()
            return 0
        case 2:
            task02.main()
            return 0
        case 4:
            task04.main()
            return 0
        case _:
            print("No such problem! Only 1, 2 and 4 are available.")
            exit(1)


if __name__ == '__main__':
    main()
