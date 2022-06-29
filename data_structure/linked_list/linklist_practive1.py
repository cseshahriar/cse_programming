""" [data|next] -> [data|next] data[data|next]"""
class Node:
    def __str__(self, value):
        self.value = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None  # store a node [data|next]

if __name__ == '__main__':
    linked_list  = Linkedlist()  # linklist

    # assign item values
    linked_list.head = Node(1)  # first node assign in link list head
    second = Node(2)  # node
    third = Node(3)  # node

    # connect nodes
    linked_list.head.next = second # first node next = second node
    second.next = third  # second node next = third node

    # print
    while linked_list.head != Node:
        print(linked_list.head.value, end='')
        linked_list.head = linked_list.head.next


