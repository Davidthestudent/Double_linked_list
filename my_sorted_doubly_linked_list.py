from my_list_node import MyListNode


class MySortedDoublyLinkedList:
    """A base class providing a doubly linked list representation."""

    def __init__(self, head: 'MyListNode' = None, tail: 'MyListNode' = None, size: int = 0) -> None:
        """Create a list and default values are None."""
        self._head = head
        self._tail = tail
        self._size = size

    def __len__(self) -> int:
        """Return the number of elements in the list."""
        return self._size

    def __str__(self) -> str:
        """Return linked list in string representation."""
        result = []
        node = self._head
        while node:
            result.append(node.elem)
            node = node.next_node
        return str(result)

    def get_value(self, index: int) -> int:
        # check if index is int
        if isinstance(index, int):
            if 0 <= index < self._size:  # check if index inside the range
                node = self._head  # starting point is the head of list
                for _ in range(index):  # starting traversing the list
                    node = node.next_node  # moving the pointer to the next element
                return node.elem  # returning the element with the set index
            else:
                raise ValueError("f index is out of range ")  # raising error index is out of range
        else:
            raise ValueError("f The passed index is not an int ")  # raising error index is not an int

    def search_value(self, val: int) -> int:
        # check is val is int
        if not isinstance(val, int):
            raise ValueError(f" The given value is not integer number")  # raising error val is not int
        index = 0  # making index to count it
        node = self._head  # starting point is the head of the list
        while node:  # starting traversing  the list
            if node.elem == val:  # checking for equality
                return index  # return the index of an element
            node = node.next_node  # moving pointer
            index += 1  # adding one to index
        return -1

    def insert(self, val: int) -> None:
        # check if val is int
        if not isinstance(val, int):
            raise ValueError(f" The given value is not integer number")  # raising error val is not int
        new_node = MyListNode(val)  # Creating a new node with the given value
        if not self._head or val <= self._head.elem:  # if list is empty or val < head
            new_node.next_node = self._head  # Inserting the new node before the current head
            if self._head:  # Inserting the new node before the current head
                self._head.prev_node = new_node  # Set the prev_node of the head to the new node if the head exists
            self._head = new_node  # Update the head to point to the new node
        else:
            node = self._head  # traversing the list if the element is not before the head
            while node.next_node and node.next_node.elem < val:
                node = node.next_node
            new_node.next_node = node.next_node  # Inserting the new node between node and node.next_node
            new_node.prev_node = node  # the previous node for a new node points to the node
            if node.next_node:  # if it is not the end of the list
                node.next_node.prev_node = new_node  # for previous node the next node is new_node
            node.next_node = new_node  # the next node of the node points to the new_node
        self._size += 1

    def remove_first(self, val: int) -> bool:
        # check if val is int
        if not isinstance(val, int):
            raise ValueError("The given value is not an integer number")  # raising error val is not int

        node = self._head  # starting point is the head of the list
        while node:  # traversing the list
            if node.elem == val:  # if node element equal val
                # If the node to be deleted is the head
                if node == self._head:
                    self._head = node.next_node
                    if self._head:
                        self._head.prev_node = None
                # If the node to be deleted is the tail
                if node == self._tail:
                    self._tail = node.prev_node
                    if self._tail:
                        self._tail.next_node = None
                # If the node to be deleted is in the middle
                else:
                    if node.prev_node:
                        node.prev_node.next_node = node.next_node
                    if node.next_node:
                        node.next_node.prev_node = node.prev_node

                # Clear references from the node being deleted
                node.next_node = None
                node.prev_node = None
                node.elem = None

                self._size -= 1  # Update size
                return True  # the element deleted return true
            node = node.next_node  # traverse the list
        return False  # if we do not delete the element return False

    def remove_all(self, val: int) -> bool:
        # check if val is int
        if not isinstance(val, int):
            raise ValueError("The given value is not an integer number")  # raising error val is not int

        removed = False  # creating a bool variable to see if we have removed an element
        node = self._head  # starting point
        while node:  # traverse the list
            next_node = node.next_node  # Store the next node before potentially removing the current one

            if node.elem == val:  # if node element equal val
                if node == self._head:  # If the node to be deleted is the head
                    self._head = node.next_node
                    if self._head:
                        self._head.prev_node = None
                    else:
                        self._tail = None
                # If the node to be deleted is the tail
                elif node == self._tail:
                    self._tail = node.prev_node
                    if self._tail:
                        self._tail.next_node = None
                else:  # if the node to be deleted is in the middle
                    if node.prev_node:
                        node.prev_node.next_node = node.next_node
                    if node.next_node:
                        node.next_node.prev_node = node.prev_node

                # Clear the references of the removed node
                node.next_node = None
                node.prev_node = None
                node.elem = None
                self._size -= 1  # Update size

                removed = True  # we have removed the element removed is True

            node = next_node  # Move to the next node

        return removed  # return bool

    def remove_duplicates(self) -> None:
        unique_elements = set()  # making set of unique values to remove duplicates
        node = self._head  # starting point is the head of list
        while node:  # traverse the list
            if node.elem in unique_elements:  # if the element in the unique elements we have to delete it
                if node == self._head:  # If the node to be deleted is the head
                    self._head = node.next_node
                    if self._head:
                        self._head.prev_node = None
                elif node == self._tail:  # If the node to be deleted is the tail
                    self._tail = node.prev_node
                    if self._tail:
                        self._tail.next_node = None
                else:  # If the node to be deleted is in the middle
                    node.prev_node.next_node = node.next_node
                    if node.next_node:
                        node.next_node.prev_node = node.prev_node
                self._size -= 1  # Update the size after removing an element
            else:
                unique_elements.add(node.elem)  # if we do not find the element in the unique we add it
            node = node.next_node  # continue to the next element

    def filter_n_max(self, n: int) -> None:
        # check if val is int
        if not isinstance(n, int) or n <= 0 or n > self._size:
            raise ValueError(f" The n is out of range of the list or is not an integer number")
            # raising error val is not int
        node = self._head  # starting point is the head
        values = []  # an empty array to add node elements
        while node:  # traverse the list and add elements
            values.append(node.elem)
            node = node.next_node
        max_values = sorted(values, reverse=True)[:n]  # sort the list to find n max of numbers
        node = self._head  # starting point is the head
        while node:  # traverse the list
            next_node = node.next_node  # Store the next node before potentially removing the current one

            if node.elem not in max_values:  # if element not in max_values delete it
                if node == self._head:  # if element is the head
                    self._head = node.next_node
                    if self._head:
                        self._head.prev_node = None
                    else:
                        self._tail = None
                elif node == self._tail:  # if element is the tail
                    self._tail = node.prev_node
                    if self._tail:
                        self._tail.next_node = None
                else:  # if element to be deleted is in the middle
                    if node.prev_node:
                        node.prev_node.next_node = node.next_node
                    if node.next_node:
                        node.next_node.prev_node = node.prev_node

                # Clear the references of the removed node
                node.next_node = None
                node.prev_node = None
                node.elem = None
                self._size -= 1  # Update size

            node = next_node  # Move to the next node

    def filter_odd(self) -> None:
        node = self._head  # starting point
        while node:  # traverse the list
            next_node = node.next_node  # Store the next node before removing the current one

            if node.elem % 2 == 0:  # check if the element of the node is even number
                if node == self._head:  # if the element to be deleted is the head
                    self._head = node.next_node  # Move head to the next node
                    if self._head:  # If new head exists
                        self._head.prev_node = None  # Update its prev_node to None
                    else:
                        self._tail = None  # If list becomes empty, update tail to None
                elif node == self._tail:  # if the element to be deleted is the tail
                    self._tail = node.prev_node  # Move tail to the previous node
                    self._tail.next_node = None  # Set its next_node to None
                else:  # if the element to be deleted is in the middle
                    if node.prev_node:
                        node.prev_node.next_node = node.next_node
                    if node.next_node:
                        node.next_node.prev_node = node.prev_node

                # Clear the references of the removed node
                node.next_node = None
                node.prev_node = None
                node.elem = None
                self._size -= 1  # Update size

            node = next_node  # Move to the next node

    def filter_even(self) -> None:
        node = self._head
        while node:
            next_node = node.next_node  # Store the next node before removing the current one

            if node.elem % 2 != 0:  # check if the element of the node is an odd number
                if node == self._head:  # If the element to be deleted is the head
                    self._head = node.next_node  # Move head to the next node
                    if self._head:  # If new head exists
                        self._head.prev_node = None  # Update its prev_node to None
                    else:
                        self._tail = None  # If list becomes empty, update tail to None
                elif node == self._tail:  # If the element to be deleted is the tail
                    self._tail = node.prev_node  # Move tail to the previous node
                    self._tail.next_node = None  # Set its next_node to None
                else:  # if the element to be deleted is in the middle
                    if node.prev_node:
                        node.prev_node.next_node = node.next_node
                    if node.next_node:
                        node.next_node.prev_node = node.prev_node

                # Clear the references of the removed node
                node.next_node = None
                node.prev_node = None
                node.elem = None
                self._size -= 1  # Update size

            node = next_node  # Move to the next node
