from List import Node


class Stack:
    """ the stack is implemented on a list """

    def __init__(self):
        self.head = None
        self.lenght = 0

    # append new element to stack
    def push(self, value):

        node = Node(value)

        if self.lenght == 0:
            self.head = node
            self.lenght+=1
        else:
            node.next = self.head
            self.head = node
            self.lenght += 1

    # return element to stack
    def peek(self):
        return self.head.returnValue()

    # delete and return element to stack
    def pop(self):
        if self.lenght==0:
            return
        else:
            curr = self.head
            self.head = self.head.next
            print(curr.returnValue())
            self.lenght-=1
            return curr.returnValue()


    # task
    def task(self):
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        self.push(curr.returnValue())


    # return stack
    def get_stack(self):
        if self.head is None:
            return "Нет элементов"
        string = ""
        curr = self.head
        while curr.next is not None:
            string = string + str(curr.returnValue()) + " "
            curr = curr.next
        string = string + str(curr.returnValue())
        return string