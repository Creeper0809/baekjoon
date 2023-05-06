from collections import deque

n = list(map(int, input().split()))
visited = [-1 for _ in range(100001)]

def bfs(visited,subin,brother) :
    queue = deque()
    queue.append(subin)
    visited[subin] = 0
    while queue :
        pop = queue.popleft()
        if pop == brother :
            break
        else :
            if 0 <= pop + 1 <= 100000 and visited[pop+1] == -1:
                visited[pop+1] = visited[pop] + 1
                queue.append(pop+1)
            if visited[pop-1] == -1 and 0 <= pop - 1 <= 100000 :
                visited[pop - 1] = visited[pop] + 1
                queue.append(pop-1)
            if visited[pop*2] == -1 and 0 <= pop * 2 <= 100000 :
                visited[pop * 2] = visited[pop] + 1
                queue.append(pop*2)
    return visited[brother]

print(bfs(visited,n[0],n[1]))