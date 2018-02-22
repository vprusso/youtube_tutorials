# YouTube Video: https://www.youtube.com/watch?v=yUOoJL9_y9M
"""
Write a iterative and recursive function that implements the factorial
of a number.

5! = 5 * 4 * 3 * 2 * 1
   = 120

n! = n * n - 1 * ... * 1
"""

n = 5


def fact_iter(n):
    x = 1
    for i in range(n, 0, -1):
        # x = x * i
        x *= i
    return x


def fact_recur(n):
    if n <= 1:
        return 1
    else:
        return n * fact_recur(n-1)


# 5! -> 120
# 5 * 4! -> 120
# 4 * 3! -> 24
# 3 * 2! -> 6
# 2 * 1! -> 2
# 1! = 1 -> 1

print(fact_recur(n))
















































#def factorial_iterative(N):
#	x = 1
#	for i in range(1, N+1):
#		x *= i
#	return x

#def factorial_recursive(N):
#	if N <= 1:
#		return 1
#	else:
#		return N * factorial_recursive(N-1)
#
#
#N = 5
#print(factorial_iterative(N))

