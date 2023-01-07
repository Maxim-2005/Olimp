T = int(input())
s = 0

for i in range(T):
	N = int(input())
	arr = list(map(int, input().split()))
	arr.sort()
	arr.reverse()
	for j in range(2, N, 3):
		s += arr[j]
	print(s)
