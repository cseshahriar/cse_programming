# A single node of a singly linked list


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, new_value):
        node = Node(new_value)
        node.next = self.head
        self.head = node

    def insertAtEnd(self,new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while(last_node.next):
            last_node = last_node.next
            last_node.next = new_node

    def insert(self, data):
        newNode = Node(data)
        if(self.head):
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def insertAfter(self, prev_node, new_value):
        if prev_node is None:
            print("Previous node is empty")
        new_node = Node(new_value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def deleteNode(self,key):
        temp = self.head
        if temp is None:
            print("Can't perform deletion")
            return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        prev.next = temp.next
        temp = None

    def reverseLinkedList(self):
        prev = None
        curr = self.head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def deleteLinkedList(self):
        curr = self.head
        while curr:
            temp = curr.next
            del curr.data
            curr = temp

    def printLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next


# Singly Linked List with insertion and print methods
LL = LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()

# ref: https://pythonistaplanet.com/linked-list/