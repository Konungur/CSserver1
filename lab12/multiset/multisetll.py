from node import *        

# A class implementing Multiset as a linked list.

class Multiset:

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    def __len__(self):
        res = 0
        tmp_md = self._head
        while tmp_md is not None:
            res +=1
            tmp_md = tmp_md.next
        return res

    def half_len(self):
        id = 0
        tmp_md = self._head
        half_pos = len(self) / 2
        mll = Multiset
        """
        while id < half_pos:
            id +=1
            half_pos = half_pos.next
        return id, len(tmp_md) - len(half_pos)
        """
        while tmp_md is not None:
            id = 1
            if id < half_pos:
                mll.add(tmp_md.data)
            else:
                mll.add(tmp_md.data)


if __name__ == "__main__":
    n  = format()