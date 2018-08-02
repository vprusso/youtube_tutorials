# YouTube Video: https://www.youtube.com/watch?v=G8SI2Jrqeww&index=3&list=PL5tcWHG-UPH1u5iox6v1Hey59vNd5cnTw
"""
Write a program that takes an integer and tests whether
the n-th bit in the binary representation of that integer
is set of not.

For instance, the binary representation of 6 is:
    110

The least significant bit is the bit on the far right
of the binary representation and the most significant
bit is the bit on the far left. We order the bits as

b2, b1, b0
1   1   0

For our function, if we check the 0th bit, we should obtain
"False" as the binary value at b0 is 0.

Alternatively, if we check the 1st bit, we should obtain
"True" as the binary value at b1 is 1.
"""


"""
Observation:
    1 << 0 : 0 0 0 0 0 0 0 1
    1 << 1 : 0 0 0 0 0 0 1 0
    1 << 2 : 0 0 0 0 0 1 0 0
    1 << 3 : 0 0 0 0 1 0 0 0
    1 << 4 : 0 0 0 1 0 0 0 0
    1 << 5 : 0 0 1 0 0 0 0 0
    1 << 6 : 0 1 0 0 0 0 0 0
    1 << 7 : 1 0 0 0 0 0 0 0

We can combine the shift operator with the same idea used in the video
to determine if a given number is even or odd:
    XXX

Example: Is 2nd bit set?

    6      : 1 1 0
    1 << 2 : 1 0 0
            ------ &
             1 0 0

Example: Is 0th bit set?

    6      : 1 1 0
    1 << 0 : 0 0 1
            ------ &
             0 0 0

Observation:
    If we AND the result of shifting over by n with
    the number in question, we obtain either 0 or 1:

    0 : n-th bit is not set.
    1 : nth bit is set.
"""


def is_nth_bit_set(x: int, n: int):
    if x & (1 << n):
        return True
    return False


# Is 2nd bit set for binary representation of 6: (True)
print(is_nth_bit_set(6, 2))

# Is 0th bit set for binary representation of 6: (False)
print(is_nth_bit_set(6, 0))
