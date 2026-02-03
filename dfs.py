def dfs(u, graph, visited=None):
    if visited is None:
        visited = set()


    visited.add(u)
    print(u, end=" ")

    for v in graph[u]:      
        if v not in visited:
            dfs(v, graph, visited)


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'C'],
    'C': ['E'],
    'D': ['F', 'E'],
    'E': ['F'],
    'F': []
}

print("DFS Traversal:")
dfs('A', graph)
