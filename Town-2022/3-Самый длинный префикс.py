N = int(input())
arr = []
D = 1e2
f = 1
s = 0

for i in range(N):
	arr.append(input())
	D = min(len(arr[i]), D)
	
for i in range(D):
	t = arr[0][i]
	for j in range(N):
		if arr[j][i] != t:
			f = 0
			break
	if f == 0:
		break
	s += 1
print(s)
