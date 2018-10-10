# YouTube Link:

# We will look at how to share a state (or variable) between processes.
# Note that we touched on this when covering the video on locks:
# ()


from multiprocessing import Process, Value, Array


def f(d, i, a):
    d.value = 3.14159
    i.value = 100

    for i in range(len(a)):
        a[i] = -a[i]


def g(d):
    d.value = 1.689


if __name__ == '__main__':

    double_val = Value('d', 0.0)
    int_val = Value('i', 5)

    arr_val = Array('i', range(10))

    p1 = Process(target=f, args=(double_val, int_val, arr_val))
    p1.start()
    p1.join()

    print(double_val.value)
    print(int_val.value)
    print(arr_val[:])

    p2 = Process(target=g, args=(double_val,))

    p2.start()
    p2.join()

    print(double_val.value)
