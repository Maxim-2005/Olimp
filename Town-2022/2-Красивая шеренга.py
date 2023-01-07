N = int(input())
arr = list(map(int, input().split()))
arr.sort()
for i in range(0, N-1, 2):
	 arr[i], arr[i+1] = arr[i+1], arr[i]
print(*arr)
