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
        node = Node(data, self.head)
        self.head = node

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
        if self.head is None:
            return
        
        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

if __name__ == "__main__":
    ll = DoublyLinkedList()
    ll.insert_at_beginning(32)
    ll.insert_at_beginning(34)
    ll.insert_at_beginning(290)

    ll.insert_at_end(413)
    ll.print()