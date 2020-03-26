from collections import defaultdict, deque

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
            # print(f'v: {v}')
            for i in self.graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    self.distance[i] = min(self.distance[i], distance_from_start)
            distance_from_start += 1

def main():
    n = int(input())
    g = Graph(n)
    for _ in range(n-1):
        a, b = map(int, input().split())
        g.add_edge(a-1, b-1)
    #print(g.graph)
    g.bfs(1)
    print(g.distance)
    
if __name__ == '__main__':
    main()

'''
入力

N
a_1 b_1
...
a_N-1 b_N-1

5
1 2
1 3
3 4
3 5
'''