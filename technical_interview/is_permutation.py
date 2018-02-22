# YouTube Video: https://www.youtube.com/watch?v=71UjBGz-o0w
"""
Given two strings, write a function to decide if one is a permutation
of the other.
"""

# "driving"
# "drivign" <- Permutation.
# "ddriving" <- Not a permutation.
# "riving" <- Not a permutation.
# "criving" <- Not a permutation.

# "the cow jumps over the moon."
# "the moon jumps over the cow." <- Permutation.
# "the cow      jumps over the moon." <- Permutation.

str_1 = "driving"
str_2 = "criving"


def is_permutation(str_1, str_2):
    str_1 = str_1.replace(" ", "")
    str_2 = str_2.replace(" ", "")

    if len(str_1) != len(str_2):
        return False

    for c in str_1:
        if c in str_2:
            str_2 = str_2.replace(c, "")
    return len(str_2) == 0


print(is_permutation(str_1, str_2))
