N = int(input())
arr = list(map(int, input().split()))

temp = 0
for i in range(len(arr)):
	arr[i], temp = arr[i] - temp, arr[i]

T = int(input())
for i in range(T):
	L, R, V = map(int, input().split())
	arr[L - 1] += V
	if R < N:
		arr[R] -= V

temp = 0
for i in range(len(arr)):
	arr[i] += temp
	temp = arr[i]

print(*arr)

#N = int(input())
#A = list(map(int, input().split()))
#T = int(input())
#for i in range(T):
#	L, R, V = map(int, input().split())
#	for j in range(L-1, R):
#		A[j] += V
#print(*A)
