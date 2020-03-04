from List import Node


class Queue:

    """ the queue is implemented on a linked list """
    def __init__(self):
        self.length = 0
        self.head = None
        self.last = None
        self.K = 1000   # отвечает за переполнение очереди (по заданию)

    def insert(self, value):
        node = Node(value)
        node.next = None
        if self.length == 0:
            # if list is empty, the new node is head and last
            self.head = self.last = node
        else:
            # find the last node
            last = self.last
            # append the new node
            last.next = node
            self.last = node
        self.length += 1

    def remove(self):
        if self.length == 0:
            return
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        if self.length == 0:
            self.last = None
        return value


    def get_queue(self):
        if self.head is None:
            return "Нет элементов"
        string = ""
        curr = self.head
        while curr.next is not None:
            string = str(curr.returnValue()) + " " + string
            curr = curr.next
        string = str(curr.returnValue()) + " " + string
        return string

    # изменение макисмальной длины очереди (переполнение)
    def set_K(self, K):
        self.K = K

    # задание
    def task(self):
        # проверяем что очередь не пуста и не переполнена
        if self.length < 1 or self.length > self.K:
            return

        curr = Node(self.remove())
        self.insert(curr.returnValue())