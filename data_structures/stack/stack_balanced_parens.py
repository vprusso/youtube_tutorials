# YouTube Video: https://www.youtube.com/watch?v=TC7apM-xGaU
"""
Use a stack to check whether or not a string
has balanced usage of parenthesis.

Example:
    (), ()(), (({[]}))  <- Balanced.
    ((), {{{)}], [][]]] <- Not Balanced.


Balanced Example: {[]}


Non-Balanced Example: (()

Non-Balanced Example: ))
"""

from stack import Stack


def is_match(p1, p2):
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False


def is_paren_balanced(paren_string):
    s = Stack()
    is_balanced = True
    index = 0

    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in "([{":
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
        index += 1

    if s.is_empty() and is_balanced:
        return True
    else:
        return False


print(is_paren_balanced("(((({}))))"))

print(is_paren_balanced("[][]]]"))
print(is_paren_balanced("[][]"))

