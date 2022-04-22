#!/usr/bin/env python
import argparse
import src.tasks.task01 as task01
import src.tasks.task02 as task02
import src.tasks.task04 as task04


def get_task_by_number(n: int):
    match n:
        case 1:
            return task01
        case 2:
            return task02
        case 4:
            return task04
        case _:
            return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("problem", type=int,
                        help="number of problem to solve")
    args = parser.parse_args()
    problem = args.problem
    task = get_task_by_number(problem)
    if task is None:
        print("No such problem! Only 1, 2 and 4 are available.")
        exit(1)
    task.main()


if __name__ == '__main__':
    main()
