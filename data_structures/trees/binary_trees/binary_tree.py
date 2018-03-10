from math import log


class Queue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_search(tree.root, find_val)
        elif traversal_type == "inorder":
            return self.inorder_search(tree.root, find_val)
        elif traversal_type == "postorder":
            return self.postorder_search(tree.root, find_val)
        else:
            print("Traversal type " + str(traversal_type) + " not recognized.")
            return False

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        else:
            print("Traversal type " + str(traversal_type) + " not recognized.")
            return False

    def levelorder_print(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue.peek()) + "-"
            node = queue.dequeue()

            if len(queue) > 0:
                if int(log(len(queue), 2)) == log(len(queue), 2):
                    traversal += "\n"

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    def levelorder_line_split(self, start):
        pass

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or \
                       self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
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
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.left.right.left = Node(7)
tree.root.left.right.right = Node(8)
tree.root.right.right = Node(6)
tree.root.right.right.left = Node(9)

#print(tree.height(tree.root))

# Should be True
#print(tree.search(4))

# Should be False:
#print(tree.search(6))

# Test print_tree
print(tree.print_tree("preorder"))
print(tree.print_tree("postorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("levelorder"))

