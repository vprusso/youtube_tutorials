
# (John, Carmack), (John, Romero), (Bill, Gates), (Elon, Musk) 
# -->
# (John, Carmack), (Bill, Gates), (Elon, Musk)
# or
# (John, Romero), (Bill, Gates), (Elon, Musk)
A = [("John", "Carmack"), ("John" "Romero"), ("Bill", "Gates"), ("Elon", "Musk")]


class FirstLastName():
    def __init__(self, first_name, last_name):
        self.first_name = first_name 
        self.last_name = last_name 

    def __str__(self):
        return self.first_name + " " + self.last_name

    def __eq__(self, other):
        return self.first_name == other.first_name

    def __lt__(self, other):
        return (self.first_name < other.first_name 
                if self.first_name != other.first_name else
                self.last_name < other.last_name)


A = [FirstLastName("John", "Carmack"), FirstLastName("John", "Romero"), FirstLastName("Bill", "Gates"), FirstLastName("Elon", "Musk")]


def remove_duplicate(A):
    A.sort()

    for name in A:
        print(name)
    print("\n")

    write_idx = 1
    for name in A:
        if name != A[write_idx - 1]:
            A[write_idx] = name
            write_idx += 1
    del A[write_idx:]

    for name in A:
        print(name)
    print("\n")

    return A


remove_duplicate(A)

