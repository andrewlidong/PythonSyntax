# https://eddmann.com/posts/depth-first-search-and-breadth-first-search-in-python/

# adjacency list
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

# DFS
# Connected component


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


dfs(graph, 'A')  # {'E', 'D', 'F', 'A', 'C', 'B'}


# a second recursive implementation
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


dfs(graph, 'C')  # {'E', 'D', 'F', 'A', 'C', 'B'}


# Paths

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


list(dfs_paths(graph, 'A', 'F'))  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]


# recursive implementation
def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths(graph, next, goal, path + [next])


list(dfs_paths(graph, 'C', 'F'))  # [['C', 'F'], ['C', 'A', 'B', 'E', 'F']]


# Breadth First Search

# Connected Component
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


bfs(graph, 'A')  # {'B', 'C', 'A', 'F', 'D', 'E'}

# Paths


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


list(bfs_paths(graph, 'A', 'F'))  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

# Shortest path


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


shortest_path(graph, 'A', 'F')  # ['A', 'C', 'F']
