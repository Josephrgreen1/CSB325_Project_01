# A doubly linked node that stores data and references to the previous and next nodes.
class DLNode:

    # Sets up the node with its data and links to other nodes.
    def __init__(self, previous_node=None, data_portion=None, next_node=None):

        # The previous node in the linked deque.
        self.previous_node = previous_node

        # The data stored in the node.
        self.data = data_portion

        # The next node in the linked deque.
        self.next_node = next_node

    # GETTER: Returns the data stored in the node.
    def get_data(self):
        return self.data

    # SETTER: Updates the data stored in the node.
    def set_data(self, new_data):
        self.data = new_data

    # GETTER: Returns the next node.
    def get_next_node(self):
        return self.next_node

    # SETTER: Changes which node comes next.
    def set_next_node(self, next_node):
        self.next_node = next_node

    # GETTER: Returns the previous node.
    def get_previous_node(self):
        return self.previous_node

    # SETTER: Changes which node comes before.
    def set_previous_node(self, previous_node):
        self.previous_node = previous_node


# A doubly linked deque that allows adding and removing elements from both ends.
class LinkedDeque:

    # Constructs an empty deque with no front or back node.
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    # Checks if the deque is empty.
    def is_empty(self):
        if self.front is None and self.back is None:
            return True
        else:
            return False

    # Adds a new entry to the back of the deque.
    def add_to_back(self, new_entry):

        # If the deque is empty, the new node becomes both the front and back.
        if self.is_empty() == True:
            new_DL_node = DLNode(None, new_entry, None)
            self.front = new_DL_node
            self.back = new_DL_node
            self.size += 1

        else:
            # Create a new node that points back to the current back node.
            new_DL_node = DLNode(self.back, new_entry, None)

            # Connect the old back node to the new node.
            self.back.set_next_node(new_DL_node)

            # Make the new node the back of the deque.
            self.back = new_DL_node
            self.size += 1

    # Adds a new entry to the front of the deque
    def add_to_front(self, new_entry):

        # If the deque is empty, the new node becomes both the front and back
        if self.is_empty() == True:
            new_DL_node = DLNode(None, new_entry, None)
            self.front = new_DL_node
            self.back = new_DL_node
            self.size += 1

        else:
            # Create a new node that points forward to the current front node.
            new_DL_node = DLNode(None, new_entry, self.front)

            # Connect the old front node back to the new node.
            self.front.set_previous_node(new_DL_node)

            # Make the new node the front of the deque.
            self.front = new_DL_node
            self.size += 1

    # GETTER: Returns the data stored in the front node without removing it.
    def get_front(self):

        # If the deque is empty, there is no data to return.
        if self.is_empty() == True:
            return None

        else:
            return self.front.get_data()

    # GETTER: Returns the data stored in the back node without removing it.

    def get_back(self):

        # If the deque is empty, there is no data to return.
        if self.is_empty() == True:
            return None

        else:
            return self.back.get_data()

    # Removes the front node and returns its stored data.
    def remove_front(self):

        # If the deque is empty, there is nothing to remove.
        if self.is_empty() == True:
            return None

        else:
            # Remember the current front node before removing it.
            front_node = self.front

            # Move the front reference to the next node.
            self.front = front_node.get_next_node()

            if self.front is not None:
                # Disconnect the new front node from the old front node.
                self.front.set_previous_node(None)

            else:
                # If there are no nodes left, the back must also be empty.
                self.back = None

            # Return the data from the node that was removed.
            self.size -= 1
            return front_node.get_data()

    # Removes the back node and returns its stored data.
    def remove_back(self):

        # If the deque is empty, there is nothing to remove.
        if self.is_empty() == True:
            return None

        else:
            # Remember the current back node before removing it.
            back_node = self.back

            # Move the back reference to the previous node.
            self.back = back_node.get_previous_node()

            if self.back is not None:
                # Disconnect the new back node from the old back node
                self.back.set_next_node(None)

            else:
                # If there are no nodes left, the front must also be empty.
                self.front = None

            # Return the data from the node that was removed.
            self.size -= 1
            return back_node.get_data()

    # Removes all nodes from the deque.
    def clear(self):

        # Remove references to the first and last nodes.
        self.front = None
        self.back = None
        self.size = 0

    # Displays all data in the deque, starting at the front.
    def display(self):

        # Start at the front node.
        current_node = self.front

        # Continue until there are no more nodes.
        while current_node is not None:

            # Print The data stored in the current node.
            print(current_node.get_data())

            # Move to the next node.
            current_node = current_node.get_next_node()