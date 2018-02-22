# YouTube Video: https://www.youtube.com/watch?v=cXxkvq3u_f8


class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def reverse_string(stack, input_str):

    # Loop through the string and push contents
    # character by character onto stack.
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str = ""
    while not stack.is_empty():
        rev_str += stack.pop()

    return rev_str


stack = Stack()    
input_str = "Hello"

print(reverse_string(stack, input_str))


#print(input_str[::-1])

