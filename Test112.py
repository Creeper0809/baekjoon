for _ in range(int(input())):
    N = int(input())
    arr = [i for i in range(N+1)]
    perpose_num = 0
    arr_sum = sum(arr)
    while sum(arr) > perpose_num:
        perpose_num += N
    start_index = perpose_num - arr_sum
    while start_index != 0:
        add = start_index // N
        arr[N] += add * N
        start_index %= N
        N-=1
    print(*arr[1:] ,sep=" ")