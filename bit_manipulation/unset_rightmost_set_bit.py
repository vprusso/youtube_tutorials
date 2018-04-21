"""
Write a program  that takes an integer and
unsets the right most bit in the binary representation 
of that integer

For instance, the binary representation of 7 is:
    111

The least significant bit is the bit on the far right
of the binary representation and the most significant
bit is the bit on the far left. We order the bits as

b2, b1, b0
1   1   1

For our function, if we unset the right-most bit,
we should obtain the binary representation:
    1 1 0
    
Alternatively, if we have a number like this

1 1 0 0

Then the result of our function should yield:

1 0 0 0
"""


"""
Observation:

We can combine some of the ideas present in the video 
one how to unset the nth bit:
    XXX

Example: Unset the right-most bit:

        0 1 0 1 0 1 1 1     (x)
    &   0 1 0 1 0 1 1 0     (x-1)
        ---------------
        0 1 0 1 0 1 1 0

Example: Unset the right-most bit:

        0 1 0 1 1 0 0 0     (x)
    &   0 1 0 1 0 1 1 1     (x-1)
        ---------------
        0 1 0 1 0 0 0 0
"""


def unset_rightmost_set_bit(x: int):
    return x & (x-1)


# Unset rightmost bit of binary representation of 7:
y = unset_rightmost_set_bit(7)
print(y)

