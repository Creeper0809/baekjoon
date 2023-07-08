import bisect

N = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

count = [-float('inf')]

for i in range(1, N + 1):
    if arr[i] > count[-1]:
        count.append(arr[i])
        dp[i] = len(count) - 1
    else:
        dp[i] = bisect.bisect_left(count, arr[i])
        count[dp[i]] = arr[i]
print(len(count) - 1)

# max_idx 부터 한칸씩 내려보면서 1 2 1 3 2 4라면 4 -> 3 -> 2 -> 1 부분인곳을 찾아주기
max_idx, lis = max(dp) + 1, []
for i in range(N, 0, -1):
    if dp[i] == max_idx - 1:
        lis.append(arr[i])
        max_idx = dp[i]
print(*lis[::-1])