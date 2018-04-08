"""
Write a program to determine if a given number is even or odd.
Do not make use of the modulus operator.
"""


"""
  : 4 2 1
0 : 0 0 0
1 : 0 0 1
2 : 0 1 0
3 : 0 1 1
4 : 1 0 0
5 : 1 0 1
6 : 1 1 0
7 : 1 1 1

Note:
    Adding one to an even number makes it odd.
    Adding any number of even numbers will result in an even number.
"""

"""
Example:
    1 : 0 0 1
        0 0 1
        -----
        0 0 1

    3 : 0 1 1
        0 0 1
        -----
        0 0 1

    6 : 1 1 0
        0 0 1
        0 0 0

Observation:
    ANDing the number with 1 gives either "0" or "1":
        0 : If even.
        1 : If odd.
"""


def is_even_odd(x: int):
    if x & 1 == 0:
        return "Even"
    else:
        return "Odd"


# Yields "Even":
print(is_even_odd(26))

# Yields "Odd":
print(is_even_odd(25))
