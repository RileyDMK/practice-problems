class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):

    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, find_val):
        return self.bst_search(self.root, find_val)

    def bst_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            elif find_val > start.value:
                return self.bst_search(start.right, find_val)
            elif find_val < start.value:
                return self.bst_search(start.right, find_val)
        return False
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
