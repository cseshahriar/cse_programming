class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(11)
b = Node(52)
c = Node(18)

a.next = b
b.next = c

print(a.data)
print(a.next.data)
print(a.next.next.data)
head = a


def traverse(head):
    current = head
    while current != None:
        print(current.data)
        current = current.next

print(traverse(head))