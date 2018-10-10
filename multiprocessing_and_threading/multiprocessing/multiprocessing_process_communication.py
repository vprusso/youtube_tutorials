# YouTube Link:

# We show how to make use of the multiprocessing Queue class to communicate
# between different processes.


from multiprocessing import Process, Queue, Lock


def square(numbers, queue, lock):
    for i in numbers:
        lock.acquire()
        queue.put(i*i)
        lock.release()


def cube(numbers, queue, lock):
    for i in numbers:
        lock.acquire()
        queue.put(i*i*i)
        lock.release()


if __name__ == '__main__':

    numbers = range(5)
    lock = Lock()

    queue = Queue()
    square_process = Process(target=square, args=(numbers, queue, lock))
    cube_process = Process(target=cube, args=(numbers, queue, lock))

    square_process.start()
    cube_process.start()

    square_process.join()
    cube_process.join()

    while not queue.empty():
        print(queue.get())



