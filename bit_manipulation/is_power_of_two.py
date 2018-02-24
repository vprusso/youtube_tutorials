"""
Given a positive integer N, check if N is a power of 2.
"""

# Method 1: Use Log_2
import math


def is_power_of_two_1(n):
    return math.log(n, 2) == math.floor(math.log(n, 2))


# Method 2: Without Python math library
def is_power_of_two_2(n):
    if n == 0: 
        return False
    else:
        while n != 1:
            if n % 2 != 0:
                return False
            else:
                n = n/2
    return True


# Method 3: Without looping
def is_power_of_two_3(n):
    if n == 0:
        return False
    else:
        return n and not(n & (n-1))


n = 2
print(is_power_of_two_1(n))
print(is_power_of_two_2(n))
print(is_power_of_two_3(n))

n = 3
print(is_power_of_two_1(n))
print(is_power_of_two_2(n))
print(is_power_of_two_3(n))

n = 4
print(is_power_of_two_1(n))
print(is_power_of_two_2(n))
print(is_power_of_two_3(n))
