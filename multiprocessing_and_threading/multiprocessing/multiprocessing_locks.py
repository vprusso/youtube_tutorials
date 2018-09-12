# YouTube Link:

# A lock or mutex is a sychronization mechanism for enforcing
# limits on access to a resource in an environment where there
# are many threads of execution.

# More on locks:
# https://en.wikipedia.org/wiki/Lock_(computer_science)

from multiprocessing import Process, Lock


def info(item, lock):
    """Outputs the item passed in."""

    # Acquire a lock prior to using it.
    lock.acquire()

    # If the lock is released, print the item.
    # Otherwise, release the lock.
    try:
        print(item)
    finally:
        lock.release()


if __name__ == '__main__':
    lock = Lock()
    items = ['Lucid', 'Programming', 'Tutorials']

    # Loop through all of the items in the above list and create
    # a process for each element in the list.
    for item in items:
        # Passing and using the lock allows us to ensure that
        # the next process will wait until the lock is released.
        p = Process(target=info, args=(item, lock))
        p.start()
