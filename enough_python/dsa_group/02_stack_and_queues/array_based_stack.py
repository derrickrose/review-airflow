class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size() == 0:
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.size() == 0:
            raise IndexError("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return " -> ".join(map(str, self.items))


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.size())
print(stack)
print(stack.pop())
print(stack)
