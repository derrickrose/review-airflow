class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

    def __str__(self):
        print(self.item)


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = 0

    def push(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.items += 1

    def pop(self):
        if self.head is None:
            raise IndexError("Queue is empty")
        item = self.head.item
        self.head = self.head.next
        return item

    def peek(self):
        if self.head is None:
            raise IndexError("Queue is empty")
        return self.head.item

    def size(self):
        return self.size

    def __str__(self):
        node = self.head
        items = []
        while node:
            items.append(str(node.item))
            node = node.next
        return " -> ".join(reversed(items))


queue = Queue()
queue.push(1)
queue.push(2)
queue.push(3)
print(queue.size())
print(queue)
print(queue.pop())
print(queue)
