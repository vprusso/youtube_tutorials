# YouTube Video: https://www.youtube.com/watch?v=0gkWZNE1H4Y&list=PL5tcWHG-UPH1kjiE-Fqt1xCSkcwyfn2Jb
"""
Given an array of sorted integers. We need to find the closest value to the 
given number.

Array may contain duplicate values and negative numbers.

Examples:

    Input : arr[] = {1, 2, 4, 5, 6, 6, 8, 9}

    Target number = 11
    Output : 9
    9 is closest to 11 in given array

    Input :arr[] = {2, 5, 6, 7, 8, 8, 9};
    Target number = 4
    Output : 5
"""

A = [1, 2, 4, 5, 6, 6, 8, 9]
A = [2, 5, 6, 7, 8, 8, 9]


def find_closest_num(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) - 1
    closest_num = None

    # Edge cases for empty list of list
    # with only one element:
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high)//2
        
        # Keep track of the closest value from the target 
        # so far.
        if min_diff > abs(A[mid] - target):
            closest_num = A[mid]
            min_diff = abs(A[mid] - target)

        # Move the mid-point appropriately as is done
        # via binary search.
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        # If the element itself is the target, the closest
        # number to it is itself. Return the number.
        else:
            return A[mid]
    return closest_num


y = find_closest_num(A, 4)
print(y)
