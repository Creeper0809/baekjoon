from collections import deque
arr = [""] + [deque(map(int, input())) for _ in range(4)]

def recu(num, dir, already):
    if num in already:
        return
    already.append(num)
    if num + 1 < 5:
        if arr[num][2] != arr[num + 1][6]:
            recu(num + 1, -dir, already)
    if num - 1 > 0:
        if arr[num][6] != arr[num - 1][2]:
            recu(num - 1, -dir, already)
    arr[num].rotate(dir)

for _ in range(int(input())):
    num, dir = map(int, input().split())
    recu(num, dir, list())

print(sum([arr[i][0] * (2**(i-1)) for i in range(1,5)]))