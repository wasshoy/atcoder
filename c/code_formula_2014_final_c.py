import re
import string
import sys


def input(): return sys.stdin.readline().strip()
def S(): return input()
def LS(): return input().split()


s = LS()
ans = set()
pat = r'@.*?$'
for st in s:
    if '@' not in st:
        continue
    tmp = re.findall(pat, st)
    # print(tmp[0].split('@'))
    for sk in tmp[0].split('@'):
        if len(sk) != 0 and sk[0] in set(string.ascii_letters):
            ans.add(sk)
ans = list(ans)
ans.sort()
print(*ans, sep='\n')
