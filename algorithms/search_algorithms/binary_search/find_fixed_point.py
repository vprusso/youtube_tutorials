# YouTube Video: https://www.youtube.com/watch?v=BQa1hi6fnOE&list=PL5tcWHG-UPH1kjiE-Fqt1xCSkcwyfn2Jb
"""
A fixed point in an array "A" is an index "i" such that A[i] is equal to "i".

Given an array of n distinct integers sorted in ascending order, write a
function that returns a "fixed point" in the array. If there is not a
fixed point return "None".
"""

# Fixed point is 3:
A = [-10, -5, 0, 3, 7]

# Fixed point is 0:
#A = [0, 2, 5, 8, 17]

# No fixed point. Return "None":
#A = [-10, -5, 3, 4, 7, 9]


# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None


# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_fixed_point(A):
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low + high)//2

        if A[mid] < mid:
            low = mid + 1
        elif A[mid] > mid:
            high = mid - 1
        else:
            return A[mid]
    return None


print(find_fixed_point(A))
