# YouTube Video: https://www.youtube.com/watch?v=3r5TmVmPuJ8&index=6&list=PL5tcWHG-UPH1u5iox6v1Hey59vNd5cnTw
"""
Write a program  that takes an integer and
toggles the n-th bit in the binary representation of
that integer

For instance, the binary representation of 6 is:
    110

The least significant bit is the bit on the far right
of the binary representation and the most significant
bit is the bit on the far left. We order the bits as

b2, b1, b0
1   1   0

For our function, if we toggle the 0th bit, we should obtain
the binary representation:
    1 1 1

If we again toggle the 0th bit from the above representation 
we obtain
    1 1 0
"""


"""
We can combine the ideas inherent in the videos where we covered 
set_nth_bit and unset_nth_bit:

Example: Toggle 0th bit:

    6       : 1 1 0
    1 << 0  : 0 0 1
            -------- ^
              1 1 1

If we then toggle the same 0th bit:

    7       : 1 1 1
    1 << 0  : 0 0 1
            -------- ^
              1 1 0
"""


def toggle_nth_bit(x: int, n: int):
    return x ^ (1 << n)


# Toggle the 0th bit of the binary representation of 6:
y = toggle_nth_bit(6, 0)
print(y)

# Toggle the 0th bit of the binary representation of 7:
z = toggle_nth_bit(y, 0)
print(z)
