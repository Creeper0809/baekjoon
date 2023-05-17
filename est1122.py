import copy

N = int(input())
arr = list(map(int,input().split()))

sorted_arr = sorted(arr)
copied_temp = copy.deepcopy(arr)
k = N - 1
while True:
    left,right = 0,0
    for i in range(N):
        for j in range(N):
            if arr[j] != j+1 and arr[i] != i+1 and  abs(arr[j] -arr[i]) == k and arr[i]>arr[j]:
                arr[j],arr[i] = arr[i],arr[j]
    print(k)
    if sorted_arr == arr:
        break
    arr = copy.deepcopy(copied_temp)
    k-=1
print(k)

