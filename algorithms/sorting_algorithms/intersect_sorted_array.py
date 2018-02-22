# YouTube Video: https://www.youtube.com/watch?v=vNm2nvDyyls
A = [2, 3, 3, 5, 7, 11]
B = [3, 3, 7, 15, 31]

# One-liner. This works, but does not take advantage of
# the fact that A and B are sorted. We can do a bit
# better by taking advantage of this fact.
# print(set(A) & set(B))


def intersect_sorted_array(A, B):
    i = 0
    j = 0
    intersection = []

    while i < len(A) and j < len(B):
        if A[i] == B[j]:
            if i == 0 or A[i] != A[i - 1]:
                intersection.append(A[i])
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    return intersection


print(intersect_sorted_array(A, B))
