A, B = map(int, input().split())
D = min(A % B,  B - (A % B))
mini = D

for i in range(-D, D):
	for j in range(-D, D):
		if ((A + i) % (B + j)) == 0:
			S = abs(i) + abs(j)
			if S < mini:
				mini = S
print(mini)
