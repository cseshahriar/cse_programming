"""
    A queue is an object(an abstract data structure - ADT) that allows the 
    following operations

    - enqueue : add an element to the end of the queue
    - Dequeue : remove an element from the front of the queue
    - isEmpty: Check if the queue is empty
    - isFull: Check if the queue is full
    - Peek: get the value of the front of the queue without removing it
    types: Circular queue, Priority queue, Dequeue
"""


class Queue(object):
    def __init__(self):
        self.queue = []

    # Add an element
    def enqueue(self, item):
        self.queue.append(item)  # first in

    # remove an element
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)  # first out

    # Display the queue
    def display(self):
        print(self.queue)

    def size(self):
        return len(self.queue)

queue = Queue()

# add an elements
queue.enqueue(1)
queue.display()

queue.enqueue(3)
queue.display()

queue.enqueue(2)
queue.display()

queue.enqueue(4)
queue.display()

# remove an element
queue.dequeue()

queue.display()
