import heapq

def a_star(graph, heuristics, start, goal):
    # Priority queue (min-heap)
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0
    
    f_cost = {node: float('inf') for node in graph}
    f_cost[start] = heuristics[start]

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            # Reconstruct path
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for neighbor, cost in graph[current].items():
            tentative_g_cost = g_cost[current] + cost

            if tentative_g_cost < g_cost[neighbor]:
                came_from[neighbor] = current
                g_cost[neighbor] = tentative_g_cost
                f_cost[neighbor] = tentative_g_cost + heuristics[neighbor]
                heapq.heappush(open_list, (f_cost[neighbor], neighbor))

    return None


# Graph representation
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3, 'C': 2},
    'C': {'D': 5},
    'D': {}
}

# Heuristic values
heuristics = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 0
}

start = 'A'
goal = 'D'

path = a_star(graph, heuristics, start, goal)

print("Shortest Path:", path)
