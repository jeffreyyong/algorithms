class Stack:
    # initialize an empty list

    def __init__(self):
        self.items = []

    # push a new item to the last index
    def push(self, item):
        self.items.append(item)

    # remove the last item
    def pop(self):
        if not self.items:
            return None
        return self.items.pop()

    def peek(self):
        if not self.items:
            return None
        return self.items[-1]

class MaxStack:

    def __init__(self):
        self.stack = Stack()
        self.maxs_stack = Stack()

    
    def push(self, item):
        self.stack.push(item)
        if self.maxs_stack.peek() is None or item >= self.maxs_stack.peek():
            self.maxs_stack.push(item)

    def pop(self):
        item = self.stack.pop()
        if item == self.maxs_stack.peek():
            self.maxs_stack.pop()
        return item

    def get_max(self):
        return self.maxs_stack.peek()




