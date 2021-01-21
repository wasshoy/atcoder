# 23m AC
*nums, = map(int, input().split())
nums.sort()
a, b, c = nums
ans = 0
if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0) or (a % 2 != 0 and b % 2 != 0 and c % 2 != 0):
    ans += (c-a)//2 + (c-b)//2
elif (c % 2 == 0 and b % 2 != 0 and a % 2 != 0) or (c % 2 != 0 and b % 2 == 0 and a % 2 == 0):
    a += 1
    b += 1
    ans += 1
    ans += (c-a)//2 + (c-b)//2
else:
    ans += (c-a)//2 + (c-b)//2 + 2
print(ans)
