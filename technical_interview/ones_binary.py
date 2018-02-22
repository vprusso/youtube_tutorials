# YouTube Video: https://www.youtube.com/watch?v=P9EFWCvD_yU
"""
Problem: Find the number of 1s in the binary representation of a number.
For example:

num_ones(2) = 1 --> since "10" is the binary representation of the number "2".

num_ones(5) = 2 --> since "101" is the binary representation of the number "5"

etc.
"""


num = 2
# num = 5
# num = 11

# Approach 1 (using Python's "bin" function):
one_sum = 0
bin_rep = bin(num)[2:]
for i in bin_rep:
    one_sum += int(i)
print(one_sum)

# Approach 2 (without Python's "bin" function):
one_sum = 0
while num:
    one_sum += num & 1
    num >>= 1
print(one_sum)
