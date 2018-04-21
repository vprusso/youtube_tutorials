"""
Write a program  that takes an integer and
sets the n-th bit in the binary representation of
that integer

For instance, the binary representation of 6 is:
    110

The least significant bit is the bit on the far right
of the binary representation and the most significant
bit is the bit on the far left. We order the bits as

b2, b1, b0
1   1   0

For our function, if we set the 0th bit, we should obtain
the binary representation:
    1 1 1
"""


"""
We can combine the shift operator with the same idea used in the video
to determine if the nth bit is set:
    XXX

Example: Set 0th bit:

    6       : 1 1 0
    1 << 0  : 0 0 1
            -------- |
              1 1 1
"""


def set_nth_bit(x: int, n: int):
    # If you just want to return the binary
    # representation of the number:
    #return bin(x | 1 << n)[2:]
    return x | 1 << n


print(set_nth_bit(6, 0))
