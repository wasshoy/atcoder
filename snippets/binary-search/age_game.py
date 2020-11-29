# 基本的な二分探索の例
# これをベースに考える

def start_game() -> None:
    print('Start Game!')
    left = 0
    right = 100
    cnt = 0
    while right - left > 1:
        mid = left + (right - left) // 2
        cnt += 1
        ans = input(f'Is the age same or more than {mid} ? (y/n): ')
        if ans == 'y':
            left = mid
        else:
            right = mid

    print(f'The age is {left} !(operation counts: {cnt})')


if __name__ == '__main__':
    start_game()
