# import sys
# sys.path.append('./binary_search_tree')
from dll_stack import Stack
from dll_queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if input is less than parent value, move to left
        if value < self.value:
            # Create a new binary search tree inputting incoming as value
            if self.left == None:
                self.left = BinarySearchTree(value)
            # if there's already an element, slide down and make BST with recursion
            else:
                self.left.insert(value)
        # if input is more, move to right pointer
        else:
            # Create a new BST inputting incoming value as value
            if self.right == None:
                self.right = BinarySearchTree(value)
            # if there's already an element, slide down and make BST with recursion
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # if target value is > parent, traverse right
        elif target > self.value:
            # if self.right = None return False
            if self.right == None:
                return False
            # else, call contains recursively
            else:
                return self.right.contains(target)
        # if not, traverse left
        elif target < self.value:
            # if current value = None return False
            if self.left == None:
                return False
            # else call contains recursively
            else:
                return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right != None:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        # recursive go left
        if self.left != None:
            self.left.for_each(cb)
        # recursive go right
        if self.right != None:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left is not None:
           self.left.in_order_print(self.left)
        print(self.value)
        if self.right is not None:
            self.right.in_order_print(self.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal

    #     BFT Steps:
    # initialize a queue
    # push root to queue
    # while stack not empty
    # pop top item out of queue into temp
    # DO THE THING!!!!!!
    # if temp has right right put into queue
    # if temp has left left put into queue

    def bft_print(self, node):
        if node is None:
            return
        q = Queue() #make your queue
        q.enqueue(node)#adds to back of queue
        while q.size > 0:
            node = q.dequeue() #remove and return from front of queue
            print(node.value)
            if node.left is not None: #same for left side
                q.enqueue(node.left)
            if node.right is not None: #same for right side
                q.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal

    #     DFT Steps:
    # initialize a stack
    # push root to stack
    # while stack not empty
    # pop top item out of stack into temp
    # DO THE THING!!!!!!
    # if temp has right right put into stack
    # if temp has left left put into stack

    def dft_print(self, node):
        if node is None:
          return
        s = Stack() #make that stack
        s.push(node) #push her out 
        while s.size > 0:
            node = s.pop()
            print(node.value)
            if node.left is not None:
                s.push(node.left)
            if node.right is not None:
                s.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
