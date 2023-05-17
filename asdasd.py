def count_substrings(s):
	length = len(s)
	count = 0

	for center in range(length):
		left,right = center,center
		while left >= 0 and right < length:
			q = s[center : right+1]
			if s[left : center + 1] == q[::-1]:
				print(s[left : center + 1] + q)
				count += 1
			left -= 1
			right += 1

	return count


n = input()
s = input()
print(count_substrings(s))
