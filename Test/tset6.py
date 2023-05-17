N = int(input())
if N<1 or N > 100:
    exit(0)
if N == 1:
    print(1)
    exit(0)
graph = [[0] * N for _ in range(N)]
x,y = 0,0
graph[y][x] = 1
nownum = 1
flag = True
for i in range(1,N):
    if flag:
        y += 1
        nownum += 1
        graph[y][x] = nownum

        for _ in range(i):
            nownum += 1
            x += 1
            y -= 1
            graph[y][x] = nownum
        flag = not flag
    else:
        x += 1
        nownum += 1
        graph[y][x] = nownum

        for _ in range(i):
            nownum += 1
            x -= 1
            y += 1
            graph[y][x] = nownum
        flag = not flag
if N %2 == 1:
    flag = False
    for i in range(N - 2, 0, -1):
        if flag:
            y += 1
            nownum += 1
            graph[y][x] = nownum
            for _ in range(i):
                nownum += 1
                x -= 1
                y += 1
                graph[y][x] = nownum

            flag = not flag
        else:
            x += 1
            nownum += 1
            graph[y][x] = nownum
            for _ in range(i):
                nownum += 1
                x += 1
                y -= 1
                graph[y][x] = nownum

            flag = not flag
else:
    flag = True
    for i in range(N - 2, 0, -1):
        if flag:
            y += 1
            nownum += 1
            graph[y][x] = nownum
            for _ in range(i):
                nownum += 1
                x -= 1
                y += 1
                graph[y][x] = nownum

            flag = not flag
        else:
            x += 1
            nownum += 1
            graph[y][x] = nownum

            for _ in range(i):
                nownum += 1
                x += 1
                y -= 1
                graph[y][x] = nownum
            flag = not flag
nownum += 1
graph[N-1][N-1] = nownum
# 틀린답
for i in graph:
    print(*i,sep=" ")
# 정답
for i in graph:
    for j in i:
        print(j,end=" ")
    print("")
