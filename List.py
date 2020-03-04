# List Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def returnValue(self):
        return self.value


class List:
    def __init__(self):
        self.head = None     # First element

    def length(self):
        """return length list"""
        if self.head is None:
            return 0
        len = 0
        curr = self.head
        while curr.next is not None:
            len += 1
            curr = curr.next
        return len + 1

    def append(self, value):
        """ New elements """
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def get_list(self):
        if self.head is None:
            return "Нет элементов"
        string = ""
        curr = self.head
        while curr.next is not None:
            string = string + str(curr.returnValue()) + " "
            curr = curr.next
        string = string + str(curr.returnValue())
        return string

    def clear_list(self):
        """Clear list"""
        self.head = None