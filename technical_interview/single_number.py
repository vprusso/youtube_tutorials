# YouTube Video: https://www.youtube.com/watch?v=r0CAz6MdgEg
"""
Given an array of integers, every element appears twice except for one.
Find that single one.

Note: Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?

Example :

Input : [1, 2, 2, 3, 1]
Output : 3

{ element : number of occurences }

i = 0 { 1 : 1 }
i = 1 { 1 : 1, 2 : 1}
i = 2 { 1 : 1, 2 : 2}
i = 3 { 1 : 1, 2 : 2, 3 : 1}
i = 4 { 1 : 2, 2 : 2, 3 : 1}

XOR : b1 | b2
    0   0 : 0
    0   1 : 1
    1   0 : 1
    1   1 : 0
"""

nums = [1, 2, 2, 3, 1]
ans = 0
for i in range(len(nums)):
    ans ^= nums[i]

print(ans)
