# YouTube Link: https://www.youtube.com/watch?v=itbx_hDX7z8

# Introduction an simple example of the multiprocessing module in Python.
# We show how to simply apply this module to a function that takes a number
# and squares it.

import os
import time

from multiprocessing import Process, current_process


def cube(numbers):
    for number in numbers:
        time.sleep(0.5)
        print(f"The number {number} cubes to {number*number*number}.")


def square(numbers):
    for number in numbers:
        time.sleep(0.5)
        print(f"The number {number} squares to {number*number}.")


if __name__ == '__main__':

    processes = []
    numbers = range(100)

    for i in range(100):
        process = Process(target=square, args=(numbers,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    #p1 = Process(target=square, args=(numbers,))
    #p2 = Process(target=cube, args=(numbers,))
    #p3 = Process(target=square, args=(numbers,))

    #p1.start()
    #p2.start()
    #p3.start()

    #p1.join()
    #p2.join()
    #p3.join()

    print("Multiprocessing process complete")

