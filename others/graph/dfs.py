from collections import deque

def make_graph(n, m, ab, directed=False):
    graph = [deque([]) for _ in range(N)]
    for i in range(M):
        a, b = ab[i]
        graph[a-1].append(b-1)
        # 無向グラフの場合
        if not directed: graph[b-1].append(a-1)
    return graph
   
 
def dfs(graph, start, goal=None):
    seen = [False for _ in range(len(graph))]
    todo = deque([start])
    seen[start] = True
    while todo:
        print(f'todo: {todo}')
        v = todo.pop()    # LIFO
        for w in graph[v]:
            if seen[w]: continue
            seen[w] = True
            print(f'append {w}')
            todo.append(w)
    
if __name__ == '__main__':
    N, M = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(M)]
    g = make_graph(N, M, AB)
    print(g)
    dfs(g, 0)

'''
標準入力形式
N M
A_1 B_1
...
A_M B_M

入力例.
8 12
1 6
2 4
2 7
3 6
3 8
4 1
4 8
5 2
5 3
5 7
7 8
8 1

'''