# YouTube Vide: https://www.youtube.com/watch?v=3WuUy2UPX9s
"""
1.5
One Away: There are three types of edits that can be performed on strings:
insert a character, remove a character, or replace a character. Given two
strings, write a function to check if they are one edit (or zero edits) away.
"""

test_str_1 = "pale"
test_str_2 = "ple"

test_str_3 = "pales"
test_str_4 = "pale"

test_str_5 = "pale"
test_str_6 = "bale"

test_str_7 = "pale"
test_str_8 = "bake"

test_str_9 = "pale"
test_str_10 = "pale"


def is_one_away(input_str_1, input_str_2):
    return 0 <= len(list(set(input_str_1) - set(input_str_2))) <= 1


# Should return True
print(is_one_away(test_str_1, test_str_2))

# Should return False
print(is_one_away(test_str_7, test_str_8))
