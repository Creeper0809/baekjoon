import math
n = int(input())
def change(a):
    temp = 0
    temp2 = int(math.log10(a) + 1)
    count = int(math.log10(a) + 1)//2
    while count != 0:
        temp *= 10
        temp += a%10
        a//=10
        count -= 1
    if temp2 % 2 != 0:
        temp *= 10
        temp += a % 10
    if temp == a:
        return True
    else:
        return False

while 1:
    n += 1
    if change(n):
        print(n)
        break
