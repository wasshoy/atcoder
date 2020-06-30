# 30m AC
import sys
import timeit


def input(): return sys.stdin.readline().strip()
def I(): return int(input())
def LI(): return list(map(int, input().split()))
def IR(n): return [I() for i in range(n)]
def LIR(n): return [LI() for i in range(n)]
def SR(n): return [S() for i in range(n)]
def S(): return input()
def LS(): return input().split()


def main():
    c = LIR(3)
    a = [0] * 3
    b = [0] * 3
    ans = 'No'
    for i in range(101):
        a[0] = i
        b[0] = c[0][0] - a[0]
        for j in range(101):
            a[1] = j
            b[1] = c[1][1] - a[1]
            for k in range(101):
                a[2] = k
                b[2] = c[2][2] - a[2]
                current = [[a[i] + b[j] for j in range(3)] for i in range(3)]
                if c == current:
                    ans = 'Yes'
                    break
    print(ans)


# res = timeit.timeit('main()', globals=globals(), number=1)
# print(res / 1)
main()
