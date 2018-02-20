# YouTube Video: https://www.youtube.com/watch?v=QvSIAB27Vdk
A = [6, 3, 2, 7, 5, 5]

A = sorted(A)

for i in range(len(A)//2):
    print(A[i], A[~i])
