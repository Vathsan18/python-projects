graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': [],
    'D': [],
    'E': ['F','G'],
    'F': [],
    'G': []
}

queue = []
visited = []
goal_node = input("Enter the node: ").upper()

def bfs(graph, visited, node, goal_node):
    queue.append(node)
    while queue:
        v = queue.pop(0)
        visited.append(v)
        if v == goal_node:
            print(f"gaol reached = {goal_node}")
            break
        for n in graph[v]:
            if n not in visited:
                queue.append(n)
    else:
        print("Goal not found")
    print(f"Queue = {queue}")
    print(f"Visited = {visited}")


print("Following is BFS")
bfs(graph, visited, 'A', goal_node)