# YouTube Video: https://www.youtube.com/watch?v=l7swJRixYUM
"""
An array is "cyclically sorted" if it is possible to cyclically shift
its entries so that it becomes sorted.

The following list is an example of a cyclically sorted array:

    A = [4, 5, 6, 7, 1, 2, 3]

Write a funtion that determines the index of the smallest element
of the cyclically sorted array.
"""

A = [4, 5, 6, 7, 1, 2, 3]


def find(A):
    low = 0
    high = len(A) - 1

    while low < high:
        mid = (low + high) // 2
        print(A[mid])

        if A[mid] > A[high]:
            low = mid + 1
        elif A[mid] <= A[high]:
            high = mid

    return low


idx = find(A)
print(A[idx])
