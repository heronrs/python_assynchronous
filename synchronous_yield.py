"""
example_2.py

Just a short example demonstrating a simple state machine in Python
"""

import queue
import time


def task(name, queue):
    while not queue.empty():
        count = queue.get()
        total = 0
        for x in range(count):
            print(f'Task {name} running')
            total += 1
            time.sleep(1)
            yield  # returns control back to the caller
        print(f'Task {name} total: {total}')


def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # create some tasks
    tasks = [
        task('One', work_queue),
        task('Two', work_queue)
    ]

    # run the tasks
    start = time.time()
    while tasks:
        for t in tasks:
            try:
                next(t)
            except StopIteration:
                tasks.remove(t)
    end = time.time() - start
    print(f'Time slapsed {end}')


if __name__ == '__main__':
    main()
