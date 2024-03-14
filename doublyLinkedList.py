'''Implement doubly linked list. The only difference with regular linked list is that double linked has prev node reference as well. 
That way you can iterate in forward and backward direction. Your node class will look this this,
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
Add following new methods,

def print_forward(self):
    # This method prints list in forward direction. Use node.next

def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.'''


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def print(self):

        if self.head is None:
            print("empty linked list")

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '<--->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node
        new_node.prev = last_node

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head

        while itr:
            count += 1
            itr = itr.next

        return count
            


if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert_at_beginning(32)
    ll.insert_at_beginning(34)
    ll.insert_at_beginning(290)

    ll.insert_at_end(413)
    ll.insert_at_end(20)
    ll.insert_at_end(324)
    ll.insert_values(["Papaya","Mango","orange","Peech"])
    print(f"Length of the linked list is : {ll.get_length()}")
    ll.print()