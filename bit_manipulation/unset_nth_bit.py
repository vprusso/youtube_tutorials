# YouTube Video: https://www.youtube.com/watch?v=4sYl6oIgrs8&index=5&list=PL5tcWHG-UPH1u5iox6v1Hey59vNd5cnTw
"""
Write a program  that takes an integer and
unsets the n-th bit in the binary representation of
that integer

For instance, the binary representation of 6 is:
    110

The least significant bit is the bit on the far right
of the binary representation and the most significant
bit is the bit on the far left. We order the bits as

b2, b1, b0
1   1   0

For our function, if we unset the 1st bit, we should obtain
the binary representation:
    1 0 0
"""


"""
Observation:
    ~(1 << 0) : 1 1 1 1 1 1 1 0
    ~(1 << 1) : 1 1 1 1 1 1 0 1
    ~(1 << 2) : 1 1 1 1 1 0 1 1
    ~(1 << 3) : 1 1 1 1 0 1 1 1
    ~(1 << 4) : 1 1 1 0 1 1 1 1
    ~(1 << 5) : 1 1 0 1 1 1 1 1
    ~(1 << 6) : 1 0 1 1 1 1 1 1
    ~(1 << 7) : 0 1 1 1 1 1 1 1

We can combine the negation of the shift operator above
with the idea used in how we set the nth bit:
    XXX

Example: Unset the 1st bit in 6:
    6         : 1 1 0
    ~(1 << 1) : 1 0 1
                ------ &
                1 0 0
"""


def unset_nth_bit(x: int, n: int):
    # If you just want to return the binary
    # representation of the number:
    # return bin(x & ~(1 << n))[2:]
    return x & ~(1 << n)


# Unset 1st bit in binary representation of 6:
print(unset_nth_bit(6, 1))

# Unset 2nd bit in binary representation of 6:
print(unset_nth_bit(6, 2))
