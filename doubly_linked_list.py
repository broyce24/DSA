class Node:
    def __init__(self, prev=None, data=None, next=None):
        self.prev = prev
        self.data = data
        self.next = next


class DoublyLinkedList:
    def __init__(self, values=None):
        self.size = 0
        self.head = None
        if values is not None:
            for value in values:
                self.append(value)

    def insert_at_beginning(self, data):
        new_node = Node(None, data, self.head)
        self.head = new_node
        self.size += 1

    def append(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        new_node = Node(itr, data, None)
        itr.next = new_node
        self.size += 1

    def print(self):
        if self.head is None:
            return 'DoublyLinkedList is empty!'
        itr = self.head
        output = '<- ' + str(itr.data) + ' ->'
        while itr.next:
            itr = itr.next
            output += '<- ' + str(itr.data) + ' ->'
        print(output)

    def insert_values(self, values):  # append values from iterable onto DLL
        for val in values:
            self.append(val)

    def clear(self):
        self.head = None
        self.size = 0

    def get_length(self):
        return self.size

    def remove_at(self, index):
        if index < 0 or index >= self.size:
            raise Exception("Invalid index!")

        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return

        itr = self.head
        i = 0
        while itr:
            if i == index - 1:
                itr.next = itr.next.next
                if index < self.size - 1:
                    itr.next.prev = itr
            i += 1
            itr = itr.next
        self.size -= 1

    def insert_at(self, index, val):
        if index < 0 or index >= self.size:
            raise Exception("Invalid index!")
        if index == 0:
            self.insert_at_beginning(val)
            return
        itr = self.head
        i = 0
        while itr:
            if i == index - 1:
                new_node = Node(itr, val, itr.next)
                itr.next = new_node
                itr.next.next.prev = new_node
            i += 1
            itr = itr.next

def main():
    animals = ['cat', 'dog', 'mouse', 'rat']
    some_vals = ['a', 2, False, True]
    dll = DoublyLinkedList()
    dll.insert_values(animals)
    dll.print()
    dll.insert_at(3, 'hello')
    dll.print()


if __name__ == '__main__':
    main()