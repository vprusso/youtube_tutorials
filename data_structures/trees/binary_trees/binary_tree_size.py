class Stack(object):
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()
     
    def size(self):
        return len(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):  
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s


class Queue(object):
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
        # Recursive traversals
        if traversal_type == "preorder":
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

        # Iterative traversals
        elif traversal_type == "levelorder":
            return self.levelorder_print(tree.root)
        elif traversal_type == "inorder_iterative":
            return self.inorder_iterative(tree.root)
        elif traversal_type == "preorder_iterative":
            return self.preorder_iterative(tree.root)
        elif traversal_type == "postorder_iterative":
            return self.postorder_iterative(tree.root)
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

            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

        return traversal

    def preorder_search(self, start, find_val):
        if start:
            if start.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val) or \
                       self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        """Root->Left-Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def preorder_iterative(self, start):
        stack = Stack()

        cur = start
        is_done = False

        traversal = ""
        while not is_done:
            if cur is not None:
                traversal += str(cur.value) + "-"
                stack.push(cur)
                cur = cur.left
            else:
                if len(stack) > 0:
                    cur = stack.pop()
                    cur = cur.right
                else:
                    is_done = True
        return traversal

    def inorder_iterative(self, start):
        s = Stack()

        cur = start
        is_done = False

        traversal = ""
        while not is_done:
            if cur is not None:
                s.push(cur)
                cur = cur.left
            else:
                if len(s) > 0:
                    cur = s.pop()
                    traversal += str(cur.value) + "-"
                    cur = cur.right
                else:
                    is_done = True
        return traversal

    def postorder_iterative(self, start):
        s = Stack()

        cur = start
        is_done = False

        traversal = ""
        while not is_done:
             
            if cur is not None:
                s.push(cur)
                cur = cur.left
            else:
                if len(s) > 0:
                    cur = s.pop()
                    traversal += str(cur.value) + "-"
                    cur = cur.right
                else:
                    is_done = True

        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return 1 + max(left_height, right_height)

    def size_(self, node):
        if node is None:
            return 0
        return 1 + self.size_(node.left) + self.size_(node.right)

    def size(self):
        if self.root is None:
            return 0

        stack = Stack()
        stack.push(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.push(node.left)
            if node.right:
                size += 1
                stack.push(node.right)
        return size

# Calculate size of binary tree:
#     1
#    / \
#   2  3
#  / \
# 4  5
# 
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

print(tree.size())
print(tree.size_(tree.root))



