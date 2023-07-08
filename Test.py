def find_closest_sum(n, m, numbers):
    numbers.append(0)
    numbers.sort()
    closest_sum = float('-inf')
    n += 1
    for i in range(n):
        for j in range(n):
            left = 0
            right = n - 1

            while left < right:
                current_sum = numbers[i] + numbers[j] + numbers[left] + numbers[right]

                if current_sum == m:
                    return m

                if current_sum > closest_sum and current_sum < m:
                    closest_sum = current_sum

                if current_sum < m:
                    left += 1
                else:
                    right -= 1

    return closest_sum


n, m = map(int, input().split())
numbers = list(map(int, input().split()))

result = find_closest_sum(n, m, numbers)
print(result)
