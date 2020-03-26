from collections import Counter
n = int(input())
*v, = map(int, input().split())
v_even, v_odd = v[::2], v[1::2]
even = Counter(v_even).most_common(2)
odd = Counter(v_odd).most_common(2)

ans = 0

if even[0][0] != odd[0][0]:
    ans = n - odd[0][1] - even[0][1]

else:
    if len(even) == 1 and len(odd) == 1:
        ans = n // 2
        
    elif len(even) == 1:
        ans = n - even[0][1] - odd[1][1]
        
    elif len(odd) == 1:
        ans = n - even[1][1] - odd[0][1]
        
    else:
        ans = min(n - even[0][1] - odd[1][1], 
                  n - even[1][1] - odd[0][1])
                  
print(ans)
