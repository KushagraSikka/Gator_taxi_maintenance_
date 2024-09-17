# code by Kushagra Sikka
# UFID: 3979-0988
# ADS Project final submission

from enum import Enum
# this is the enum library which is used to define the color of the node


class Color(Enum):
    RED = 1
    BLACK = 2
# this is the node class which has the ride information and the color of the node


class Node:
    def __init__(self, ride_info, color=Color.RED, left=None, right=None, parent=None):
        self.ride_info = ride_info
        self.color = color
        self.left = left
        self.right = right
        self.parent = parent
# this is the rb tree class which has the root node and the nil node

    def __str__(self):
        return f"Node(ride_info={self.ride_info}, color={self.color})"


class RBTree:
    BLACK = 0
    RED = 1
# this is the init function which initializes the root node and the nil node

    def __init__(self):
        self.nil = Node(None, color=Color.BLACK)
        self.root = self.nil
# this is the fix insert function which fixes the tree after the insertion of the node

    def insert(self, ride_info):
        new_node = Node(ride_info, left=self.nil, right=self.nil)
        parent, curr = None, self.root

        while curr != self.nil:
            parent = curr
            if new_node.ride_info[0] < curr.ride_info[0]:
                curr = curr.left
            elif new_node.ride_info[0] > curr.ride_info[0]:
                curr = curr.right
            else:
                return False

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.ride_info[0] < parent.ride_info[0]:
            parent.left = new_node
        else:
            parent.right = new_node

        self._fix_insert(new_node)
        return True
# this is the search function which searches for the node with the given ride number

    def get_ride(self, ride_number):
        ride_info = self._search_ride(self.root, ride_number)
        if ride_info:
            return str(ride_info)
        else:
            return "(0,0,0)"
# this is the get range function which returns the rides in the given range

    def get_range(self, ride_number1, ride_number2):
        result = []
        self._search_range(self.root, ride_number1, ride_number2, result)
        if result:
            return ','.join(str(ride) for ride in result)
        else:
            return "(0,0,0)"
# this is the search ride function which searches for the ride with the given ride number

    def _search_ride(self, node, ride_number):
        if node == self.nil or node.ride_info[0] == ride_number:
            return node.ride_info
        if ride_number < node.ride_info[0]:
            return self._search_ride(node.left, ride_number)
        return self._search_ride(node.right, ride_number)
# this is the search range function which searches for the rides in the given range

    def _search_range(self, node, ride_number1, ride_number2, result):
        if node == self.nil:
            return
        if ride_number1 < node.ride_info[0]:
            self._search_range(node.left, ride_number1, ride_number2, result)
        if ride_number1 <= node.ride_info[0] <= ride_number2:
            result.append(node.ride_info)
        if ride_number2 > node.ride_info[0]:
            self._search_range(node.right, ride_number1, ride_number2, result)
# this is the fix insert function which fixes the tree after the insertion of the node

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == Color.RED:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == Color.RED:
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == Color.RED:
                    node.parent.color = Color.BLACK
                    uncle.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    node.parent.color = Color.BLACK
                    node.parent.parent.color = Color.RED
                    self._left_rotate(node.parent.parent)

        self.root.color = Color.BLACK
# this is the left rotate function which rotates the tree to the left

    def _left_rotate(self, x):
        if x is None:
            return

        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        elif x == x.parent.right:
            x.parent.right = y

        y.left = x
        x.parent = y
# this is the right rotate function which rotates the tree to the right

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right is not None:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
# this is the transplant function which transplants the node

    def _transplant(self, u, v):
        if u.parent is None or u.parent == self.nil:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent
# this is the delete function which deletes the node with the given key

    def delete(self, key):
        node = self._search(self.root, key)
        if node is None:
            return False

        self._delete_node(node)
        return True
# this is the delete node function which deletes the node

    def _delete_node(self, node):
        if node is None or node == self.nil:
            return

        y = node
        y_original_color = y.color if y != self.nil else None

        if node.left == self.nil:
            x = node.right
            self._transplant(node, node.right)
        elif node.right == self.nil:
            x = node.left
            self._transplant(node, node.left)
        else:
            y = self._minimum(node.right)
            y_original_color = y.color if y != self.nil else None
            x = y.right

            if y.parent == node:
                x.parent = y
            else:
                self._transplant(y, y.right)
                y.right = node.right
                y.right.parent = y

            self._transplant(node, y)
            y.left = node.left
            y.left.parent = y
            y.color = node.color

        if y_original_color == Color.BLACK:
            self._fix_delete(x)
# this is the fix delete function which fixes the tree after the deletion of the node


# this is the search function which searches for the node with the given key

    def _search(self, root, ride_number):
        if root == self.nil or ride_number == root.ride_info[0]:
            return root
        if ride_number < root.ride_info[0]:
            return self._search(root.left, ride_number)
        return self._search(root.right, ride_number)

    # You also need to add a public method that calls this private method:

    def search(self, ride_number):
        return self._search(self.root, ride_number)
# this is the search range function which searches for the nodes in the given range

    def search_range(self, start_key, end_key):
        result = []
        node = self._get_minimum(self.root)
        while node != self.nil and node is not None:
            if start_key <= node.ride_info[0] <= end_key:
                result.append(node.ride_info)
            node = self._get_successor(node)
        return result
# this is the get successor function which returns the successor of the given node

    def _get_successor(self, node):
        if node.right != self.nil:
            return self._get_minimum(node.right)

        successor = node.parent
        while successor is not None and node == successor.right:
            node = successor
            successor = successor.parent

        return successor
# this is the get minimum function which returns the minimum node

    def _get_minimum(self, node):
        while node.left != self.nil:
            node = node.left
        return node if node is not None else self.nil

# this is the update ride info function which updates the ride info of the given node
    def update_ride_info(self, ride_number, updated_ride_info):
        node = self.search(ride_number)
        if node is not None and node != self.nil:
            node.ride_info = updated_ride_info
# this is the fix delete function which fixes the tree after the deletion of the node

    def _fix_delete(self, x):
        while x != self.root and x.color == Color.BLACK:
            if x == x.parent.left:
                sibling = x.parent.right
                if sibling.color == Color.RED:
                    sibling.color = 0
                    x.parent.color = 1
                    self._left_rotate(x.parent)
                    sibling = x.parent.right

                if sibling.left.color == 0 and sibling.right.color == 0:
                    sibling.color = 1
                    x = x.parent
                else:
                    if sibling.right.color == 0:
                        sibling.left.color = 0
                        sibling.color = 1
                        self._right_rotate(sibling)
                        sibling = x.parent.right

                    sibling.color = x.parent.color
                    x.parent.color = 0
                    sibling.right.color = 0
                    self._left_rotate(x.parent)
                    x = self.root
            else:
                sibling = x.parent.left
                if sibling.color == 1:
                    sibling.color = 0
                    x.parent.color = 1
                    self._right_rotate(x.parent)
                    sibling = x.parent.left

                if sibling.right.color == 0 and sibling.left.color == 0:
                    sibling.color = 1
                    x = x.parent
                else:
                    if sibling.left.color == 0:
                        sibling.right.color = 0
                        sibling.color = 1
                        self._left_rotate(sibling)
                        sibling = x.parent.left

                    sibling.color = x.parent.color
                    x.parent.color = 0
                    sibling.left.color = 0
                    self._right_rotate(x.parent)
                    x = self.root
        x.color = 0
# this is the minimum function which returns the minimum node

    def _minimum(self, node):
        if node is None:
            return None
        while node.left != self.nil:
            node = node.left
        return node
