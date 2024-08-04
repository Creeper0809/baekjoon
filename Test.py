def fibonacci_dp(n):
    if n == 0: return []
    elif n == 1: return [1]
    fib = [0] * (n + 1)
    fib[1], fib[2] = 1, 1
    for i in range(3, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[1:]

def fibonacci_fibonacci_sequence(n):
    fib_seq = fibonacci_dp(n)
    fib_fib_seq = []
    for i in fib_seq:
        fib_fib_seq.extend([i] * i)
    return fib_fib_seq

def sum_of_fibonacci_fibonacci_sequence(a, b):
    n = 30  # n값 높게 설정가능하나 시간 오래걸림
    fib_fib_seq = fibonacci_fibonacci_sequence(n)
    return sum(fib_fib_seq[a-1:b])

a, b = map(int, input().split())

print(sum_of_fibonacci_fibonacci_sequence(a, b))