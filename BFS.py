# DFS in python
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


#Here's an explanation of the code:

#We start by importing the deque class from the collections module. This will be used to create our queue for the BFS algorithm. The bfs function takes in two arguments: a graph represented as a dictionary, and a start vertex from which to start the search. We create a visited set to keep track of the vertices we've already visited, and a queue deque to keep track of the vertices we still need to visit. We add the start vertex to the queue. While there are still vertices in the queue, we pop the vertex at the front of the queue and check if it has already been visited. If not, we add it to the visited set and add all its unvisited neighbors to the queue. Once the queue is empty, we return the visited set containing all the visited vertices. Here's an example of how to use the bfs function with a sample graph:

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(bfs(graph, 'A')) # prints {'A', 'B', 'C', 'D', 'E', 'F'}
