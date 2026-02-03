def dfs(start, goal, graph, vis=None):
    if vis is None:
        vis = set()

    print(start, end=" ")

    if start == goal:
        return True

    vis.add(start)

    for child in graph[start]:      
        if child not in vis:
            if dfs(child, goal, graph, vis):
                return True

    return False


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'C'],
    'C': ['E'],
    'D': ['F', 'E'],
    'E': ['F'],
    'F': []

}

print("\n\nGoal Found:", dfs('A', 'F', graph))
