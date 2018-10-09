# YouTube Link: https://www.youtube.com/watch?v=RR4SoktDQAw

# Introduction an simple example of the multiprocessing module in Python.
# We show how to simply apply this module to a function that takes a number
# and squares it.

import os

from multiprocessing import Process, current_process


def square(number):
    """The function squares whatever number it is provided."""
    result = number * number

    # We can use the OS module in Python to print out the process ID
    # assigned to the call of this function assigned by the operating
    # system.
    proc_id = os.getpid()
    print(f"Process ID: {proc_id}")

    # We can also use the "current_process" function to get the name
    # of the Process object:
    process_name = current_process().name
    print(f"Process Name: {process_name}")

    print(f"The number {number} squares to {result}.")


if __name__ == '__main__':

    # The processes list will store each call we make to "square" and the
    # numbers list contains the numbers we loop through and call the
    # "square" function on."
    processes = []
    numbers = [1, 2, 3, 4, 5]

    # Loop through the list of numbers, call the "square" function,
    # and store and start each call to "square".
    for i, number in enumerate(numbers):
        process = Process(target=square, args=(number,))
        processes.append(process)

        # Processes are spawned by creating a Process object and
        # then calling its start() method.
        process.start()

    # Wait for Python process to end before starting the
    # next process.
    for process in processes:
        process.join()

