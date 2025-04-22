MOD = 998244353

def fft(poly, inverse):
    n = len(poly)
    bit_reversed_idx = 0
    for i in range(1, n):
        bit = n // 2
        while bit_reversed_idx >= bit:
            bit_reversed_idx -= bit
            bit //= 2
        bit_reversed_idx += bit
        if i < bit_reversed_idx:
            poly[i], poly[bit_reversed_idx] = poly[bit_reversed_idx], poly[i]

    length = 2
    while length <= n:
        half = length // 2
        root = pow(3, MOD // length, MOD)
        if inverse:
            root = pow(root, MOD - 2, MOD)
        for start in range(0, n, length):
            omega = 1
            for i in range(start, start + half):
                t = poly[i + half] * omega % MOD
                poly[i + half] = (poly[i] - t) % MOD
                poly[i] = (poly[i] + t) % MOD
                omega = omega * root % MOD
        length *= 2

    if inverse:
        inv_n = pow(n, MOD - 2, MOD)
        for i in range(n):
            poly[i] = poly[i] * inv_n % MOD

# 두 다항식
a = [5, 3, 1, 6]
b = [3, 8, 3, 5]

# 필요한 길이 계산: 결과 길이는 최대 len(a)+len(b)-1
n = 1
while n < len(a) + len(b) - 1:
    n *= 2

# fft는 2의 거듭제곱 안에서 동작함으로 zero padding
a += [0] * (n - len(a))
b += [0] * (n - len(b))

# FFT
fft(a, False)
fft(b, False)

# 주파수 공간에서 합성
c = [(a[i] * b[i]) % MOD for i in range(n)]

# 계산 결과 푸리에 역변환
fft(c, True)

# 결과 출력: 상수항부터 높은 차수까지
print("최종 계수:", c)
print("결과 다항식:", " + ".join(f"{coef}x^{i}" for i, coef in enumerate(c) if coef != 0))
