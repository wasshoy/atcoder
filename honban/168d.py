# from collections import defaultdict
import numpy as np
from scipy.sparse.csgraph import shortest_path

def get_path(start, goal, pred):
    return get_path_row(start, goal, pred[start])

def get_path_row(start, goal, pred_row):
    path = []
    i = goal
    while i != start and i >= 0:
        path.append(i)
        i = pred_row[i]
    if i < 0:
        return []
    path.append(i)
    return path[::-1]

n, m = map(int, input().split())
a, b = [], []
for _ in range(m):
   ai, bi =  map(int, input().split())
   a.append(ai)
   b.append(bi)

graph = [[0 for _ in range(n)] for _ in range(n)]
for ai, bi in zip(a, b):
    graph[ai - 1][bi - 1], graph[bi - 1][ai - 1] = 1, 1
graph = np.array(graph)
signs = [set() for _ in range(n)]
# print(graph)
shortest, pathes = shortest_path(graph, return_predecessors=True)
# print(shortest)
# print(pathes)
for i in range(1, n):
    path = get_path(i, 0, pathes)
    # print(i, path)
    # print(get_path(i, 0, pathes)[1:-1])
    for j in range(len(path) - 1):
        # print(f'{path[j + 1]} is signed at {path[j]}')
        signs[path[j]].add(path[j + 1])
        if path
# print(signs)

is_ok = True
for sign in signs:
    if len(sign) > 1:
        is_ok = False
        break

if is_ok:
    print('Yes')
    for sign in signs[1:]:
        print(sign.pop() + 1)
else:
    print('No')