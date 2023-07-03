class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def show(self):
        if self.head is None:
            print("Linked list is empty")
            return

        current_node = self.head
        output = ""
        while current_node:
            output += str(current_node.data) + " -> "
            current_node = current_node.next
        print(output)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def convert_to_linked_list(self, data_list):
        self.head = None
        for element in data_list:
            self.insert_at_end(element)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                return
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                new_node = Node(data, itr.next)
                itr.next = new_node
                return
            itr = itr.next
            count += 1


if __name__ == "__main__":
    ll = LinkedList()
    ll.convert_to_linked_list(["apple", "banana", "cantaloupe", "durian"])
    ll.show()
    ll.insert_at(0, "figs")
    ll.show()
    ll.insert_at(4, "cats")
    ll.show()
