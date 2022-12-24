N = int(input())
arr = list(map(int, input().split()))
s = 0
for i in range(N):
	s += (i+1) * arr[i]
m = s

for i in range(N):
	for j in range(i + 1, N):
		t = s - (arr[i] * (i+1) + arr[j] * (j+1)) + (arr[i] * (j + 1) + arr[j] * (i + 1))
		m = max(t, m)

print(m)

# 30 баллов
#N = int(input())
#arr = list(map(int, input().split()))
#s = 0
#
#for i in range(N):
#	s += (i+1) * arr[i]
#
#for i in range(N):
#	for j in range(i + 1, N):
#		arr[i], arr[j] = arr[j], arr[i]
#		t = 0 
#		for n in range(N):
#			t += (n+1) * arr[n]
#		arr[i], arr[j] = arr[j], arr[i]
#		s = max(t, s)
#
#print(s)
