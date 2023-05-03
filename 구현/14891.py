from collections import deque

arr = [""] + [deque(map(int, input())) for _ in range(4)]


def recu(num, dir, already):
    if num in already:
        return
    temp.append((num, dir))
    already.append(num)
    if num + 1 < 5:
        if arr[num][2] != arr[num + 1][6]:
            recu(num + 1, -dir, already)
    if num - 1 > 0:
        if arr[num][6] != arr[num - 1][2]:
            recu(num - 1, -dir, already)


N = int(input())
for _ in range(N):
    num, dir = map(int, input().split())
    temp = list()
    recu(num, dir, list())
    for nums, dirs in temp:
        arr[nums].rotate(dirs)

count = 0
for i in range(1, 5):
    count += arr[i][0] * (2 ** (i - 1))
print(count)
