# Stack implementation in python

# creating a stack
class Stack:
    def __init__(self):
        self.stack = []

    def stack_check_empty(self):
        return len(self.stack) == 0

    def stack_push(self, item):
        self.stack.append(item)

    def stack_pop(self):
        if(self.stack_check_empty()):
            return "stack is empty"

        return self.stack.pop()

    def stack_top(self):
        if not self.stack_check_empty():
            return self.stack[0]

    def stack_size(self):
        return len(self.stack)

    def __str__(self):
        if not self.stack_check_empty():
            return ", ".join(str(x) for x in self.stack)
        return []

stack = Stack()

stack.stack_push(1)
stack.stack_push(2)
stack.stack_push(3)
stack.stack_push(4)

print('size ', stack.stack_size())
print('peek ', stack.stack_top())

print('stack', stack.stack)

stack.stack_pop()
print('stact', stack)
