x,n,y,t = map(int,input().split())
direct = True
while x != 0:
    connerTime = n / x
    if connerTime >= t:
        break
    x = max(x - y, 0)
    direct = not direct
    t -= connerTime

move = t * x
result = move if direct else n - move
print("%0.2f" % result)