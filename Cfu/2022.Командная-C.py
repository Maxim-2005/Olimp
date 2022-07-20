T = int(input())

for i in range(T):
	N = int(input())
	arr = list(map(int, input().split()))
	print((max(arr) - min(arr)) * 2)
