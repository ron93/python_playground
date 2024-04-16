from typing import Any

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data 
        self.next = None

    def __repr__(self) -> Any:
        return f'Node({ self.data })'

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __iter__(self) -> None:
        node = self.head 
        while node:
            yield node.data
            node = node.next

    def __len__(self) -> int:
        """ 
        Return length of linked list

        >>> l = LinkedList()
        >>> len(l)
        o
        >>> l.insert_head("head")
        >>> len(l)
        1
        >>> l.insert_tail("tail")
        >>> len(l)
        >>> 2
        >>> l.delete_tail()
        >>>len(l)
        1
        >>> l.delete_head()
        >>> len(l)
        0 
        """

        return len(tuple(iter(self)))

    def __repr__(self) -> Any:
        """
        string representation of linked list

        """
        return "->".join([str(item) for item in self])

    def __getitem__(self, index) -> Any:
        """
       Indexing Support. Used to get a node at particular position
        >>> linked_list = LinkedList()
        >>> for i in range(0, 10):
        ...     linked_list.insert_nth(i, i)
        >>> all(str(linked_list[i]) == str(i) for i in range(0, 10))
        True
        >>> linked_list[-10]
        Traceback (most recent call last):
        ...
        ValueError: list index out of range.
        >>> linked_list[len(linked_list)]
        Traceback (most recent call last):
        ...
        ValueError: list index out of range.
        """
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        for i ,node in enumerate(self):
            return node

    # Used to change the data of a particular node
    def __setitem__(self, index, data):
        """
        >>> l = LinkedList()
        >>> for i in range(0, 10):
        ...     l.insert_nth(i, i)
        >>> l[0] = 666
        >>> l[0]
        666
        >>> l[5] = -666
        >>> l[5]
        -666
        >>> l[-10] = 666
        Traceback (most recent call last):
        ...
        ValueError: list index out of range.
        >>> l[len(l)] = 666
        Traceback (most recent call last):
        ...
        ValueError: list index out of range.
        """
        if not 0 <= index < len(self):
            raise ValueError("list index out of range.")
        current = self.head
        for i in range(index):
            current = current.next
        current.data = data

    def insert_head(self, data) -> None:
        self.insert_nth(0, data)
    
    def insert_tail(self, data) -> None:
        self.insert_nth(len(self), data)

    def insert_nth(self, index: int, data) -> None:
        if not 0 <= index <= len(self):
            raise IndexError("List index out of range")
        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        elif index == 0:
            new_node.next = self.head #link new node to head
            self.head = new_node

        else:
            temp = self.head
            for _ in range(index -1):
                temp = temp.next
                temp.next = new_node

    def print_list(self) -> None:
        #print node data
        print(self)
    def delete_head(self):
        return self.delete_nth(0)

    def delete_tail(self):  # delete from tail
        return self.delete_nth(len(self) - 1)


    def delete_nth(self, index: int = 0):
        if not 0 <= index <= len(self) - 1:  # test if index is valid
            raise IndexError("list index out of range")
        delete_node = self.head  # default first node
        if index == 0:
            self.head = self.head.next
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
        return delete_node.data

    def is_empty(self) -> bool:
        return self.head is None

    def reverse(self):
        prev = None
        current = self.head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.head = prev


def test_singly_linked_list() -> None:
    """
    >>> test_singly_linked_list()
    """
    l = LinkedList()
    assert l.is_empty() is True
    assert str(l) == ""

    try:
        l.delete_head()
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    try:
        l.delete_tail()
        assert False  # This should not happen.
    except IndexError:
        assert True  # This should happen.

    for i in range(10):
        assert len(l) == i
        l.insert_nth(i, i + 1)
    assert str(l) == "->".join(str(i) for i in range(1, 11))

    l.insert_head(0)
    l.insert_tail(11)
    assert str(l) == "->".join(str(i) for i in range(0, 12))

    assert l.delete_head() == 0
    assert l.delete_nth(9) == 10
    assert l.delete_tail() == 11
    assert len(l) == 9
    assert str(l) == "->".join(str(i) for i in range(1, 10))

    assert all(l[i] == i + 1 for i in range(0, 9)) is True

    for i in range(0, 9):
        l[i] = -i
    assert all(l[i] == -i for i in range(0, 9)) is True


def main():
    from doctest import testmod

    testmod()

    l = LinkedList()
    l.insert_head(input("Inserting 1st at head ").strip())
    l.insert_head(input("Inserting 2nd at head ").strip())
    print("\nPrint list:")
    l.print_list()
    l.insert_tail(input("\nInserting 1st at tail ").strip())
    l.insert_tail(input("Inserting 2nd at tail ").strip())
    print("\nPrint list:")
    l.print_list()
    print("\nDelete head")
    l.delete_head()
    print("Delete tail")
    l.delete_tail()
    print("\nPrint list:")
    l.print_list()
    print("\nReverse linked list")
    l.reverse()
    print("\nPrint list:")
    l.print_list()
    print("\nString representation of linked list:")
    print(l)
    print("\nReading/changing Node data using indexing:")
    print(f"Element at Position 1: {l[1]}")
    l[1] = input("Enter New Value: ").strip()
    print("New list:")
    print(l)
    print(f"length of linked_list is : {len(l)}")


if __name__ == "__main__":
    main()