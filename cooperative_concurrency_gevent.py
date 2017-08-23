"""
example_4.py

Just a short example demonstrating a simple state machine in Python
However, this one has delays that affect it
"""

import time
import queue
import gevent
from gevent import monkey
monkey.patch_all()


def task(name, work_queue):
    while not work_queue.empty():
        count = work_queue.get()
        total = 0
        for x in range(count):
            print(f'Task {name} running')
            total += 1
            time.sleep(1)
        print(f'Task {name} total: {total}')


def main():
    """
    This is the main entry point for the programWhen
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for work in [15, 10, 5, 2]:
        work_queue.put(work)

    # run the tasks
    tasks = [
        gevent.spawn(task, 'One', work_queue),
        gevent.spawn(task, 'Two', work_queue)
    ]
    start = time.time()
    gevent.joinall(tasks)
    end = time.time() - start
    print(f'Time elapsed {end}')


if __name__ == '__main__':
    main()
