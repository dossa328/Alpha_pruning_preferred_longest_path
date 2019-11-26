

# Code by Eryk Kopczyński
import collections


def find_shortest_path(graph, start, end):
    dist = {start: [start]}
    q = collections.deque(start)
    while len(q):
        at = q.popleft()
        for next in graph[at]:
            if next not in dist:
                dist[next] = dist[at] + [next]
                q.append(next)
    return dist[end]


graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C', 'E'],
         'E': ['F'],
         'F': ['C']}

print(find_shortest_path(graph, 'A', 'E'))
