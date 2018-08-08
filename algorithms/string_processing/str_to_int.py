"""
You are given some numeric string as input. Conver the string you are
given to an integer. Do not make use of the built-in "int" function.

Example:
    "123" -> 123
    "554" -> 554
    etc.
"""


def str_to_int(input_str):
    s = 0
    for i in range(len(input_str)):
        place = 10**(len(input_str) - (i+1))
        digit = ord(input_str[i]) - ord('0')
        s += digit * place
    return s


str_to_int("123")
str_to_int("3283")

