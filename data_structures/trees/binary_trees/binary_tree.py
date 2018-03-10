class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        return self.preorder_search(tree.root, find_val)

    def print_tree(self):
        return self.preorder_print(tree.root, "")[:-1]

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def height(self, node):
        if node is None:
            return 0
        left = self.height(node.left)
        right = self.height(node.right)

        if left > right:
            h = 1 + left
        else:
            h = 1 + right

        return h


# Set up tree:
tree = BinaryTree(Node("a"))
tree.root.left = Node("b")
tree.root.right = Node("c")
tree.root.left.left = Node("d")
tree.root.left.right = Node("e")
tree.root.left.left.left = Node("f")
tree.root.left.left.right = Node("g")
tree.root.left.left.right.left = Node("h")
tree.root.left.left.right.right = Node("i")

tree.root.right.left = Node("j")
tree.root.right.right = Node("k")
tree.root.right.right.left = Node("l")
tree.root.right.right.right = Node("m")

print(tree.height(tree.root))

# Should be True
#print(tree.search(4))

# Should be False:
#print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
#print(tree.print_tree())
