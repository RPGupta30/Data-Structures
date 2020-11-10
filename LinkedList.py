class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_last(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while True:
            if last_node.next is None:
                break
            last_node = last_node.next
        last_node.next = new_node

    def insert_at_head(self, new_node):
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node
        del temp_node

    def length_of_list(self):
        lenght = 0
        current_node = self.head
        while True:
            lenght += 1
            current_node = current_node.next
            if current_node.next is None:
                break
        return lenght

    def print_list(self):
        if self.head is None:
            print('List is empty')
        current_node = self.head
        while True:
            print(current_node.data)
            if current_node.next is None:
                return
            current_node = current_node.next

    def insert_at_position(self, new_node, position):
        if position == 0:
            self.insert_at_head(new_node)
            return
        elif position <0 or position > self.length_of_list():
            print('Index Error : Index is out of range.')
            return
        else:
            current_node = self.head
            current_position = 0
            while True:
                if current_position == position:
                    previous_node.next = new_node
                    new_node.next = current_node
                    break
                previous_node = current_node
                current_node = current_node.next
                current_position += 1


def build_linked_list():
    linkedList = LinkedList()
    first_node = Node(10)
    linkedList.insert_at_last(first_node)
    second_node = Node(20)
    linkedList.insert_at_last(second_node)
    third_node = Node(30)
    linkedList.insert_at_last(third_node)
    fourth_node = Node(5)
    linkedList.insert_at_head(fourth_node)
    print('Linked List before adding 100')
    linkedList.print_list()

    node = Node(100)
    linkedList.insert_at_position(node, 2)
    print('Linked List after adding 100')
    linkedList.print_list()


if __name__ == '__main__':
    build_linked_list()


