x = 500
y = 2000


def recursive_multiply(x, y):

    # This cuts down on the total number of
    # recursive calls:
    if x < y:
        return recursive_multiply(y, x)
    if y == 0:
        return 0
    return x + recursive_multiply(x, y-1)

print(x * y)
print(recursive_multiply(x, y))
