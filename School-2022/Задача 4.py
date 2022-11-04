N, K, M = map(int, input().split())

S = N // (K + M) * 2
H = N - S * (K + M) // 2

if H == 0:
	S = S
elif K >= H:
	S += 1
else:
	S += 2

print(S)
