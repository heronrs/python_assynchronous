"""
example_5.py

Just a short example demonstrating a simple state machine in Python
This version is doing actual work, downloading the contents of
URL's it gets from a queue
"""

import gevent
from gevent import monkey
monkey.patch_all()
import queue
import requests
import time


def task(name, work_queue):
    while not work_queue.empty():
        url = work_queue.get()
        print(f'Task {name} getting URL: {url}')
        requests.get(url)
        print(f'Task {name} got URL: {url}')


def main():
    """
    This is the main entry point for the program
    """
    # create the queue of 'work'
    work_queue = queue.Queue()

    # put some 'work' in the queue
    for url in [
        "http://google.com",
        "http://yahoo.com",
        "http://linkedin.com",
        "http://shutterfly.com",
        "http://mypublisher.com",
        "http://facebook.com"
    ]:
        work_queue.put(url)

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
