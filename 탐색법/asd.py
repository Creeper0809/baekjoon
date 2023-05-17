N = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)
print(max_dp)
# 몇번째 까지 봤을 때 최장 길이인지
max_idx = dp.index(max_dp)
lis = []

# max_idx 부터 한칸씩 내려보면서 1 2 1 3 2 4라면 4 -> 3 -> 2 -> 1 부분인곳을 찾아주기
while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(arr[max_idx])
        max_dp -= 1
    max_idx -= 1

lis.reverse()
print(*lis)