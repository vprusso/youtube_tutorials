# YouTube Video: https://www.youtube.com/watch?v=71UjBGz-o0w
"""
1.4
Palindrome Permutation: Given a string, write a function to check if it is
a permutation of a palindrome. A palindrome is a word or phrase that is the
same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
"""

palindrome = "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!"
not_palindrome = "LucidProgramming"


def is_palindrome_perm(input_str):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    input_str = input_str.replace(" ", "")
    input_str = input_str.lower()

    hist = dict.fromkeys(list(alphabet.lower()), 0)
    for letter in input_str:
        if letter in alphabet.lower():
            hist[letter] += 1

    strike = 0
    odd_strike = 0
    for letter in hist:
        if hist[letter] % 2 != 0 and hist[letter] > 1:
            odd_strike += 1
            if hist[letter] == 1:
                strike += 1
            if strike == 2 or odd_strike == 2:
                return False
    return True


print(is_palindrome_perm("XXXYYY"))
