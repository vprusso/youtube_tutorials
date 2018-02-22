# YouTube Video: https://www.youtube.com/watch?v=UqEU-obRUnI
"""
Implement an algorithm to determine if a string has all unique characters.
"""

# "unique"
# "bear"


def is_unique(s):
    return len(s) == len(set(s))


s1 = "unique"
s2 = "bear"

# False
print(is_unique(s1))

# True
print(is_unique(s2))
