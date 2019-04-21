graph = {'A': set(['B', 'C']),'B': set(['A', 'D', 'E']),'C': set(['A', 'F']),'D': set(['B']),'E': set(['B', 'F']),'F': set(['C', 'E'])}

# first implementation
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

print("First Implementation: ")
print(dfs(graph, 'A')) # should output {'E', 'D', 'F', 'A', 'C', 'B'}, but letters don't have to be in that order
print()

# second implementation
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

print("Second Implementation: ")
print(dfs(graph, 'C')) # should output {'E', 'D', 'F', 'A', 'C', 'B'}, but not necessarily in that order
print()

# above, each of the implementation outputs all of the nodes in the graph, because all of the nodes in the given graph are somehow connected to each other

# actually stating all the possible paths between two given points
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

print("Stating paths:")
print(list(dfs_paths(graph, 'A', 'F'))) # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']], though not necessarily in that order
print()
