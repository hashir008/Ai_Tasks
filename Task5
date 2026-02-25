#Question 1 : DFS with stack and node 

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def dfs(start_node):
    visited = set()
    stack = [start_node]

    while stack:
        node = stack.pop()

        if node not in visited:
            print(node.value, end=" ")
            visited.add(node)

            for neighbor in reversed(node.neighbors):
                stack.append(neighbor)


A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")

A.neighbors = [B, C]
B.neighbors = [D, E]

print("DFS Traversal:")

#----------------------------------------------------------------------------------------

#Question 2 : inorder , preorder and post order 

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def preorder(root):
    if root:
        print(root.value, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end=" ")
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end=" ")

A = TreeNode("A")
B = TreeNode("B")
C = TreeNode("C")
D = TreeNode("D")
E = TreeNode("E")

A.left = B
A.right = C
B.left = D
B.right = E

print("Preorder Traversal:")
preorder(A)

print("\nInorder Traversal:")
inorder(A)

print("\nPostorder Traversal:")
postorder(A)
dfs(A)
