import math
n =math.factorial(int(input()))

while True:
    if str(n)[-1] == "0":
        n //= 10
    else:
        break
print(str(n)[-5:])
