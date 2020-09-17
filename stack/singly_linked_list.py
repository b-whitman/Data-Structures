class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def set_next_node(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next_node(self.head)
            self.head = new_node

    def add_to_tail(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next_node(new_node)
            self.tail = new_node

    def remove_head(self):
        if self.head is None:
            return None
        else:
            ret_value = self.head.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.get_next_node()
            return ret_value

    def remove_tail(self):
        if self.tail is None:
            return None
        else:
            ret_value = self.tail.get_value()
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                current_node = self.head
                last_node = self.head
                while current_node.get_next_node() != None:
                    last_node = current_node
                    current_node = current_node.get_next_node()
                self.tail = last_node
                self.tail.set_next_node(None)
            return ret_value

    def contains(self, value):
        pass

    def get_max(self):
        pass