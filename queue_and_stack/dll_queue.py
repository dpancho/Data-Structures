from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('./doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = DoublyLinkedList()

    # add to back of queue
    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    # Remove and return item from front of queue
    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    # Number of Items in queue
    def len(self):
        return self.size
