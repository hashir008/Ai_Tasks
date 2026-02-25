#Question 1 : 
# BFS without Queue and without Node

graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": [],
    "F": []
}

def bfs(graph, start):
    visited = []
    current_level = [start]

    while current_level:
        next_level = []

        for node in current_level:
            if node not in visited:
                print(node, end=" ")
                visited.append(node)
                next_level.extend(graph[node])

        current_level = next_level

print("BFS Traversal:")

#--------------------------------------------------------------------------

#Question 2 : BFS with Queue & Node

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def bfs(start_node):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node.value, end=" ")
            visited.add(node)

            for neighbor in node.neighbors:
                queue.append(neighbor)

A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")
E = Node("E")
F = Node("F")

A.neighbors = [B, C]
B.neighbors = [D, E]
C.neighbors = [F]

print("BFS Traversal:")
bfs(A)
bfs(graph, "A")
