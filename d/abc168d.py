from collections import deque


class Graph:
    def __init__(self, n, directed=False):
        self.graph = [deque([]) for _ in range(n)]
        self.directed = directed
        self.distance = [float('inf') for _ in range(n)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        if not self.directed: self.graph[v].append(u)

    def bfs(self, start):
        visited = [False for _ in range(len(self.graph))]
        queue = deque([start])
        visited[start] = True
        distance_from_start = 1
        
        while queue:
            v = queue.popleft()
            print(f'pop v: {v}')
            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    self.distance[i] = min(self.distance[i], distance_from_start)
            distance_from_start += 1

def main():
    n, m = map(int, input().split())
    g = Graph(n)
    for _ in range(m):
        a, b = map(int, input().split())
        g.add_edge(a - 1, b - 1)
    print(g.graph)
    g.bfs(1)
    print(g.distance)
    
if __name__ == '__main__':
    main()