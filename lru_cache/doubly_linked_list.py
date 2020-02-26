"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.head and not self.tail:  # if there is no head or tail the list is empty
            self.head = new_node  # new node is head and tail
            self.tail = new_node
        else:
            new_node.next = self.head  # make this node the head
            self.head.prev = new_node  # rearrange the pointers, this becoming new head
            self.head = new_node

    def remove_from_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1  # if empty and we add something to list
        if not self.head and not self.tail:  # if there is no head or tail the list is empty
            self.head = new_node  # new node is head and tail
            self.tail = new_node
        else:
            new_node.prev = self.tail  # make this node the head
            self.tail.next = new_node  # rearrange the pointers, this becoming new head
            self.tail = new_node

    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.value)
        return value

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    def delete(self, node):
        self.length -= 1

        # If LL is empty
        if not self.head and not self.tail:
            return
        # If head and tail
        if self.head == self.tail:  # if there's only one item in the list
            self.head = None  # we don't want to delete the entire list, just get rid of the pointers
            self.tail = None  # garbage collector will handle it for us
        # head
        elif self.head == node:
            self.head = self.head.next
            node.delete()
        # tail
        elif self.tail == node:
            self.tail = self.tail.prev
            node.delete()
        # otherwise
        else:
            node.delete()

    def get_max(self):
        if self.head is None:
            return None
        max_value = self.head.value
        current = self.head
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value
