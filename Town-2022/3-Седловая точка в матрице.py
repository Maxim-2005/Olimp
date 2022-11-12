N, M = map(int, input().split())
arr = []
st = res = 0
for i in range(N):
	s = list(map(int, input().split()))
	arr.append(s)
	t = 1e10
	for j in range(M):
		if s[j] < t:
			t = s[j]
			ty = i
	if st < t:
		st = t
		y = ty

for i in range(M):
	if arr[y][i] == st:	
		for j in range(N):
			if arr[j][i] > st:
				break
			if j == N - 1:
				res = str(st) + '\n' + str(y) + ' ' + str(i)
print(res)
