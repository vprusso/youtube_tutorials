# YouTube Link:

# A lock or mutex is a sychronization mechanism for enforcing
# limits on access to a resource in an environment where there
# are many threads of execution.

# More on locks:
# https://en.wikipedia.org/wiki/Lock_(computer_science)

import logging
import time
from multiprocessing import Process, Lock, Value
from multiprocessing import log_to_stderr, get_logger


def add_500_no_mp(total):
    for i in range(100):
        time.sleep(0.01)
        total += 5
    return total


def sub_500_no_mp(total):
    for i in range(100):
        time.sleep(0.01)
        total -= 5
    return total


def add_500_no_lock(total):
    for i in range(100):
        time.sleep(0.01)
        total.value += 5


def sub_500_no_lock(total):
    for i in range(100):
        time.sleep(0.01)
        total.value -= 5


def add_500_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value += 5
        lock.release()


def sub_500_lock(total, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        total.value -= 5
        lock.release()


#if __name__ == '__main__':
#
#    total = 500
#    print(total)
#    total = add_500_no_mp(total)
#    print(total)
#    total = sub_500_no_mp(total)
#    print(total)

#if __name__ == '__main__':
#
#    total = Value('i', 500)
#    add_proc = Process(target=add_500_no_lock, args=(total,))
#    sub_proc = Process(target=sub_500_no_lock, args=(total,))
#
#    add_proc.start()
#    sub_proc.start()
#
#    add_proc.join()
#    sub_proc.join()
#    print(total.value)

if __name__ == '__main__':

    total = Value('i', 500)
    lock = Lock()

    log_to_stderr()
    logger = get_logger()
    logger.setLevel(logging.INFO)

    add_proc = Process(target=add_500_lock, args=(total, lock))
    sub_proc = Process(target=sub_500_lock, args=(total, lock))

    add_proc.start()
    sub_proc.start()

    add_proc.join()
    sub_proc.join()
    print(total.value)


