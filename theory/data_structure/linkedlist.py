class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.back = None

    def insert_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.back = new_node  # First node
        self.head = new_node

    def insert_back(self, data):
        new_node = Node(data)
        if self.back is None:
            self.head = self.back = new_node
        else:
            self.back.next = new_node
            new_node.prev = self.back
            self.back = new_node

    def delete_front(self):
        if not self.head:
            return
        temp = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.back = None  # List is now empty
        del temp

    def delete_back(self):
        if not self.back:
            return
        temp = self.back
        self.back = self.back.prev
        if self.back:
            self.back.next = None
        else:
            self.head = None  # List is now empty
        del temp

    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

# Test
ll = LinkedList()
ll.insert_back(1)
ll.insert_back(2)
ll.insert_back(3)
ll.insert_back(4)
ll.traverse()
