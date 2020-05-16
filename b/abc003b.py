import sys
s = sys.stdin.readline()
t = sys.stdin.readline()
substitutes = set(['a', 't', 'c', 'o', 'd', 'e', 'r'])
ans = 'You will lose'
can_win = False
for s_c, t_c in zip(s, t):
    if s_c == t_c:
        can_win = True
        continue
    if s_c != '@' and t_c != '@':
        can_win = False
        break
    if s_c == '@':
        if t_c in substitutes: can_win = True
        else:
            can_win = False
            break
    elif t_c == '@':
        if s_c in substitutes: can_win = True
        else:
            can_win = False
            break
# print(ans := 'You can win' if can_win else 'You will lose')
ans = 'You can win' if can_win else 'You will lose'
print(ans)
                