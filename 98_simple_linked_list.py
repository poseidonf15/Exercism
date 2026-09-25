class EmptyListException(Exception):
    """Class to raise exeption when the linked list is empty.

    Attributes:
        message (str): The message of the exeption.
    """
    def __init__(self, message):
        """Initialize the exeption with its message."""
        self.message = message

class Node:
    """Class to store nodes of the linked list.

    Attributes:
        value (any): The value of the node.
        next (class object): The next node in the linked list.
    """
    def __init__(self, value, next):
        """Initialize the node with its value and a pointer to the next node."""
        self.node_value = value
        self.node_next = next

    def value(self):
        """Function returns the value of the node.

        Returns:
            any: The value of the node.
        """
        return self.node_value

    def next(self):
        """Function returns the next node in the linked list.

        Returns:
            class object: The next node in the linked list.
        """
        return self.node_next

class LinkedList:
    """Class to store and manipulate the linked list.

    Attributes:
        head (class object): The node that is the head of the linked list.
    """
    def __init__(self, values=None):
        """Initialize the linkedlist with its nodes."""
        self.list_head = None
        if values:
            for value in values:
                self.push(value)

    def __iter__(self):
        """Function returns the linked list as an iterable object.

        Returns:
            list: The iterable version of the linked list.
        """
        node = self.list_head
        if not node:
            return []
        while node:
            yield node.node_value
            node = node.node_next

    def __len__(self):
        """Function returns the length of the linked list.

        Returns:
            int: The length of the linked list.
        """
        result = 0
        head = self.list_head
        while head:
            result += 1
            head = head.node_next
        return result

    def head(self):
        """Function returns the node that is the head of the linked list.

        Returns:
            class object: The node that is the head of the linked list.
        """
        if self.list_head:
            return self.list_head
        raise EmptyListException("The list is empty.")

    def push(self, value):
        """Function add a node to the iterable object.

        Args:
            value (any): The value of the new head of the linked list.
        """
        self.list_head = Node(value, self.list_head)

    def pop(self):
        """Function removes and returnes the head of the linked list.

        Returns:
            any: The value of the head of the linked list.
        """
        if self.list_head:
            value = self.list_head.value()
            self.list_head = self.list_head.next()
            return value
        raise EmptyListException("The list is empty.")

    def reversed(self):
        """Function returns the reversed version of the linked list.

        Returns:
            list: The reversed version of the linked list.
        """
        return reversed(list(iter(self)))