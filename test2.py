n = int(input())
dp = [[[-1 for _ in range(n)] for _ in range(n)] for _ in range(n)]
voters = [list(map(int,input().split())) for _ in range(n)]
def dfs(x1, y1, x2,y2,dp):

    # 위치가 격자 밖이면 0 반환
    if x1 >= n or y1 >= n or x2 >= n or y2 >= n:
        return 0

    # 두 사람이 모두 (n,n)에 도착한 경우, 유권자 수 반환
    if x1 == n - 1 and y1 == n - 1:
        return voters[x1][y1]

    # 현재 상태가 이미 방문한 상태라면 메모이제이션 테이블에서 해당 값을 반환
    if dp[x1][y1][x2] != -1:
        return dp[x1][y1][x2]

    # 현재 상태의 최대 유권자 수 초기화
    ans = 0
    # 두 사람이 모두 오른쪽으로 이동
    ans = max(ans, dfs(x1 + 1, y1, x2 + 1,y2,dp))
    # 첫 번째 사람은 오른쪽으로, 두 번째 사람은 아래쪽으로 이동
    ans = max(ans, dfs(x1 + 1, y1, x2,y2+1,dp))
    # 첫 번째 사람은 아래쪽으로, 두 번째 사람은 오른쪽으로 이동
    ans = max(ans, dfs(x1, y1 + 1, x2 + 1,y2,dp))
    # 두 사람이 모두 아래쪽으로 이동
    ans = max(ans, dfs(x1, y1 + 1, x2,y2+1,dp))
    # 메모이제이션 테이블을 현재 상태의 최대 유권자 수로 업데이트
    dp[x1][y1][x2] = ans + voters[x1][y1] + (x1 != x2) * voters[x2][y2]
    return dp[x1][y1][x2]


print(dfs(0, 0, 0,0,dp))  # 출력: 103
print(dp)
