# linked list implementation 
from typing import Any

class Node:
    #create a node
    def __init__(self, item: Any, next: Any) -> None:
        self.item = item
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.size = 0

    def add(self, item: Any) -> None:
        self.head = Node(item, self.head)
        self.size += 1

    def remove(self) -> Any:
        if self.is_empty():
            return None
        
        else:
            item = self.head.item
            self.head = self.head.next
            self.size -= 1
            return item
    
    def is_empty(self) -> bool:
        return self.head is None

    def __str__(self) -> str:
        """
        >>> l = LinkedList()
        >>> l.add(20)
        >>> l.add(2)
        >>> l.add(23)
        >>> print(l)
        20 --> 2 --> 23
        """
        if not self.is_empty:
            return ""

        else:
            iterate = self.head
            item_str = ""
            item_list = []

            while iterate:
                item_list.append(str(iterate.item))
                iterate = iterate.next
            item_str = " --> ".join(item_list)

            return item_str
    
    def __len__(self) -> int:
        """
        >>>l = LinkedList()
        >>> len(l)
        0
        >>> l.add("a")
        >>> len(l)
        """
        return self.size