# 26m AC
import sys


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


INF = float('inf')


s = S().split()
n = I()
t = SR(n)

ans = []
for elem in s:
    is_registerd = False
    for ng in t:
        is_ng = True
        if len(elem) != len(ng):
            continue
        for elem_c, ng_c in zip(elem, ng):
            if elem_c == ng_c or ng_c == '*':
                is_ng = True
            else:
                is_ng = False
                break

        if is_ng:
            ans.append('*' * len(elem))
            is_registerd = True
            break

    if not is_registerd:
        ans.append(elem)

ans = ' '.join(ans)
print(ans)
