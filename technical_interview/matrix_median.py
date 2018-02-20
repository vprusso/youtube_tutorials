# YouTube Video: https://www.youtube.com/watch?v=wn-NKs_KNyQ
"""
Given a N cross M matrix in which each row is sorted, find the overall median of the matrix.
Assume N*M is odd.

For example,

Matrix=
[1, 3, 5]
[2, 6, 9]
[3, 6, 9]

A = [1, 2, 3, 3, 5, 6, 6, 9, 9]

Median is 5. So, we return 5.
"""


def median_matrix(A):
    if len(A) == 1:
        vec = A[0]
        return vec[len(vec)//2]
    else:
        new_list = []
        for row in range(len(A)):
            new_list.extend(A[row])
        new_list = sorted(new_list)
    return new_list[len(new_list)//2]


# Example 1: 
l1 = [1, 3, 5]
l2 = [2, 6, 9]
l3 = [3, 6, 9]
A = [l1, l2, l3]

# Example 2:
A1 = [l1]

print(median_matrix(A))
print(median_matrix(A1))
