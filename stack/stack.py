"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""


class Stack:
    stack = []
    def __init__(self, size, value):
        self.size = 0
        # self.storage = ?

    def __len__(self):
        pass

    def push(self, value):
        if self.size = -1:
            self.stack.append(value)
        elif len(self.stack) < self.size:
            self.stack.append(value)
        else:
            print('cant add item')

    def pop(self):
        if len(self.stac) > 0:
            temp = self.stack[-1]
            self.stack.pop()
            return temp
        else:
            print('stack is already empty')


