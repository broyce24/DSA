class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return not bool(self.size)

    def push(self, data):
        new_node = Node(data, self.head)
        self.head = new_node
        self.size += 1
        return data

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data
    def __str__(self):
        if self.is_empty():
            return 'Stack is empty!'
        itr = self.head
        output = ''
        while itr:
            output += str(itr.data) + ' '
            itr = itr.next
        return output