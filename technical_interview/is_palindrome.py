# YouTube Video: https://www.youtube.com/watch?v=y3S0iYFedCw
"""
Given a string, write a function to determine if it is a palindrome.
"""

# racecar
# madam
# Dammit I'm mad.

import string


def is_palindrome(s):
    s = s.lower()
    s = s.translate(None, string.punctuation)
    s = s.replace(" ", "")

    return s == s[::-1]


str_1 = "racecar"
str_2 = "Dammit I'm mad."
str_3 = "computer"

print(is_palindrome(str_1))
print(is_palindrome(str_2))
print(is_palindrome(str_3))
