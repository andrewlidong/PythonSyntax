# Approach 1

stack = [4, 5, 6]
stack.append(7)
stack.pop()

# Approach 2:


class Stack:
    def __init__(self):
        self.stack = []

        # check if empty

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, p):
        self.stack.append(p)

    def pop(self):
        return self.stack.pop()
