#!/usr/bin/env python
import argparse
from src.tasks.common_tasks import get_task_by_number


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("task", type=int,
                        help="number of task to solve")
    args = parser.parse_args()
    task = args.task
    task = get_task_by_number(task)
    if task is None:
        print("No such task! Only 1, 2 and 4 are available.")
        exit(1)
    task.main()


if __name__ == '__main__':
    main()
