print('Start Game!')
left = 20
right = 36
while right - left > 1:
    mid = left + (right - left) // 2
    ans = input(f'Is the age same or more than {mid} ? (y/n): ')
    if ans == 'y':
        left = mid
    else:
        right = mid

print(f'The age is {left} !')
