import sys

sys.setrecursionlimit(10 ** 8)
p = int(input())
prime_numbers = [3, 5, 17, 257, 65537]
selected = []
def dfs():
    num = 1
    print(selected)
    for i in selected:
        num *= i
    while num <= p:
        if num == p:
            print("YES")
            exit(0)
        num *= 2
    for i in prime_numbers:
        if i not in selected:
            selected.append(i)
            dfs()
            selected.pop()


dfs()
print("NO")
