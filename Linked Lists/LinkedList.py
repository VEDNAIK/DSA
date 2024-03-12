class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    def insert_in_front(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_index(self, index: int, value):
        count = 0
        current_node = self.head
        new_node = Node(value)
        if index == 0:
            self.insert_in_front(value)
        else:
            while count+1 != index and current_node.next is not None:
                count = count + 1
                current_node = current_node.next
            if count+1 == index and current_node.next is not None:
                new_node.next = current_node.next
                current_node.next = new_node
            if current_node.next is None:
                current_node.next = new_node
                print("Index not found so value added at the end")

    def insert_at_back(self, value):
        current_node = self.head
        new_node = Node(value)
        if self.head is None:
            self.insert_in_front(value)
        else:
            while current_node.next is not None:
                current_node = current_node.next
            if current_node.next is None:
                current_node.next = new_node

    def delete_head(self):
        if self.head is not None:
            self.head = self.head.next
        else:
            print("EMPTY LIST!!")

    def delete_at_index(self,index):
        count = 0
        current_node = self.head
        if index == 0:
            self.delete_head()
        else:
            while count+1 != index and current_node.next is not None:
                count = count+1
                current_node = current_node.next
            if count+1 == index and current_node.next is not None:
                current_node.next = current_node.next.next
            if current_node.next is None:
                print("Index out of range")

    def delete_from_end(self):
        current_node = self.head
        if current_node is None:
            print("Empty List")
        elif current_node.next is None:
            self.head = None
        else:
            while current_node.next.next is not None:
                current_node = current_node.next
            if current_node.next.next is None:
                current_node.next = None

    def search_and_delete(self,value):
        current_node = self.head
        if self.head.data == value:
            self.delete_head()
        else:
            while current_node.next.data != value and current_node.next.next is not None:
                current_node = current_node.next
            if current_node.next.data == value:
                current_node.next = current_node.next.next
            else:
                print("Value not found")

    def edit_at_index_value(self, index, value):
        count = 0
        current_node = self.head
        if index == 0:
            self.head.data = value
        else:
            while count != index and current_node.next is not None:
                count = count + 1
                current_node = current_node.next
            if count == index:
                current_node.data = value
            else:
                print("Index out of range")

    def length(self):
        count = 1
        current_node = self.head
        if current_node is None:
            print("Empty List")
        else:
            while current_node.next is not None:
                count = count+1
                current_node = current_node.next
            print("Length of Linked list is : ", count)

    def print_list(self):
        current_node = self.head
        print("List : ")
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


x = Linkedlist()
x.insert_in_front(1)
x.insert_in_front(2)
x.insert_at_back(3)
x.insert_in_front(4)
x.insert_in_front(5)
x.insert_at_back(6)
x.insert_at_index(2,8)
x.insert_at_index(8000,1000)
x.print_list()
x.delete_head()
x.print_list()
x.delete_from_end()
x.print_list()
x.delete_at_index(1)
x.print_list()
x.edit_at_index_value(4,3)
x.print_list()

x.search_and_delete(4)
x.print_list()
x.length()
