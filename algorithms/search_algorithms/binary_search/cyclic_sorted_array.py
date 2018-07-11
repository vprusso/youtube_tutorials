"""
An array is "cyclically sorted" if it is possible to cyclically shift
its entries so that it becomes sorted.

The following list is an example of a cyclically sorted array:

    A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]

Write a funtion that determines the index of the smallest element
of the cyclically sorted array.
"""

A = [378, 478, 550, 631, 103, 203, 220, 234, 279, 368]


def find(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2

        if A[mid] > A[high]:
            low = mid + 1
        else:
            high = mid

    return low 


idx = find(A)
print(A[idx])
