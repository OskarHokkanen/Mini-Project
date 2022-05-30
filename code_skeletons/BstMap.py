from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    # Check if given key is the current nodes key or None.
    # If true set the current nodes key and value.
    # Else check if key should go left or right,
    # call left/rights nodes put-method.
    def put(self, key, value):
        if self.key is None or self.key == key:
            self.key = key
            self.value = value
        else:
            if key < self.key:
                if self.left is None:
                    m = Node(key, value)
                    self.left = m
                else:
                    self.left.put(key, value)
            else:
                if self.right is None:
                    n = Node(key, value)
                    self.right = n
                else:
                    self.right.put(key, value)

    # Get all nodes key and value and convert to a string.
    # Returns string
    def to_string(self):
        left = ""
        s = "( " + self.key + "," + str(self.value) + ") "
        if self.left is not None:
            left = self.left.to_string()
            s = left + s
        if self.right is not None:
            s += self.right.to_string()
        return s

    # Counts the amount of nodes in the tree.
    # Returns (int) the amount of Nodes.
    def count(self):
        c = 0
        if self.key is not None:
            c += 1
            if self.right is not None:
                c += self.right.count()
            if self.left is not None:
                c += self.left.count()
        return c

    # Searches each node and checks if the key corresponds to the Nodes key
    # Returns (int) the value of the key or None if not found
    def get(self, key):
        val = None
        if self.key == key:
            val = self.value
        if key < self.key and self.left is not None:
            val = self.left.get(key)
        if key > self.key and self.right is not None:
            val = self.right.get(key)
        return val

    # Checks if there is a left and right node if so add
    # one to left/right side. The hihgher value gets re-
    # turned.
    def max_depth(self):
        left, right, m = 0, 0, 0
        if self.left is not None:
            left += self.left.max_depth()
            left += 1
        if self.right is not None:
            right += self.right.max_depth()
            right += 1
        if self.right is None and self.left is None:  # Last node
            m += 1
        m += left if left > right else right
        return m

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        t = (self.key, self.value)
        if self.left is not None:
            self.left.as_list(lst)
        if self.left is None and self.right is None:
            lst.append(t)
        elif self.right is not None:
            lst.append(t)
            self.right.as_list(lst)
        return lst


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
